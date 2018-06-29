#!/usr/bin/python2

#Step 1:
	#(assume vg already exists )
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

if cgi.FormContent().has_key('os'):
	osname=cgi.FormContent()['os'][0]
	final=uname+osname
	i=[]
	

	y=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} virsh list --all |grep '{2}' ".format(serverPass,serverIP,final))

	z=y[1].split("\n")
	#print z
	i=re.sub(' +',' ',z[-1]).split(" ")
	
	if(i[3]=='running'):
	 stopStatus=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} virsh destroy {2}".format(serverPass,serverIP,i[2]))
	 if stopStatus[0]==0:
		print "<script> alert('Operating System stopped successfully !!!!!'); </script>"
		print "<META HTTP-EQUIV='refresh' content='0; url=iuser.py'/>" 
	
	 else:
		print "<script> alert('Operating system failed to shut down !!!!!'); </script>"
		print "<META HTTP-EQUIV='refresh' content='0; url=iuser.py'/>" 

	else:
	 startStatus=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} virsh create /etc/libvirt/qemu/{2}.xml".format(serverPass,serverIP,i[2]))
	 if startStatus[0]==0:
		print "<script> alert('Operating System started successfully !!!!!'); </script>"
		print "<META HTTP-EQUIV='refresh' content='0; url=iuser.py'/>" 
	 else:
		print "<script> alert('Operating System failed to start !!!!!'); </script>"
		print "<META HTTP-EQUIV='refresh' content='0; url=iuser.py'/>" 


else :
	print "<script> alert(' Please select os !!'); </script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=iuser.py'/>" 





