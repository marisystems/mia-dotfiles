import subprocess
import os
# Get all the pacman packages
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

def get_password():
    print_pretty("Getting password for sudo commands!", "blue", True)
    print("Enter your sudo password below")
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

def pacman_update():
    print_pretty("Updating system!", "blue", True)
    subprocess.run(["sudo", "pacman", "-Syu"],)

def install_packages():
    print_pretty("Installing all packages!", "blue", True)
    for package in my_packages.packages:
        pacman_helper(package)

def run_dotbot():
    print_pretty("Running dotbot!", "blue", True)
    try:
        subprocess.run(["sh", "install-dot", "-v"])
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
    

def setup_fonts():
    print_pretty("Installing fonts!", "blue", True)
    # Font viewer pretty useful :D
    pacman_helper("font-manager")
    # Install all fonts
    for font in my_packages.fonts:
        pacman_helper(font)

# ----- #

def run():
    greeting()
    get_password()

    
# Classic
if __name__ == "__main__":
    run()

