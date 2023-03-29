
Change settings for sleep under Power and Privacy in settings

Install  random apps

```zsh
sudo dnf install pinta
```
Generate ssh keys add to git account

```zsh
sudo dnf install zsh util-linux-user
chsh -s $(which zsh)
# run zsh to configure (automate this)
# Install Oh My zsh
sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
```

Configure ssh

```zsh
  git config --global user.email "eddie@eddiedunn.com"
  git config --global user.name "eddiedunn"
```

Change default editor to vi 

```zsh
dnf remove nano-default-editor
sudo dnf install -y vim-default-editor
# add nano back
sudo dnf install nano
```


Install nvidia drive with cuda
loosly (from https://www.linuxcapable.com/how-to-install-nvidia-drivers-on-fedora-linux/)

add cuda developer repo for correct fedora version

```zsh
sudo dnf config-manager --add-repo https://developer.download.nvidia.com/compute/cuda/repos/fedora37/x86_64/cuda-fedora37.repo
```

Install dependencies

```zsh
sudo dnf install kernel-headers kernel-devel tar bzip2 make automake gcc gcc-c++ pciutils elfutils-libelf-devel libglvnd-opengl libglvnd-glx libglvnd-devel acpid pkgconfig dkms
```

Install cuda as well as nvidia driver

```zsh
sudo dnf install cuda
```

Install ChatGPT

```zsh
mkdir /opt/ChatGPT-Desktop
wget https://github.com/lencx/ChatGPT/releases/download/v0.12.0/ChatGPT_0.12.0_linux_x86_64.AppImage.tar.gz -P /opt/ChatGPT-Desktop
cp files/chatgpticon.png /opt/ChatGPT-Desktop
cp files/ChatGPT.desktop /usr/share/applications
```

Add rpmfusion repos

```zsh
sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
sudo dnf install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

Install Discord

```zsh
sudo dnf install discord
```

Install vscode

```zsh
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
sudo dnf install code
```


Install Sublime

```zsh
sudo rpm -v --import https://download.sublimetext.com/sublimehq-rpm-pub.gpg
sudo dnf config-manager --add-repo https://download.sublimetext.com/rpm/stable/x86_64/sublime-text.repo
sudo dnf install sublime-text
```


