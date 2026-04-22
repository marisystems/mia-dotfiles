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
    match color:
        case("black"):
            COLOR = "\033[0;31m"
        case("red"):
            COLOR = "\033[0;32m"
        case("blue"):
            COLOR = "\033[31m"
        case _:
            COLOR = "\033[31m"
            
    print(f"{"=> "}{COLOR}{str}\033[0m")

def pacman_update():
    subprocess.run(["sudo", "pacman", "-Syu"], )


# ----- #

def run():
    greeting()
    #get_password()
    #pacman_update()
    print_pretty("hi", "black")

# Classic
if __name__ == "__main__" :
    run()