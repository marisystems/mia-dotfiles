import subprocess
import os
# Get all the pacman packages
import packages

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
    print("Enter your sudo password below")
    subprocess.run(["sudo", "ls"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def pacman_helper(package_name):
    # 1. Check if its already installed
    p = subprocess.run(["pacman", "-Qi", package_name], capture_output=True)
    if("error" in p.stderr.decode()):
        # 2. If not install it
        try:
            subprocess.run(["sudo", "pacman", "-S", package_name, "--noconfirm"])
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
    subprocess.run(["sudo", "pacman", "-Syu"],)

def install_packages():
    pass

def run_dotbot():
    pass

def setup_cron():
    # install cron package
    # enable cronie service
    pass

def setup_gamemode():
    #stuff
    pass

def setup_fonts():
    # Font viewer pretty useful :D
    pacman_helper("font-manager")
    # Install all fonts
    for font in packages.fonts:
        pacman_helper(font)

# ----- #

def run():
    get_password()
    setup_fonts()
    
    
    for font in packages.fonts:
        pacman_helper(font)

# Classic
if __name__ == "__main__":
    run()

