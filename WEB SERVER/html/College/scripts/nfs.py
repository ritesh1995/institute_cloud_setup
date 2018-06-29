#!/usr/bin/python2

#Step 1:
	#(assume vg already exists )
import commands
import cgi
import os

print "content-type: text/html"
print

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
		
	elif j[0]=='size':
		part_Size=j[1]
		#print part_Size
	else:
		pass

#user= os.environ["HTTP_COOKIE"].split(",")
#userName=user[0].split("=")[1]

user_name=userName.split("@")[0]

serverIP="192.168.43.84"
serverPass="root"

clientIP="192.168.43.0/255.255.255.0"
IP="192.168.43.23"
passd="root"

#print user_name
#print part_Size
#create temp directory

c=commands.getstatusoutput("sudo mkdir /temp")


#check if vg is created or not..if not created exit
vgStatus=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} vgdisplay my".format(serverPass,serverIP))

 #myvg naam ka vg bna hona chahiye jha nfs server create krna hai


if vgStatus[0]!=0:
	print "<script> alert('Volume Grouop not created yet !!!!!'); </script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=../twooptions.html'/>" 
	

else:
	
	lvStatus=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} lvcreate --size {3}G  --name {2} my ".format(serverPass,serverIP,user_name,part_Size))
	#print lvStatus
	if lvStatus[0]== 1280:
		print "<script> alert(' Storage Insufficient ...Kindly contact Admin to increase storage !!'); </script>"
		print "<META HTTP-EQUIV='refresh' content='0; url=../twooptions.html'/>"
	

	#Step 2:  
	#format using ext4 
	elif lvStatus[0]==0:
		formatStatus=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} mkfs.ext4  /dev/my/{2} ".format(serverPass,serverIP,user_name))

		if formatStatus[0]!=0:
			print "<script> alert(' Allocated storage format failed!!...'); </script>"
			print "<META HTTP-EQUIV='refresh' content='0; url=../twooptions.html'/>"
	

		#Step 3:
		#    mount the folder /share

		#mkdir /share
		else:
			dirCreation=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} mkdir -p /media/{2} ".format(serverPass,serverIP,user_name))

			if dirCreation[0]!=0:
				print "<script> alert('Mount directory failed to be created'); </script>"
				print "<META HTTP-EQUIV='refresh' content='0; url=../twooptions.html'/>"
		
				#print " Directory creation failed "+dirCreation[1]
	

			mountStatus=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} mount /dev/my/{2}  /media/{2}".format(serverPass,serverIP,user_name))

			if mountStatus[0]!=0:
				print "<script> alert(' Allocated storage failed to mount'); </script>"
				print "<META HTTP-EQUIV='refresh' content='0; url=../twooptions.html'/>"
	
				#print "mount failed"+mountStatus[1]

			#fstab file automatically mount 
			else:			
				fstabString="/dev/my/{0}   /media/{0}  ext4  defaults  1  2".format(user_name)

			
				commands.getstatusoutput("sshpass -p {0} scp -o stricthostkeychecking=no root@{1}:/etc/fstab  /temp/".format(serverPass,serverIP))
				
				commands.getstatusoutput("sudo chown apache /temp/fstab")

				#dont use 'w' mode over here
				fstabfh=open('/temp/fstab', 'a')

				fstabfh.write(fstabString + "\n")
				fstabfh.close()


				commands.getstatusoutput("sshpass -p {0} scp -o stricthostkeychecking=no /temp/fstab root@{1}:/etc/fstab ".format(serverPass,serverIP))

				# -p to automatically create share folder and ritesh-lv1 

				fstabStatus=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} mount -a".format(serverPass,serverIP))

				if fstabStatus[0]!=0:
					print "<script> alert(' Permanent mount failed to setup'); </script>"
					print "<META HTTP-EQUIV='refresh' content='0; url=../twooptions.html'/>"
					#print "PLease go and check manually fstab file...There is some error!!!!!!!!! "
				else:
					shareLocation=("/media/{0}  {1}(rw,sync,no_root_squash) ".format(user_name,clientIP))

					#file system se download krke hum file handling krenge aur waps upload kr denge

					nfsFileStatus=commands.getstatusoutput(" sshpass -p {0} scp -o stricthostkeychecking=no root@{1}:/etc/exports /temp/ ".format(serverPass,serverIP))


					nfsfh=open('/temp/exports','a')
					nfsfh.write(shareLocation + "\n")
					nfsfh.close()

					#uploading the file to server after editing it
					nfsFileUploadStatus=commands.getstatusoutput(" sshpass -p {0} scp -o stricthostkeychecking=no /temp/exports root@{1}:/etc/exports ".format(serverPass,serverIP))

					commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} setenforce 0".format(serverPass,serverIP))

					commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} iptables -F".format(serverPass,serverIP))

					serviceStatus=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} systemctl restart nfs".format(serverPass,serverIP))

					if serviceStatus[0]!=0:
						print "<script> alert(' Storage service failed to restart'); </script>"
						print "<META HTTP-EQUIV='refresh' content='0; url=../twooptions.html'/>"
	
						#print serviceStatus[1]
	
					else:
					#Step 4:
						exportStatus=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no {1} -l root exportfs -v".format(serverPass,serverIP))
						if exportStatus[0]==0:
							commands.getstatusoutput("sudo mkdir -p /College/mounted/{0} ".format(user_name))

							mountStatus=commands.getstatusoutput("sshpass -p {2} ssh -o stricthostkeychecking=no {3} -l root mount {0}:/media/{1} /College/mounted/{1}".format(serverIP,user_name,passd,IP))

							if mountStatus[0]!=0:
								print "<script> alert(' Mount Error..Storage not ready!!'); </script>"
								print "<META HTTP-EQUIV='refresh' content='0; url=../twooptions.html'/>"
							else:
								print "<script> alert(' Storage configured successfully !!!'); </script>"
								print "<META HTTP-EQUIV='refresh' content='0; url=m.py'/>"
						else:
							print "<script> alert(' Storage not ready to be exported'); </script>"
							print "<META HTTP-EQUIV='refresh' content='0; url=../twooptions.html'/>"
	
