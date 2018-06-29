#!/usr/bin/python2

import commands
import cgi
import os


print "content-type: text/html"
print



Num =  os.environ["HTTP_COOKIE"].split(";")
#print Num
for i in Num:
	#k= i.split(',')	
	#j=k[0].split("=")
	k= i.split(',')	
	l=k[0].strip()
	j=l.split("=")		
	#j[0].strip(' ')
	if j[0]=='userName':
		userName= j[1]
		
	elif j[0]=='size':
		partSize=j[1]
		
	else:
		pass


userName=userName.split("@")[0]

serverIP="192.168.43.84"
serverPass="root"

commands.getstatusoutput("sshpass -p {2} ssh -o stricthostkeychecking=no {3} -l root lvextend --size +{0}G /dev/my/{1} ".format(partSize,userName,serverPass,serverIP))

formatStatus=commands.getstatusoutput("sshpass -p {1} ssh -o stricthostkeychecking=no {2} -l root resize2fs /dev/my/{0} ".format(userName,serverPass,serverIP))


if formatStatus[0]==0:
	print "<script> alert('Successfully allotted the requested size !!!!!'); </script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=m.py'/>" 

elif formatStatus[0]== 1280:
	print "<script> alert(' Storage Insufficient ...Kindly contact Admin to increase hardware storage !!'); </script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=../extend1.html'/>"
	




