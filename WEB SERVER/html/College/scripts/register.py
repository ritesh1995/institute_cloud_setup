#!/usr/bin/python2

print "content-type: text/html"
print 

import cgi
import cgitb
from bcrypt import gensalt,hashpw
import mysql.connector as mariadb

cgitb.enable() 

if cgi.FormContent().has_key('user') and  cgi.FormContent().has_key('email') and  cgi.FormContent().has_key('pass') and  cgi.FormContent().has_key('confirmpass') and cgi.FormContent().has_key('authpass'):
	

	user=cgi.FormContent()['user'][0]
	email=cgi.FormContent()['email'][0]
	pas=hashpw(cgi.FormContent()['pass'][0],gensalt(log_rounds=15))
	authpass=hashpw(cgi.FormContent()['authpass'][0],gensalt(log_rounds=15))
	passwd=hashpw(cgi.FormContent()['confirmpass'][0],pas)

	if pas!=passwd:
		print "<script> alert(' Confirm Password and Password Must be same.. !!'); </script>"
		print "<META HTTP-EQUIV='refresh' content='0; url=../login.html'/>" 
	else :

		try:		
			connection = mariadb.connect(host='192.168.43.36',user='student',password='cL0u)@Dm!n',database='cloud')

			crsr = connection.cursor()

			sql_command = 'INSERT INTO student VALUES("'+email+'","'+ user+'","' +pas+'","'+authpass+'");'
			try:
				crsr.execute(sql_command)
				connection.commit()	
				print "<script> alert(' User Successfully Registered !'); </script>"
				print "<META HTTP-EQUIV='refresh' content='0; url=/login.html'/>"
	
			except mariadb.Error as error:
				print "<script>alert(' Email ID already exists, try with a different one')</script>"
				print "<META HTTP-EQUIV='refresh' content='0; url=/login.html'/>"


		except mariadb.Error as error:
				print "<script>alert(' Database server down..Try again after sometime!!!!')</script>"
				print "<META HTTP-EQUIV='refresh' content='0; url=/login.html'/>"

else:
	print "<script> alert(' Please enter the details !!'); </script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=../login.html'/>" 


