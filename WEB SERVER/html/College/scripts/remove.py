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

fName=cgi.FormContent()['x'][0]

removeStatus=commands.getstatusoutput("sudo rm -f /College/mounted/{0}/{1}".format(userName,fName))



if removeStatus[0]!=0:
	print "<script> alert(' File could not be removed please try again '); </script>"
else:
	print "<script> alert(' Deletion completed successful'); </script>"
	
print "<META HTTP-EQUIV='refresh' content='0; url=m.py'/>"

