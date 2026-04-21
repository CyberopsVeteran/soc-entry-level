# Indicators of Compromise (IOCs)

## IP Addresses
- `185.88.101.42`

## File Names
- `Invoice_April_2026.docm`
- `update.dll`

## Domains
- `vendor-payments-example.com`
- `malicious-domain.example`

## Commands
- `powershell.exe -nop -w hidden -enc ...`
- `rundll32.exe C:\Users\Public\update.dll,Start`

## Behavioral Indicators
- Office spawning PowerShell
- Encoded PowerShell execution
- DLL execution from user-writable location
- Rapid outbound connection after macro execution
