# mia.files 🗄️

> Using [dotbot⚡️](https://github.com/anishathalye/dotbot) to manage my files, check it out its pretty cool!

These dotfiles are meant to be used with an arch
linux based distro, but probs work in other distros 
(at the time of writing I'm using CachyOS with KDE Plasma)

## Components
- WM : **Hyprland / KDE**
- Display Manager: **SDDM**
- Shell : **Fish**
- Package manager: **pacman & paru**
- Terminal emulator: **Kitty**
- Font : **Victor Mono Nerd*

## Overview 
While the symlinking will be done using the dotbot utility
the installation and further setup using specific commands
will be handled with the install.py

## Instructions
1. Git clone this repo
- ```git clone git@github.com:marisystems/mia-dotfiles.git ~/.dotfiles``` for SSH
- ```git clone https://github.com/marisystems/mia-dotfiles.git ~/.dotfiles``` for HTTPS
2. cd into ~/.dotfiles
3. Run python install.py to download all packages
4. Whenever you need to remake symlinks and add new ones
configure dotbot.yaml and run ./install-dot (-vv for verbose)
## To-do
- [] Create python script for post-install
- [] Create file with all the packages I want
- [] Separate the files into modules so i can pick and choose
- [] Integrate with dotbot
- [] Create option to use either hyprland or plasma
