#!/usr/bin/python2

import cgi
import os

serverIP="192.168.43.84"
serverPass="root"

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

userName=userName.split("@")[0]

if cgi.FormContent().has_key('file'):
	FileName=cgi.FormContent()['file'][0]


	print 'content-type: application/octet-stream;'
	print 'Content-Disposition: attachment; filename = "{0}"'.format(FileName)
	print
	# Actual File Content will go here.

	fo = open("../mounted/{}/{}".format(userName,FileName), "rb")

	st = fo.read()
	print st

	# Close opend file
	fo.close()

else:
	print "content-type: text/html"
	print
	print "<script> alert(' Please select the file first !!'); </script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=m.py'/>" 

