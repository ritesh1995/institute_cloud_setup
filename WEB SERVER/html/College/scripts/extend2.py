#!/usr/bin/python2


print "content-type: text/html"

import cgi

if not cgi.FormContent().has_key('store'):
	print
	print "<script> alert(' Please login first !!'); </script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=../login.html'/>"
	
else:
	os=cgi.FormContent()['store'][0]
	print "set-cookie:  store={}".format(os)
	print "location: review.py"	
	print
