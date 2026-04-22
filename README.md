# mia.files 🗄️

> Using [dotbot⚡️](https://github.com/anishathalye/dotbot) to manage my files, check it out its pretty cool!

These dotfiles are meant to be used with an arch
linux based distro, but probs work in other distros 
(at the time of writing I'm using CachyOS with KDE Plasma)

## Components
- Shell : **ZSH**
- Package manager: **pacman & yay**
- Terminal emulator: **Kitty**
- Font : **Victor Mono Nerd*

## Instructions
1. Git clone this repo
- ```git clone git@github.com:marisystems/mia-dotfiles.git ~/.dotfiles``` for SSH
- ```git clone https://github.com/marisystems/mia-dotfiles.git ~/.dotfiles``` for HTTPS
2. cd into ~/.dotfiles
3. Run ./install (you can run ./install -vv for more information)
4. Run zsh/oh-my-zsh-repo/tools/.install

## To-do
- [] Create python script for post-install
- [] Create file with all the packages I want
- [] Separate the files into modules so i can pick and choose
- [] Integrate with dotbot