#!/usr/bin/python2

import commands
import cgi
import os
import re


print "content-type: text/html"
print

serverIP="192.168.43.84"
serverPass="root"

print commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} rm -f /lvmounts/{2}".format(serverPass,serverIP,"riteshrhel73gui.img"))
