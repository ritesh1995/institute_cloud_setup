#!/usr/bin/python2

import cgi
import cgitb
import commands
import os

cgitb.enable()

print "content-type: text/html"
print

serverIP="192.168.43.84"
serverPass="root"

user= os.environ["HTTP_COOKIE"].split(",")
size=os.environ["CONTENT_LENGTH"]

userName=user[0].split("=")[1]
userName=userName.split("@")[0]
size=float(size)

form = cgi.FieldStorage()
form_file=form['file']

if not form.has_key('file'):
	print "<script> alert(' Please select the file !!'); </script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=m.py'/>"
	


elif not form_file.file:
	print "<script> alert(' Please select the file !!'); </script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=m.py'/>"
	
	
elif not form_file.filename:
	print "<script> alert(' Please select the file !!'); </script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=m.py'/>"

else:
	size=size/(1024*1024*1024)
	j=commands.getoutput(" df -h | grep '{0}' ".format(userName)).split()
	if "M" in j[3]:
		k=j[3].strip("M")
	else:
		k=j[3].strip("G")
			
	k=float(k)
	
	if size > k :
		print "<script> alert(' Storage insufficient !!! Please extend your storage!!'); </script>"
		print "<META HTTP-EQUIV='refresh' content='0; url=m.py'/>"


	else:
		fileCount=commands.getstatusoutput("ls /College/mounted/{0}/ | grep '{1}' | wc -l".format(userName,form_file.filename))

		if fileCount[1]=='0':
			uploadStatus=commands.getstatusoutput("sudo touch /College/mounted/{0}/{1}".format(userName,form_file.filename))
			if uploadStatus[0]!=0:
				print "<script> alert(' '+uploadStatus[1]+'!!'); </script>"
				print "<META HTTP-EQUIV='refresh' content='0; url=m.py'/>"
			
			else:
				commands.getstatusoutput("sudo chown apache  /College/mounted/{0}/{1}".format(userName,form_file.filename))

				fh=open('/College/mounted/{0}/{1}'.format(userName,form_file.filename),'w')
				fh.write(form.getvalue('file'))
				fh.close()

				#print "<h1>Completed file upload</h1>"

				#print " <a href= '../upload.html'> Back to uplaod file </a>"
				print "<script> alert('File Successfully Uploaded '); </script>"
				print "<META HTTP-EQUIV='refresh' content='0; url=m.py'/>"
	
	

		else:
			count=int(fileCount[1])+1
			count=str(count)
			fileName=form_file.filename.split(".")
			uploadStatus=commands.getstatusoutput("sudo touch /College/mounted/{0}/{1}{2}.{3}".format(userName,filename[0],count,filename[1]))
			if uploadStatus[0]!=0:
				print "<script> alert(' '+uploadStatus[1]+'!!'); </script>"
				print "<META HTTP-EQUIV='refresh' content='0; url=m.py'/>"
	
			else:
				commands.getstatusoutput("sudo chown apache  /College/mounted/{0}/{1}".format(userName,form_file.filename))

				fh=open('/College/mounted/{0}/{1}'.format(userName,form_file.filename),'w')
				fh.write(form.getvalue('file'))
				fh.close()

				#print "<h1>Completed file upload</h1>"

				#print " <a href= '../upload.html'> Back to uplaod file </a>"
				print "<script> alert('File Successfully Uploaded '); </script>"
				print "<META HTTP-EQUIV='refresh' content='0; url=m.py'/>"
	
