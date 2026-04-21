# Investigation Notes

## Case ID
SOC-2026-0418-001

## Assigned Analyst
Your Name Here

## Summary
A Finance workstation generated multiple alerts shortly after a suspicious invoice-themed email was delivered. Evidence shows a Microsoft Word document spawned PowerShell with an encoded command, followed by outbound network traffic to a suspicious external IP.

## Initial Triage
- High confidence phishing-related activity
- Host involved: `FIN-WS-07`
- User involved: `jcecil`
- Multiple corroborating alerts across email, endpoint, and firewall telemetry

## Evidence Reviewed
- Email delivery alert
- Endpoint process creation logs
- Firewall outbound connection logs
- User report to help desk
- Email header sample

## Suspicious Process Chain
`OUTLOOK.EXE` → `WINWORD.EXE` → `powershell.exe` → `cmd.exe` / `rundll32.exe`

## Why This Is Suspicious
- Office applications do not normally spawn hidden, encoded PowerShell in standard business workflows.
- The PowerShell command used `-enc`, a common defense evasion and obfuscation pattern.
- `rundll32.exe` executed a DLL from a public user-accessible path.
- External connection occurred immediately after script execution.

## Triage Assessment
This activity likely represents a successful phishing attempt with script-based payload execution.

## Recommended Containment
- Isolate `FIN-WS-07`
- Block `185.88.101.42`
- Acquire the email and attachment for malware analysis
- Reset impacted credentials
- Search for the same sender and attachment across mailboxes
