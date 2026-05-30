#!/bin/bash
# Trying to understand how I will do this with wayland
# One way is to use hyprctl, lets try that first :)

# Define array for all the possible workspaces, I'll assume 10
# because I think hyprctl has no way of querying all the desktops defined in the
# configuration
workspaces_array=(1 2 3 4 5 6 7 8 9 10)

# Get the workspaces being used by using multiline grep by pcregrep and then
# getting only the numbers by grep on top of it
used_workspaces=$(hyprctl workspaces | pcregrep -Mo '[I][D] \d+' | grep -o '[0-9]\+')
used_workspaces=$used_workspaces | sort

echo $used_workspaces
echo ${workspaces_array[@]}

# Get workspaces ids

# See if they are occupied
