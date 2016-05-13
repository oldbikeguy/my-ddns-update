# my-ddns-update
#
# Copied and modified from 
# https://github.com/istvan-antal/changeip-updater
#
# Changes I made:
#
# Removed the time functions - cron log and messages 
#    will take care of what I need
# Removed the function to trap a no IP file scenario - 
#    that shouldn't happen as I have seeded my files already
# Removed "import" lines that weren't needed
#
# Tried to make some changes for easier following - variable 
#    names, etc.
#
# I stripped this down and consolidated it some for use on a 
#    Raspberry Pi with a barebones OS and limited resources.
#
# It could do with some error trapping which I will play with 
#    next.
#
