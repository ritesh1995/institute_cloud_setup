#!/usr/bin/python2

print "content-type: text/html"


import os
import cgi
import cgitb
from bcrypt import gensalt,hashpw
import mysql.connector as mariadb

cgitb.enable() 
if cgi.FormContent().has_key('username') and cgi.FormContent().has_key('password'):
	
	userName=cgi.FormContent()['username'][0]
	if "@gmail.com" in userName:

		try:
			connection = mariadb.connect(host='192.168.43.36',user='student',password='cL0u)@Dm!n',database='cloud')
			crsr = connection.cursor()

			crsr.execute("SELECT pass FROM student WHERE email='%s'"% (userName))

			ans=crsr.fetchall()

			if not ans:
				print	
				print "<script> alert(' Please register yourself first !!'); </script>"
				print "<META HTTP-EQUIV='refresh' content='0; url=../login.html'/>"
	
			else:
				b=ans[0]
				s=b[0].split(",")
				passwd=hashpw(cgi.FormContent()['password'][0],s[0])

				if s[0]==passwd :
					#print "use authenticated"
	
					print "set-cookie: userName={0}".format(userName)
					print
					print "<script> alert(' Welcome back !!'); </script>"
					print "<META HTTP-EQUIV='refresh' content='0; url=../twooptions.html'/>"
	

				else :
					print
					print "<script>alert(' Wrong Password..Don't worry ..Click on Forgot Pass to change your password!!')</script>"
					print "<META HTTP-EQUIV='refresh' content='0; url=/login.html'/>"
	
					
		except mariadb.Error as error:
			print
			print "<script>alert(' Database server down...Please try after sometime!!')</script>"
			print "<META HTTP-EQUIV='refresh' content='0; url=/login.html'/>"
	
	else:
		print
		print "<script>alert(' Please enter valid Email Id (i.e, Gmail Id) only!!')</script>"
		print "<META HTTP-EQUIV='refresh' content='0; url=/login.html'/>"
	

else:	
	print
	print "<script> alert(' Please enter the details !!'); </script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=../login.html'/>" 
