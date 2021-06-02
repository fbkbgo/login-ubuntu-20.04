# login-ubuntu-20.04
Enables login on boot of Ubuntu-20.04 (termux proot-distro) without looping on unrooted android devices.

# Install
- root@localhost:~# apt-get update
- root@localhost:~# apt-get install python3
- root@localhost:~# apt-get install git
- root@localhost:~# git clone https://github.com/fbkbgo/login-ubuntu-20.04.git
- root@localhost:~# python3 un_install.py

# Uninstall
- root@localhost:~# python3 un_install.py

# Note
When uninstalling, the data in ~/.bashrc and /etc/profile.d/termux-proot.sh will be restored to the same old files as before the installation.
