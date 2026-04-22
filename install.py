import subprocess
import os
from enum import Enum

# Helper functions
def greeting():
    subprocess.run(["clear"])
    print("------------------------------------------")
    print("Welcome to the mia dotfiles script 𐔌՞ ܸ.ˬ.ܸ՞𐦯")
    print("------------------------------------------")
    
def get_password():
    print("Enter your sudo password below")
    subprocess.run(['sudo', 'ls'], stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)

def print_pretty(str, color="", bold=False):
    # To print at the right
    term_width = os.get_terminal_size().columns
    icon = "⋆˚꩜"
    
    match color:
        case("black"):
            COLOR = "30m"
        case("red"):
            COLOR = "31m"
        case("blue"):
            COLOR = "34m"
        case _:
            COLOR = "37m"
    
    if (bold):
        print(f"{"=> "}\033[1;{COLOR}{str}\033[0m")
    else:
        print(f"{"=> "}\033[0;{COLOR}{str}\033[0m")
        print(icon.rjust(term_width - 10))

def pacman_update():
    subprocess.run(["sudo", "pacman", "-Syu"], )


# ----- #

def run():
    greeting()
    print_pretty("Type your password bellow ")
    #get_password()
    #pacman_update()


# Classic
if __name__ == "__main__" :
    run()