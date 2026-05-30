#!/bin/bash
# Script to get the number of updates in the AUR
# (Be careful doing too many requests with this)
paru -Qu | wc -l
