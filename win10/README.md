# Win10

Install [choco](chocolatey.org) package manager from an elevated PowerShell terminal.

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

choco --version
# 1.1.0
```

WSL2 must be installed first and separately to other packages.

```powershell
choco install wsl2 --confirm
```

All remaining packages can be installed.

```
choco install --confirm packages.config
```
