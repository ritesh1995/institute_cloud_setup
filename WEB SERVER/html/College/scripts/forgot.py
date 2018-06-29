#!/usr/bin/python2

print "content-type: text/html"
print

import cgi
import cgitb
from bcrypt import gensalt,hashpw
import mysql.connector as mariadb

cgitb.enable() 
if cgi.FormContent().has_key('authpass') and cgi.FormContent().has_key('newpass') and cgi.FormContent().has_key('email') and  cgi.FormContent().has_key('confirmpass'):
	
	userName=cgi.FormContent()['email'][0]
	pas=hashpw(cgi.FormContent()['newpass'][0],gensalt(log_rounds=15))
	passwd=hashpw(cgi.FormContent()['confirmpass'][0],pas)

	if pas!=passwd:
		print "<script> alert(' Confirm Password and Password Must be same.. !!'); </script>"
		print "<META HTTP-EQUIV='refresh' content='0; url=../login2.html'/>" 
	else :

		try:
			connection = mariadb.connect(host='192.168.43.36',user='student',password='cL0u)@Dm!n',database='cloud')
			crsr = connection.cursor()

			crsr.execute("SELECT authpass FROM student WHERE email='%s'"% (userName))

			ans=crsr.fetchall()

			if not ans:
		
				print "<script> alert(' Enter correct Email ID !!'); </script>"
				print "<META HTTP-EQUIV='refresh' content='0; url=../login2.html'/>"
	
			else:
				b=ans[0]
				s=b[0].split(",")
				passwd=hashpw(cgi.FormContent()['authpass'][0],s[0])

				if s[0]==passwd:
					#print "use authenticated"
					newp=hashpw(cgi.FormContent()['newpass'][0],gensalt(log_rounds=15))
					crsr.execute("UPDATE student SET pass='%s' WHERE email='%s' "% (newp,userName))
					connection.commit()
					print "<script> alert(' Password Successfully updated !!'); </script>"
					print "<META HTTP-EQUIV='refresh' content='0; url=../login.html'/>"
	

				else:
					print "<script> alert(' Wrong Authorisation Password.. !!'); </script>"
					print "<META HTTP-EQUIV='refresh' content='0; url=../login2.html'/>"
	
		except mariadb.Error as error:
			print "<script>alert(' Database server down...Please try after sometime!!')</script>"
			print "<META HTTP-EQUIV='refresh' content='0; url=/login2.html'/>"


	
else:	

	print "<script> alert(' Please enter the details !!'); </script>"
	print "<META  HTTP-EQUIV='refresh'  content='0; url=../login2.html'/>" 
