#!/usr/bin/env python
#
# Borrowed and modified from https://github.com/istvan-antal/changeip-updater
#
# Changes:
#
# I removed the time functions - cron log will take care of that
# I removed the function to trap a no IP file scenario - that shouldn't happen
# I removed "import" lines that weren't needed
# Tried to make some changes for easier following - variable names, etc.
#
# I stripped this down and consolidated it some for use on a Raspberry Pi.
#
# It could do with some error trapping which I will play with next.
#
# import the needed things

import os
import socket
from httplib import HTTPSConnection
from httplib import HTTPConnection
from base64 import b64encode

def net_test(myUrl):
	try:
		socket.getaddrinfo(myUrl, 80)
		return True
	except socket.error:
		return False

# set login info
username = "---------"
password = "---------"
set = "1"

# store my ip
IP_FILE = "/home/pi/current_ip"
if os.path.isfile(IP_FILE):
	f = open(IP_FILE, 'r')
	lastip = f.readline()
	f.close()
	lastip_set = True
else:
	# record the ip if the file doesn't exist
	f = open(IP_FILE, 'w+')
	lastip_set = False


# test internet connectivity
if net_test("ip.changeip.com"):
	# what is my external IP now - 
	# use the ip.changeip.com page 
	# (like what's my ip but much cleaner)
	myUrl = "ip.changeip.com"
	site = HTTPConnection(myUrl)
	site.request("GET", "/")
	result = site.getresponse()
	data = result.read()
	currentip = data.split("\n")[0]

	# record ip if no file found
	if lastip_set == False:
		f.write(current_ip)
		f.close()

	# check and update if needed
	if currentip != lastip:
    		print "Last ip: " + lastip
    		print "New ip: " + currentip

    		# update the record at changeip.com
    		upyours = HTTPSConnection("nic.changeip.com")
    		userAndPass = b64encode(username + ":" + password)
    		headers = { 'Authorization': 'Basic %s' %  userAndPass, "User-Agent": "rinker.sh wget 1.0" }
    		upyours.request("POST", "/nic/update?cmd=update&set=" + set, currentip ,headers)
    		result = upyours.getresponse()
    		data = result.read()
    		print "Response: " + data

    		# update the current_ip file
    		f = open(IP_FILE, "w+")
    		f.write(current_ip)
    		f.close()
	else:
    		print "No change"
else:
	print "The internet appears to be down.  Will try again later."
