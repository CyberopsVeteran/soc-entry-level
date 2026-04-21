from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

SUSPICIOUS_IPS = {"185.88.101.42"}
SUSPICIOUS_PARENTS = {"WINWORD.EXE", "EXCEL.EXE", "OUTLOOK.EXE"}
SUSPICIOUS_CHILDREN = {"powershell.exe", "cmd.exe", "wscript.exe", "cscript.exe", "rundll32.exe"}


def load_csv(name: str) -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / name)


def analyze_alerts(alerts: pd.DataFrame) -> pd.DataFrame:
    return alerts[alerts["severity"].isin(["High", "Critical"])]


def analyze_endpoint_events(events: pd.DataFrame) -> pd.DataFrame:
    suspicious_rows = []

    for _, row in events.iterrows():
        reasons = []
        parent = str(row["parent_process"])
        child = str(row["process_name"])
        command = str(row["command_line"])

        if parent in SUSPICIOUS_PARENTS and child in SUSPICIOUS_CHILDREN:
            reasons.append("Office application spawned suspicious child process")

        if child.lower() == "powershell.exe" and "-enc" in command.lower():
            reasons.append("Encoded PowerShell detected")

        if child.lower() == "rundll32.exe" and "users\\public" in command.lower():
            reasons.append("DLL executed from user-accessible path")

        if reasons:
            enriched = row.to_dict()
            enriched["reason"] = "; ".join(reasons)
            suspicious_rows.append(enriched)

    return pd.DataFrame(suspicious_rows)


def analyze_firewall_logs(logs: pd.DataFrame) -> pd.DataFrame:
    return logs[logs["dest_ip"].isin(SUSPICIOUS_IPS)]


def main() -> None:
    alerts = load_csv("alerts.csv")
    events = load_csv("endpoint_events.csv")
    firewall = load_csv("firewall_logs.csv")

    suspicious_alerts = analyze_alerts(alerts)
    suspicious_events = analyze_endpoint_events(events)
    suspicious_connections = analyze_firewall_logs(firewall)

    print("=" * 72)
    print("SOC Detection Results")
    print("=" * 72)

    print("\n[1] High/Critical Alerts")
    if suspicious_alerts.empty:
        print("No high severity alerts found.")
    else:
        print(suspicious_alerts.to_string(index=False))

    print("\n[2] Suspicious Endpoint Events")
    if suspicious_events.empty:
        print("No suspicious endpoint events found.")
    else:
        print(suspicious_events.to_string(index=False))

    print("\n[3] Suspicious Firewall Connections")
    if suspicious_connections.empty:
        print("No suspicious external connections found.")
    else:
        print(suspicious_connections.to_string(index=False))

    print("\n[4] Analyst Assessment")
    if not suspicious_events.empty and not suspicious_connections.empty:
        print("Likely phishing-related malicious execution with outbound network activity.")
    else:
        print("Additional investigation required.")


if __name__ == "__main__":
    main()
