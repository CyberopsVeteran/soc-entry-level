# 🚨 SOC Playbook: Ransomware Incident Response

## 📌 Overview
This playbook outlines response procedures for ransomware infections affecting endpoints or servers.

---

## 🎯 Objective
- Detect ransomware activity
- Contain spread
- Preserve evidence
- Restore systems

---

## ⚠️ Indicators of Ransomware
- File encryption activity
- Unusual file extensions
- Ransom notes
- High CPU/disk usage
- Mass file modifications

---

## 🔍 Phase 1: Triage
- Review SIEM/EDR alerts
- Identify affected systems
- Confirm ransomware indicators

---

## 🧪 Phase 2: Investigation
- Identify initial infection vector (phishing, exploit)
- Determine scope (single vs multiple hosts)
- Check for lateral movement
- Identify affected files

---

## 🛑 Phase 3: Containment
- Immediately isolate infected systems
- Disable network shares
- Block malicious IPs/domains
- Disable compromised accounts

---

## 🧹 Phase 4: Eradication
- Remove malware
- Reimage systems if necessary
- Remove persistence mechanisms

---

## 🔄 Phase 5: Recovery
- Restore from backups
- Validate system integrity
- Monitor for reinfection

---

## 📘 Phase 6: Lessons Learned
- Improve backup strategy
- Enhance endpoint protection
- Update patching policies

---

## ⚠️ Escalation Criteria
- Multiple systems affected
- Critical infrastructure impacted
- Data exfiltration suspected

---

## 🧬 MITRE ATT&CK
- T1486 – Data Encrypted for Impact
- T1059 – Command Execution
