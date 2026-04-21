# SOC Analyst Home Lab Project: Suspicious PowerShell Phishing Investigation

A beginner-friendly, recruiter-ready Security Operations Center (SOC) project designed for GitHub. This project simulates a realistic entry-level analyst workflow: reviewing alerts, parsing logs, identifying phishing activity, analyzing suspicious PowerShell execution, documenting findings, and recommending containment actions.

## Project Goal

Demonstrate hands-on SOC skills that align with entry-level analyst roles:

- Alert triage
- Log analysis
- Investigating phishing-related activity
- Identifying suspicious PowerShell behavior
- Mapping activity to MITRE ATT&CK
- Writing an incident report and analyst notes
- Recommending containment and remediation actions

## Scenario Summary

A user in the Finance department reported a suspicious email attachment that appeared to be an invoice. Shortly afterward, multiple alerts were generated involving PowerShell, encoded commands, and an external network connection to a suspicious IP address.

You are the SOC analyst assigned to investigate.

## Skills Demonstrated

- Security alert triage
- Windows event log analysis
- Basic threat detection with Python
- CSV and JSON parsing
- IOC extraction
- Timeline building
- Incident documentation
- MITRE ATT&CK mapping
- Professional reporting for leadership and technical teams

## Repository Structure

```text
soc_entry_level_project/
├── README.md
├── requirements.txt
├── data/
│   ├── alerts.csv
│   ├── endpoint_events.csv
│   ├── email_headers.txt
│   ├── firewall_logs.csv
│   └── users.csv
├── docs/
│   ├── incident_report.md
│   ├── investigation_notes.md
│   ├── iocs.md
│   └── timeline.md
├── scripts/
│   ├── detect_suspicious_activity.py
│   └── build_timeline.py
└── images/
    └── architecture_overview.md
```

## Dataset Overview

### `data/alerts.csv`
Contains simulated SOC alerts from endpoint and email security tools.

### `data/endpoint_events.csv`
Contains a simplified endpoint event dataset with process creation activity.

### `data/firewall_logs.csv`
Contains outbound network activity from the affected host.

### `data/email_headers.txt`
Contains a suspicious email header sample for review.

### `data/users.csv`
Contains a simple inventory of users and departments.

## Tools Used

- Python
- pandas
- Standard SOC analysis workflow
- MITRE ATT&CK framework
- GitHub markdown documentation

## How to Run

1. Clone or download the repository.
2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

3. Run the detection script:

```bash
python scripts/detect_suspicious_activity.py
```

4. Build the incident timeline:

```bash
python scripts/build_timeline.py
```

## What the Scripts Do

### `detect_suspicious_activity.py`
Reviews alerts, endpoint events, and firewall logs to flag:

- Encoded PowerShell execution
- Office applications spawning script interpreters
- Connections to suspicious external IPs
- High severity alerts

### `build_timeline.py`
Creates an investigator-friendly timeline from endpoint, firewall, and alert data.

## Key Findings

- A suspicious email pretending to be an invoice was delivered to a Finance user.
- The user opened a file that launched a suspicious process chain.
- `WINWORD.EXE` spawned `powershell.exe`, which is abnormal for normal business activity.
- PowerShell executed with an encoded command.
- The affected host connected outbound to a suspicious IP shortly after execution.
- The activity is consistent with early-stage phishing and possible malware execution.

## MITRE ATT&CK Mapping

| Technique | ID | Relevance |
|---|---|---|
| Phishing: Spearphishing Attachment | T1566.001 | Initial access via malicious attachment |
| Command and Scripting Interpreter: PowerShell | T1059.001 | Suspicious PowerShell execution |
| User Execution | T1204 | User likely opened attachment |
| Malicious File | T1204.002 | Execution of delivered file |
| Application Layer Protocol | T1071 | Outbound communication over common protocol |

## Analyst Recommendations

1. Isolate the affected host from the network.
2. Reset the impacted user's password and review sign-in logs.
3. Block the suspicious IP and related domain indicators.
4. Hunt for similar PowerShell encoded command usage across endpoints.
5. Search mailboxes for similar invoice-themed phishing emails.
6. Reimage the system if malware execution is confirmed.
7. Update email filtering and user awareness guidance.

## Why This Project Is Valuable for GitHub

This repository shows employers that you can:

- Work through an end-to-end SOC case
- Analyze different log sources
- Document technical findings clearly
- Turn raw evidence into actionable recommendations
- Present your work like a real analyst instead of just listing certifications

## Resume Bullet Example

- Built a hands-on SOC investigation project in Python simulating phishing-driven PowerShell execution, analyzed endpoint, email, and firewall logs, mapped findings to MITRE ATT&CK, and produced a full incident report with IOCs and remediation steps.

## Suggested GitHub Repo Name

- `soc-phishing-powershell-investigation`
- `entry-level-soc-analyst-project`
- `soc-alert-triage-home-lab`

## Next Improvements

- Add Sigma rules
- Add Splunk or Elastic queries
- Add a dashboard screenshot from a SIEM home lab
- Add YARA or hash analysis
- Convert the data into JSONL for easier ingestion into a SIEM

## Author

Replace this section with your name, LinkedIn, and GitHub profile.
