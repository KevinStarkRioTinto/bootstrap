# Windows Subsystem for Linux

```powershell
# Set the default wsl version
wsl --set-default-version 2
# Install latest Ubunut LTS 
# Creates an application "Ubuntu" in the start menu
choco install 'wsl-ubuntu-2204'
# Set the new distro as default
wsl --set-default Ubuntu
```

On first run of Ubuntu application, set `user` as `wsl`. This will result in the terminal showing:
```sh
wsl@<machine>:~$
```

## Ubuntu Developer Setup

Disable bell

```sh
sudo nano /etc/inputrc
# Uncomment lines:
# set bell-style none
# set bell-style visible
```

Configure artifactory and config-rio

```sh
sudo mkdir /etc/environment.d
sudo nano /etc/environment.d/artifactory.conf
# set:
# ARTIFACTORY_USER=<email>
# ACCESS_TOKEN=<PAT>
```


```sh
sudo nano /usr/local/bin/config-rio
# > https://github.com/rio-tinto/PACE-Config-Scripts/blob/main/wsl/config-rio.sh
sudo chmod +x /usr/local/bin/config-rio
sudo config-rio
# Check/edit nameservers in /etc/resolv.conf
# Add:
# nameserver 1.1.1.1
cat /etc/resolv.conf
# Update wget with ssl cert path
printf "\nca_directory=/etc/ssl/certs" | sudo tee -a /etc/wgetrc
```

```sh
sudo apt update
sudo apt upgrade
```

Install common developer tools

```sh
sudo apt install -y \
    make \
    jq \
    unzip
```

Add python repository for multiple version installs

```sh
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update 
#sudo apt install python3.11
#sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11
python3 --version
# Install venv tools for default python version
sudo apt install python3.10-venv
```

Install/enable docker

https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers

1. Open Docker Desktop on Windows
2. Settings -> Resources -> WSL Integration
3. Disable -> Apply, Enable -> Apply
4. **Restart wsl terminal**

```sh
# Verify no docker permission errors
docker ps
docker run hello-world
```

Install CUDA

https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_network

```sh
# Verify cuda in docker
docker run -it --gpus=all --rm nvidia/cuda:11.4.2-base-ubuntu20.04 nvidia-smi -L
# GPU 0: Quadro T2000 with Max-Q Design ...
```

Install AWS

https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

```sh
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```
Set browser environment var for sso integration
```sh
echo "export BROWSER='/mnt/c/Program Files/Google/Chrome/Application/chrome.exe'" | tee -a ~/.bashrc
```

[Install poetry](https://python-poetry.org/docs/)

If error, likely being intercepted by zscaler - open the link manually in a browser to allow it.

```sh
curl -sSL https://install.python-poetry.org | python3 -
```