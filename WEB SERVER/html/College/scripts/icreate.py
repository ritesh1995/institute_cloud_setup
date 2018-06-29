#!/usr/bin/python2

print "content-type: text/html"
print 

import os
import cgi
import cgitb
import commands
import fileinput

cgitb.enable()

serverIP="192.168.43.84"
serverPass="root"

Num= os.environ["HTTP_COOKIE"].split(";")

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
	elif j[0]=='store':
		size=j[1]
	elif j[0]=='cpu':
		cpu=j[1]
	elif j[0]=='os':
		osname=j[1]
	elif j[0]=='memory':
		ram=j[1]
	else:
		pass

userName=userName.split("@")[0]
d=size.strip(" GB")
hdd=int(d)

final=userName+osname
ram=float(ram)*1048576
ram=int(ram)

"""
print osname
print hdd
print final
print userName
print ram
"""

commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} virt-clone --original {2} --name {3} --auto-clone".format(serverPass,serverIP,osname,final))


commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} qemu-img create -f raw /lvmounts/{2}hdd.img {3}G".format(serverPass,serverIP,final,hdd))

commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} virsh attach-disk {2} --source /lvmounts/{2}hdd.img  --target vdb --persistent".format(serverPass,serverIP,final))

commands.getstatusoutput("sshpass -p {0} scp -o stricthostkeychecking=no root@{1}:/etc/libvirt/qemu/{2}.xml  /temp/".format(serverPass,serverIP,final))
				
commands.getstatusoutput("sudo chown apache /temp/{}.xml".format(final))
 
for line in fileinput.input('/temp/{}.xml'.format(final),inplace=True):
 print line.rstrip().replace("<memory unit='KiB'>1048576</memory>","<memory unit='KiB'>{}</memory>".format(ram)),

for line in fileinput.input('/temp/{}.xml'.format(final),inplace=True): 
 print line.rstrip().replace("<currentMemory unit='KiB'>1048576</currentMemory>","  <currentMemory unit='KiB'>{}</currentMemory>".format(ram)),

for line in fileinput.input('/temp/{}.xml'.format(final),inplace=True): 
 print line.rstrip().replace("<vcpu placement='static'>1</vcpu>","<vcpu placement='static'>{}</vcpu>".format(cpu)),


commands.getstatusoutput("sshpass -p {0} scp -o stricthostkeychecking=no /temp/{2}.xml root@{1}:/etc/libvirt/qemu/{2}.xml ".format(serverPass,serverIP,final))

createStatus=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} virsh create /etc/libvirt/qemu/{2}.xml".format(serverPass,serverIP,final))

if createStatus[0]==0:
	print "<META HTTP-EQUIV='refresh' content='0; url=iuser.py'/>"
else:
	print "<script> alert('Operating system failed to install !!!!!'); </script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=../twooptions.html'/>"


