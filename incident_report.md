# Incident Report

## Executive Summary
On April 18, 2026, a Finance department workstation triggered a series of high-severity alerts consistent with phishing-induced malicious execution. The user received an invoice-themed email with a macro-enabled Word attachment. After opening the attachment, Microsoft Word launched PowerShell using an encoded command, followed by suspicious command execution and an outbound connection to an untrusted external IP address.

The evidence indicates likely malicious script execution and possible malware staging. Immediate containment and broader scoping actions are recommended.

## Scope
- Affected user: `jcecil`
- Affected host: `FIN-WS-07`
- Primary data sources: email header sample, EDR alerts, endpoint process logs, firewall logs

## Detailed Findings
1. The email message used an invoice lure directed at a Finance user.
2. The attachment was a `.docm` file, which is capable of running macros.
3. The user opened the file from a local Downloads directory.
4. The Office application then launched `powershell.exe`, which is highly suspicious in this context.
5. The PowerShell command used an encoded payload and hidden window execution.
6. Shortly afterward, the host connected to `185.88.101.42` over TCP port 443.
7. Additional process activity included `cmd.exe` reconnaissance-like commands and `rundll32.exe` loading a DLL from `C:\Users\Public`.

## Assessment
This incident is most consistent with a phishing attack that resulted in malicious script execution on the endpoint. The sequence suggests attempted payload retrieval or post-exploitation staging.

## Impact
Potential impact includes:
- Endpoint compromise
- Credential theft risk
- Malware download and execution
- Potential lateral movement if left uncontained

## MITRE ATT&CK Mapping
- T1566.001 — Phishing: Spearphishing Attachment
- T1204.002 — User Execution: Malicious File
- T1059.001 — Command and Scripting Interpreter: PowerShell
- T1071 — Application Layer Protocol

## Containment and Remediation
- Isolate host `FIN-WS-07`
- Reset user credentials and review identity provider logs
- Block `185.88.101.42` and related indicators
- Review email security logs for the sender and attachment hash
- Scan environment for similar PowerShell and `rundll32.exe` patterns
- Reimage endpoint if compromise is confirmed
- Brief Finance users on invoice-themed phishing attempts

## Lessons Learned
- Finance teams remain high-value targets for invoice phishing
- Office child process monitoring is a strong detection opportunity
- Correlating email, endpoint, and firewall telemetry improves triage accuracy
