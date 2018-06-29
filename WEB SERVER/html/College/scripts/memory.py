#!/usr/bin/python2


print "content-type: text/html"

import cgi
if not cgi.FormContent().has_key('x'):

	print
	print "<script> alert(' Please login first !!'); </script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=../login.html'/>"
	
else:
	os=cgi.FormContent()['x'][0]

	if os=='1a':

		print "set-cookie: cpu=1 "
		print "set-cookie: memory=0.5"
		print "location: ../extend2.html"	
		print

	elif os=='1b':

		print "set-cookie: cpu=1 "
		print "set-cookie: memory=1"
		print "location: ../extend2.html"	
		print

	elif os=='1c':

		print "set-cookie: cpu=1"
		print "set-cookie: memory=2"
		print "location: ../extend2.html"	
		print

	elif os=='1d':

		print "set-cookie: cpu=1"
		print "set-cookie: memory=4"
		print "location: ../extend2.html"	
		print
	elif os=='1e':

		print "set-cookie: cpu=1"
		print "set-cookie: memory=8"
		print "location: ../extend2.html"	
		print

	elif os=='2a':


		print "set-cookie: cpu=2"
		print "set-cookie: memory=4"
		print "location: ../extend2.html"	
		print

	elif os=='2b':

	
		print "set-cookie: cpu=2"
		print "set-cookie: memory=8"
		print "location: ../extend2.html"	
		print
	
	elif os=='2c':

		print "set-cookie: cpu=2"
		print "set-cookie: memory=16"
		print "location: ../extend2.html"	
		print
	

	
	else:
		print
		print "<script> alert(' Please login first !!'); </script>"
		print "<META HTTP-EQUIV='refresh' content='0; url=../login.html'/>"
	


