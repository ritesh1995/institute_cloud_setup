#!/usr/bin/python2

import commands
import cgi
import os
import re


print "content-type: text/html"
print

Num =  os.environ["HTTP_COOKIE"].split(";")
#print Num

for i in Num:
	#j= i.split('=')
	k= i.split(',')	
	l=k[0].strip()
	j=l.split("=")
	#j=l.strip()
	#print j
	if j[0]=='userName':
		userName= j[1]
		#print userName
	else:
		pass


uname=userName.split("@")[0]

serverIP="192.168.43.84"
serverPass="root"

if cgi.FormContent().has_key('x'):
	osname=cgi.FormContent()['x'][0]
	final=uname+osname
	#print final

	commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} virsh destroy {2}".format(serverPass,serverIP,final))
	commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} virsh undefine {2}".format(serverPass,serverIP,final))

	x=commands.getoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} ls /lvmounts/ |grep {2}".format(serverPass,serverIP,final))
	x=x.split("\n")
	#print x
	for i in x:
	 commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} rm -f /lvmounts/{2}".format(serverPass,serverIP,i))

	print "<script> alert('Operating System terminated !!!!!'); </script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=iuser.py'/>" 
else :
	print "<script> alert(' Please select os !!'); </script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=iuser.py'/>" 


#os.system("rm -f $(ls /lvmounts '{}')").format(final) does not work
#print x
#z=y[1].split("\n")
#print y
#i=re.sub(' +',' ',y[1]).split(" ")
#print i[2]
#if(i[3]=='running'):
 
#else:
# commands.getstatusoutput("virsh create /etc/libvirt/qemu/{}.xml".format(i[2]))

