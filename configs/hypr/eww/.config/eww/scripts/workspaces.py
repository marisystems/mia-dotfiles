import subprocess
import re

# Define 10 empty workspaces
workspaces = {
        "w1": False,
        "w2": False,
        "w3": False,
        "w4": False,
        "w5": False,
        "w6": False,
        "w7": False,
        "w8": False,
        "w9": False,
        "w10": False,
        }

#for key in workspaces:
    #print(workspaces[key])

#Get used workspaces
stdout = subprocess.run(['hyprctl', 'workspaces'], capture_output=True, text=True).stdout


names = ['Moroe', 'Amogus', 'Robert', 'Kyle']

regex = '\w'
for name in names:
    result = re.search(regex, name)
    if result:
        print(result)
        print(result.group())

