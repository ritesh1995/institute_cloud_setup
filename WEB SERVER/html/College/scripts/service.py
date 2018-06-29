#!/usr/bin/python2


print "content-type: text/html"
print

import commands
import cgi
import os

serverIP="192.168.43.84"
serverPass="root"

user= os.environ["HTTP_COOKIE"].split(",")
userName=user[0].split("=")[1]
userName=userName.split("@")[0]

x=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1}  ls /lvmounts/ | grep '{2}' ".format(serverPass,serverIP,userName))

if(x[0]==0):
	print "<META HTTP-EQUIV='refresh' content='0; url=iuser.py'/>"
	
else:
	print "<META HTTP-EQUIV='refresh' content='0; url=../machine1.html'/>"
	
