#!/usr/bin/python2


print "content-type: text/html"

import cgi

if cgi.FormContent().has_key('x'):
	os=cgi.FormContent()['x'][0]
	#print os

	if os=='1':
		print "set-cookie: os=rhel73gui"
		print "location: ../table.html"	
		print
	
	elif os=='2':
		print "set-cookie: os=ubuntu"
		print "location: ../table.html"	
		print
	

	elif os=='3':
		print "set-cookie: os=centos7cli"
		print "location: ../table.html"	
		print
	
	else:
		print
		print "<script> alert(' Please click on right choice !!'); </script>"
		print "<META HTTP-EQUIV='refresh' content='0; url=../login.html'/>"
	
else:
	print
	print "<script> alert(' Please login first !!'); </script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=../login.html'/>"
	

