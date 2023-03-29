Generate ssh keys add to git account

Configure ssh

  git config --global user.email "eddie@eddiedunn.com"
  git config --global user.name "eddiedunn"



Build steps to automate

Install nvidia drive with cuda
loosly (from https://www.linuxcapable.com/how-to-install-nvidia-drivers-on-fedora-linux/)

add cuda developer repo for correct fedora version

```zsh
sudo dnf config-manager --add-repo https://developer.download.nvidia.com/compute/cuda/repos/fedora37/x86_64/cuda-fedora37.repo
```

Install dependencies

sudo dnf install kernel-headers kernel-devel tar bzip2 make automake gcc gcc-c++ pciutils elfutils-libelf-devel libglvnd-opengl libglvnd-glx libglvnd-devel acpid pkgconfig dkms

Install cuda

sudo dnf install cuda


