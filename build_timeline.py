from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
DOCS_DIR = BASE_DIR / "docs"


def load_csv(name: str) -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / name)


def build_timeline() -> pd.DataFrame:
    alerts = load_csv("alerts.csv")[["timestamp", "alert_name", "description"]].copy()
    alerts["source_type"] = "alert"
    alerts.rename(columns={"alert_name": "event", "description": "details"}, inplace=True)

    endpoint = load_csv("endpoint_events.csv")[["timestamp", "process_name", "command_line"]].copy()
    endpoint["source_type"] = "endpoint"
    endpoint.rename(columns={"process_name": "event", "command_line": "details"}, inplace=True)

    firewall = load_csv("firewall_logs.csv")[["timestamp", "dest_ip", "dest_port", "action"]].copy()
    firewall["source_type"] = "firewall"
    firewall["event"] = "network_connection"
    firewall["details"] = firewall.apply(
        lambda row: f"{row['action']} connection to {row['dest_ip']}:{row['dest_port']}", axis=1
    )
    firewall = firewall[["timestamp", "event", "details", "source_type"]]

    combined = pd.concat([alerts, endpoint, firewall], ignore_index=True)
    combined["timestamp"] = pd.to_datetime(combined["timestamp"])
    combined = combined.sort_values("timestamp").reset_index(drop=True)
    return combined


def save_timeline_markdown(df: pd.DataFrame) -> None:
    output_path = DOCS_DIR / "generated_timeline.md"
    with output_path.open("w", encoding="utf-8") as f:
        f.write("# Generated Timeline\n\n")
        f.write("| Timestamp | Source | Event | Details |\n")
        f.write("|---|---|---|---|\n")
        for _, row in df.iterrows():
            timestamp = row["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
            source = row["source_type"]
            event = str(row["event"]).replace("|", "/")
            details = str(row["details"]).replace("|", "/")
            f.write(f"| {timestamp} | {source} | {event} | {details} |\n")


if __name__ == "__main__":
    timeline = build_timeline()
    save_timeline_markdown(timeline)
    print(timeline.to_string(index=False))
    print(f"\nSaved markdown timeline to: {DOCS_DIR / 'generated_timeline.md'}")
