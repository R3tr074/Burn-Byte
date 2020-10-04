#!/bin/bash
set -u

# First check if the OS is Linux or Mac.
if [[ "$(uname)" = "Linux" ]]; then
  Linux=1
fi

# Second check if the user have the super user powers
if [[ $(id -u) != 0 ]]; then
  echo -e "Permission denied!"
  exit
fi

if [[ -z "${Linux-}" ]]; then
  echo "Installing dependencies(This may take a while)"
  {
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    brew install python3
    brew install git
    git clone https://github.com/R3tr074/burn-byte
    cd burn-byte/
    pip3 install -r requirements.txt
  } &>/dev/null
  python3 burn.py --help

else
  echo "Installing dependencies(This may take a while)"
  {
    apt-get update
    apt-get -y install python3
    apt-get -y install python3-pip
    apt-get -y install git

    pkg update
    pkg -y install python3
    pkg -y install python3-pip
    pkg -y install git

    apk update
    apk add python3
    apk add python3-pip
    apk add git

    pacman -Sy
    pacman -S --noconfirm python3
    pacman -S --noconfirm python3-pip
    pacman -S --noconfirm git

    zypper refresh
    zypper install -y python3
    zypper install -y python3-pip
    zypper install -y git

    yum -y install python3
    yum -y install python3-pip
    yum -y install git

    dnf -y install python3
    dnf -y install python3-pip
    dnf -y install git

    eopkg update-repo
    eopkg -y install python3
    eopkg -y install python3-pip
    eopkg -y install git

    xbps-install -S
    xbps-install -y python3
    xbps-install -y python3-pip
    xbps-install -y git

    git clone https://github.com/R3tr074/burn-byte
    cd burn-byte
    pip3 install -r requirements.txt
  } &>/dev/null
  python3 burn.py --help
fi
