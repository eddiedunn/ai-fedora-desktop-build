Fix freeze issue for Ryzen

output of echo rcu_nocbs=0-$(($(nproc)-1)) 
to get numbers these are for 6 core ryzen CPU
grubby --args="processor.max_cstate=5 rcu_nocbs=0-11" --update-kernel=ALL

Change settings for sleep under Power and Privacy in settings

Setup Software RAID using mdadm on install

If using mdadm configure alerts so you will see them

# don't forget to enable the monitor service
systemctl enable --now mdadm-monitor.service

# NOTE: must configure SMTP
https://www.recitalsoftware.com/blogs/175-howto-use-a-gmail-account-to-relay-email-from-a-shell-prompt-on-redhat-centos-fedora

# to test
mdadm --monitor --scan --test -1



https://github.com/devangshekhawat/Fedora-37-Post-Install-Guide

Install Gnome extensions firefox browser plug-in (extension)
https://extensions.gnome.org/

Click the link in the box at top

Install  random apps

```zsh
sudo dnf install -y pinta gnome-tweaks lm_sensors htop iotop
```

Change scaling factor on font to adjust text size

Generate ssh keys add to git account

```zsh
sudo dnf install -y zsh util-linux-user
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
sudo dnf install -y kernel-headers kernel-devel tar bzip2 make automake gcc gcc-c++ pciutils elfutils-libelf-devel libglvnd-opengl libglvnd-glx libglvnd-devel acpid pkgconfig dkms
```

Install latest cuda (12.1 as of this writing) as well as latest nvidia driver (530 as of now)

```zsh
sudo dnf install -y cuda
```

Install ChatGPT (Be sure and goto Preferences -> sync prompts)

```zsh
mkdir /opt/ChatGPT-Desktop
wget https://github.com/lencx/ChatGPT/releases/download/v0.12.0/ChatGPT_0.12.0_linux_x86_64.AppImage.tar.gz -P /opt/ChatGPT-Desktop
cp files/chatgpticon.png /opt/ChatGPT-Desktop
cp files/ChatGPT.desktop /usr/share/applications
```

Add rpmfusion repos

```zsh
sudo dnf install -y https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
sudo dnf install -y https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

Install Discord

```zsh
sudo dnf install discord
```

Install vscode

```zsh
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
sudo dnf -y install code
```


Install Sublime

```zsh
sudo rpm -v --import https://download.sublimetext.com/sublimehq-rpm-pub.gpg
sudo dnf config-manager --add-repo https://download.sublimetext.com/rpm/stable/x86_64/sublime-text.repo
sudo dnf install -y sublime-text
```

Install pyenv
https://github.com/pyenv/pyenv

```zsh
curl https://pyenv.run | bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# For non-interactive shells
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zprofile
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zprofile
echo 'eval "$(pyenv init -)"' >> ~/.zprofile
```

Install Cuda 11.7

```zsh
wget https://developer.download.nvidia.com/compute/cuda/11.7.1/local_installers/cuda_11.7.1_515.65.01_linux.run
sudo sh cuda_11.7.1_515.65.01_linux.run --toolkit --silent --override --toolkitpath=/opt/cuda-11.7.1
# TDOD scripts to switch
```

Install gcc 11.2

```zsh
sudo dnf groupinstall -y "Development Tools"
sudo dnf install -y  mpfr-devel libmpc-devel gmp-devel zlib-devel
wget https://ftp.gnu.org/gnu/gcc/gcc-11.2.0/gcc-11.2.0.tar.gz
tar xf gcc-11.2.0.tar.gz
mkdir gcc-11.2.0-build
cd gcc-11.2.0-build
../gcc-11.2.0/configure --prefix=/opt/gcc-11.2.0 --enable-languages=c,c++ --disable-bootstrap --disable-multilib --disable-bootstrap --disable-libsanitizer
make -j$(nproc)
sudo make install
sudo cp [repodir]/files/gcc-remove-11.2.0.sh /usr/local/bin
sudo cp [repodir]/files/gcc-add-11.2.0.sh /usr/local/bin
chmod 755 /usr/local/bin/gcc-remove-11.2.0.sh
chmod 755 /usr/local/bin/gcc-add-11.2.0.sh
```

Add scripts to switch between both gcc 11.2 and cuda 11.7

```zsh
sudo cp [repodir]/files/gcc-cuda-remove-11.2.0-11.7.sh /usr/local/bin
sudo cp [repodir]/files/gcc-cuda-add-11.2.0-11.7.sh /usr/local/bin
chmod 755 /usr/local/bin/gcc-cuda-add-11.2.0-11.7.sh
chmod 755 /usr/local/bin/gcc-cuda-add-11.2.0-11.7.sh
```
