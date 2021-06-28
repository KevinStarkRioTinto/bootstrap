# Win10

Install [choco](chocolatey.org) package manager from an elevated PowerShell terminal.

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

choco --version
# 0.10.15
```

```powershell
choco install wsl2 --confirm

choco install \
  anaconda3
  docker-desktop
  firacode
  gh
  git
  github-desktop
  microsoft-windows-terminal
  powershell-core
  r.studio

  open-jdk
  graphvis
```
