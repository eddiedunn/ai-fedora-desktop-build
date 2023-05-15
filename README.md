# Here are my steps to get setup a new Fedora build for AI

Setup Software RAID 1 for system drive and any data drives using mdadm on install



Copy dot files inspired by
https://github.com/geerlingguy/dotfiles
 
```zsh
cp files/.gitconfig ~
cp files/.gitignore ~/.gitignore_global
cp files/.vimrc ~
git config --global core.excludesfile ~/.gitignore_global
```

https://github.com/devangshekhawat/Fedora-37-Post-Install-Guide

Install Gnome extensions firefox browser plug-in (extension)
https://extensions.gnome.org/

Click the link in the box at top

Install  random apps

```zsh
sudo dnf install -y pinta gnome-tweaks lm_sensors htop iotop golang
sudo dnf install gstreamer1-libav gstreamer1-plugins-ugly gstreamer1-plugins-bad-free gstreamer1-plugins-bad-freeworld gstreamer1-plugins-base-tools gstreamer1-plugins-good gstreamer1-plugins-good-extras ffmpeg

```

Change scaling factor on font to adjust text size

Generate ssh keys add to git account


# Install zsh and 

```zsh
sudo dnf install -y zsh util-linux-user
chsh -s $(which zsh)
# run zsh to configure (automate this)
# Install Oh My zsh
sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
```
add this to the bottom of ~/.zshrc


Change default editor to vi 

```zsh
dnf remove nano-default-editor
sudo dnf install -y vim-default-editor 
# add nano back
sudo dnf install nano
```

Install phantomjs ( for yt_dlp )


```zsh
sudo dnf install glibc fontconfig freetype freetype-devel fontconfig-devel wget bzip2

wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
sudo tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 -C /usr/local/share/
mv /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/myphantomjs
cp files/phantomjs /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs
chmod +x  /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs
sudo ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin
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

Add rpmfusion repos

```zsh
sudo dnf install -y https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
sudo dnf install -y https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

Install Discord

```zsh
sudo dnf install discord
```

Install Zoom

```zsh
# Dependencies
sudo dnf install libc.so.6 libX11.so.6 libXfixes.so.3 libglib-2.0.so.0 libGL.so.1 libsqlite3.so.0 libXrender.so.1 libXcomposite.so.1 libQt3Support.so.4 libxslt.so.1 libpulse.so.0 libgthread-2.0.so.0 libxcb-shape.so.0 libxcb-shm.so.0 libxcb-randr.so.0 libxcb-image.so.0 libxcb-xtest.so.0 libxcb-keysyms.so.1 mesa-dri-drivers ibus

wget https://zoom.us/client/latest/zoom_x86_64.rpm
sudo dnf install zoom_x86_64.rpm
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
sudo dnf groupinstall -y "Development Tools"
sudo dnf install zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel libffi-devel findutils -y

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


```zfs
curl -sL "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh" > "Miniconda3.sh"
bash Miniconda3.sh
conda config --set auto_activate_base false

sudo dnf install -y cairo-devel gobject-introspection-devel cairo-gobject-devel
```
