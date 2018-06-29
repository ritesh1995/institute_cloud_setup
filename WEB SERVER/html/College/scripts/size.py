#!/usr/bin/python2

print "content-type: text/html"

import commands
import cgi
import os


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

if cgi.FormContent().has_key('size'):
	c=cgi.FormContent()['size'][0]
	d=c.strip(" GB")
	part_Size=int(d)

	if part_Size < 0:
		print	
		print "<script> alert('Please enter correct Size !!!!!'); </script>"
		print "<META HTTP-EQUIV='refresh' content='0; url=../nfs.html'/>" 
	
	else :
		print "set-cookie: size={0}".format(part_Size)
		print 

		dirStatus= commands.getstatusoutput("ls /College/mounted/ | grep '{}'".format(userName))
		if dirStatus[0]==0:
			#print "<script> alert('Please enter correct Size !!!!!'); </script>"
			print "<META HTTP-EQUIV='refresh' content='0; url=extend.py'/>"
		else :
 
			print "<META HTTP-EQUIV='refresh' content='0; url=nfs.py'/>"
	

else :
	print	
	print "<script> alert(' Please enter the size !!'); </script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=../extend1.html'/>" 


