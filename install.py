import subprocess
import sys
import os
import shutil
import my_packages

# Automatically get info about user
USERNAME = os.getlogin()
ORIGINAL_DIR = os.getcwd()
HOME_DIR = os.path.expanduser('~')
CONFIG_DIR = HOME_DIR + '/.config'
DOTFILES_DIR = HOME_DIR + '/.dotfiles'

# Helper functions
def greeting():
    subprocess.run(["clear"])
    print("------------------------------------------")
    print("Welcome to the mia dotfiles script 𐔌՞ ܸ.ˬ.ܸ՞𐦯")
    print("------------------------------------------")

    print("This script is a post-install for my dotfiles and it might not work")
    print("in your machine.")
    print("This script installs and configures the most common stuff I dot after a fresh install")
    print("--------------------------------------------------------------------------------------")

    user_choice = input("Do you wish to continue? (y/n) ")
    if user_choice.lower() == "y":
        return
    else:
        print_pretty("Exiting...", "red", True)
        sys.exit()

def get_password():
    print_pretty("Getting password for sudo commands!", "blue", True)
    subprocess.run(["sudo", "ls"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def pacman_helper(package_name):
    # Use paru because it can handle both AUR and non-AUR at the same time
    # 1. Check if its already installed
    p = subprocess.run(["pacman", "-Qi", package_name], capture_output=True)
    if("error" in p.stderr.decode()):
        # 2. If not install it
        try:
            subprocess.run(["paru", "-S", package_name, "--noconfirm"])
            return
        except subprocess.CalledProcessError as E:
            print_pretty(E)
    else:
        print_pretty("Package already installed, skipping.", "blue")
        return
    
def print_pretty(str, color="", bold=False):
    # To print at the right
    term_width = os.get_terminal_size().columns
    icon = "⋆˚꩜"

    match color:
        case "black":
            COLOR = "30m"
        case "red":
            COLOR = "31m"
        case "blue":
            COLOR = "34m"
        case _:
            COLOR = "37m"

    if bold:
        print(f"{'=> '}\033[1;{COLOR}{str}\033[0m")
    else:
        print(f"{'=> '}\033[0;{COLOR}{str}\033[0m")
        print(icon.rjust(term_width - 10))

def setup_paru():
    print_pretty("Installing and confguring Paru!", "blue", True)
    PARU_DIR = HOME_DIR + "/Repos" + "/paru"
    os.chdir(HOME_DIR + "/Repos")
    p = subprocess.run(["git", "clone", "https://aur.archlinux.org/paru.git"], stderr=subprocess.PIPE)

    if ("already exists" in p.stderr.decode()):
        print_pretty("Paru already installed, skipping", "blue")
    else:
        os.chdir(PARU_DIR)
        subprocess.run(["makepkg", "si"])
        os.chdir(ORIGINAL_DIR)

def system_update():
    print_pretty("Updating system!", "blue", True)
    subprocess.run(["sudo", "pacman", "-Syu"],)

def install_packages():
    print_pretty("Installing all packages!", "blue", True)
    for package in my_packages.packages:
        pacman_helper(package)

def install_fonts():
    print_pretty("Installing fonts!", "blue", True)
    # Font viewer pretty useful :D
    pacman_helper("font-manager")
    # Install all fonts
    for font in my_packages.fonts:
        pacman_helper(font)

def run_dotbot():
    print_pretty("Running dotbot!", "blue", True)
    try:
        subprocess.run(["sh", "install-dot", "-v"], cwd=ORIGINAL_DIR)
    except subprocess.CalledProcessError as E:
        print(E)

def setup_cron():
    print_pretty("Installing anc configuring Cron", "blue", True)
    # install cron package
    pacman_helper("cronie")
    # enable cronie service
    try:
        subprocess.run(["systemctl", "enable", "cronie"])
    except subprocess.CalledProcessError as E:
        print(E)

def setup_gamemode():
    print_pretty("Installing and configuring Gamemode!", "blue", True)
    pacman_helper("gamemode")
    pacman_helper("lib32-gamemode")
    try:
        subprocess.run(["sudo", "usermod", "-aG", "gamemode", USERNAME])
    except subprocess.CalledProcessError as E:
        print(E) 
    
def install_grub_theme():
    theme_name = "CelesteGRUBTheme1080p"
    source = DOTFILES_DIR + "/files/grub/" + theme_name
    dest = "/boot/grub/themes/" + theme_name
    grub_dir = "/etc/default/grub"



    #Check if theme is downloaded, if not download it

    # If its a directory
    if os.path.isdir(dest) :
        print_pretty("Theme already exists, overwriting", color="blue")
        subprocess.run(["sudo", "rm", "-r", dest], capture_output=True)

    # If its a file
    elif os.path.isfile(dest) :
        print_pretty("Theme already exists, overwriting", color="blue")
        subprocess.run(["sudo", "rm", dest], capture_output=True)

    print_pretty("Copying theme to" + source, color="blue")
    subprocess.run(["sudo", "cp", "-r", source, dest], capture_output=True)

    # Edit the grub cfg to the theme
    print_pretty("Configuring " + grub_dir, color="blue")
    subprocess.run(
    ["sudo", "sed", "-i", "-e",
    ' s/^GRUB_THEME.*|#GRUB_THEME.*/GRUB_THEME=\/boot\/grub\/themes\/CelesteGRUBTheme1080p/g ', grub_dir]
    )

# ----- #


def run():
    # greeting()
    # get_password()
    # system_update()
    # setup_paru()
    # install_packages()
    # install_fonts()
    # setup_cron()
    # setup_gamemode()
    # run_dotbot()
    install_grub_theme()

# Classic (makes sure it only executes when called form __main__)
if __name__ == "__main__":
    run()

