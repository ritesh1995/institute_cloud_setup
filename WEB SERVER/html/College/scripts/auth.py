#!/usr/bin/python2

print "content-type: text/html"

import os
import cgi
import commands

user= os.environ["HTTP_COOKIE"].split(",")
userName=user[0].split("=")[1]

userName=userName.split("@")[0]

#Step2:

#Check if the lv is already created on server

serverIP="192.168.43.84"
serverPass="root"

IP="192.168.43.23"
passwd="root"

lvStatus=commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} -l root df -h | grep '{2}' ".format(serverPass,serverIP,userName))

if lvStatus[0]==0:
	dirStatus=commands.getstatusoutput("ls /College/mounted/ | grep '{}'".format(userName))
	if dirStatus[0]==256 :
		commands.getstatusoutput("mkdir -p /College/mounted/{}".format(userName))
	mountStatus=commands.getstatusoutput("sshpass -p {2} ssh -o stricthostkeychecking=no {3} -l root mount {0}:/media/{1} /College/mounted/{1}".format(serverIP,userName,passwd,IP))
	print "location: m.py"
	print
else:
	print 	
	print "<script> alert(' Please configure your storage !!'); </script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=../extend1.html'/>"
	

