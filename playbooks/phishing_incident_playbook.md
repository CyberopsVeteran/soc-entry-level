# 🚨 SOC Playbook: Phishing → PowerShell Incident Response

## 📌 Overview

This playbook outlines the standard operating procedure (SOP) for handling a phishing incident that leads to endpoint compromise via PowerShell execution and potential outbound communication.

---

## 🎯 Objective

- Detect and validate phishing activity
- Investigate endpoint and network behavior
- Contain and eradicate threats
- Restore systems safely
- Document findings and improve defenses

---

## ⚠️ Incident Scope

This playbook applies when:
- A phishing email is reported or detected
- Suspicious PowerShell activity is observed
- Outbound network connections to unknown IPs are identified

---

## 🧠 Roles & Responsibilities

| Role | Responsibility |
|------|---------------|
| Tier 1 Analyst | Triage alerts, collect initial evidence |
| Tier 2 Analyst | Deep investigation and correlation |
| Incident Responder | Containment, eradication, recovery |
| SOC Manager | Oversight and escalation decisions |

---

## 🔍 Phase 1: Triage

### Objective
Determine whether the alert is a true positive.

### Steps
- Review SIEM alert details
- Identify affected user and host
- Examine email subject and sender
- Check for known phishing indicators (urgent language, spoofed domain)

### Tools / Data Sources
- SIEM alerts
- Email logs

### Output
- Alert classification (True Positive / False Positive)
- Escalation decision

---

## 🧪 Phase 2: Investigation

### Objective
Understand attack behavior and scope.

### Steps
- Analyze email headers to identify origin
- Review endpoint logs for PowerShell execution
- Detect encoded or suspicious commands
- Correlate firewall logs for outbound connections
- Build incident timeline
- Identify Indicators of Compromise (IOCs)

### Tools / Data Sources
- Endpoint logs (Sysmon / EDR)
- Firewall logs
- Email headers
- SIEM platform

### Output
- Timeline of events
- IOC list
- Confirmed attack chain

---

## 🧬 MITRE ATT&CK Mapping

| Technique | Description |
|----------|------------|
| T1566 | Phishing |
| T1059 | Command and Scripting Interpreter (PowerShell) |
| T1071 | Application Layer Protocol |

---

## 🛑 Phase 3: Containment

### Objective
Prevent further spread of the attack.

### Steps
- Isolate affected host from network
- Block malicious IP addresses
- Disable or reset compromised user account

### Tools
- EDR / Endpoint control
- Firewall
- Identity management system

### Output
- Threat contained to affected system

---

## 🧹 Phase 4: Eradication

### Objective
Remove all traces of malicious activity.

### Steps
- Remove malicious files and processes
- Check for persistence mechanisms (registry, scheduled tasks)
- Perform full system scan

### Tools
- EDR / Antivirus
- System inspection tools

### Output
- System cleaned and verified

---

## 🔄 Phase 5: Recovery

### Objective
Restore system to normal operation.

### Steps
- Reconnect system to network
- Validate system functionality
- Monitor logs for reinfection

### Output
- System returned to production safely

---

## 📘 Phase 6: Lessons Learned

### Objective
Improve detection and response capabilities.

### Steps
- Update phishing detection rules
- Improve PowerShell monitoring alerts
- Update SOC playbooks and procedures
- Conduct user awareness training

### Output
- Enhanced security posture

---

## 📊 Key Metrics

- Time to Detect (TTD)
- Time to Respond (TTR)
- Number of affected hosts
- Number of alerts triggered

---

## 🧾 Documentation Requirements

- Incident report
- IOC list
- Timeline
- Analyst notes
- Detection improvements

---

## ⚠️ Escalation Criteria

Escalate to Tier 2 or Incident Response team if:
- Multiple hosts are affected
- Evidence of lateral movement
- Data exfiltration suspected
- Privileged accounts compromised

---

## 🔮 Future Improvements

- Integrate SIEM dashboards (e.g., Splunk or Sentinel)
- Automate detection rules
- Enhance threat hunting capabilities
- Improve email filtering systems

---

## ✅ Summary

This playbook ensures a structured and repeatable response to phishing incidents, enabling SOC analysts to quickly detect, investigate, and contain threats while improving future defenses.
