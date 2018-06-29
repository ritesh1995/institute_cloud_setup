#!/usr/bin/python2

print "content-type: text/html"
print 

import os
import cgi
import cgitb

cgitb.enable()

serverIP="192.168.43.84"
serverPass="root"

Num= os.environ["HTTP_COOKIE"].split(";")

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
	elif j[0]=='store':
		size=j[1]
	elif j[0]=='cpu':
		cpu=j[1]
	elif j[0]=='os':
		osname=j[1]
	elif j[0]=='memory':
		ram=j[1]
	else:
		pass






if "rhel" in osname:
	os= "Red Hat Enterprise "
	version="7.3"
	ostype=" Basic Server with GUI"
	
elif "centos" in osname:
	os= "CENTOS"
	ostype=" Minimal Interface "
	version="7.1"
elif "ubuntu" in osname:
	os= "Ubuntu "
	ostype=" Grapahical Interface"
	version="14.04"
		
else:
	print "<script> alert(' Please login first !!'); </script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=../login.html'/>"
	

if cpu=='1':
	power="Basic Processing"
elif cpu=='2':
	power="Upgraded Processing "

else:
	print "<script> alert(' Please login first !!'); </script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=../login.html'/>"
	

print """
<html>
<head>
<link rel="stylesheet" href="../css/mit.css">
<link rel="stylesheet" href="../css/was.css">

</head>
<body>
<div id ="particles-js">

        <h1 class="mainh">Review Your Choice</h1>
            
    <dl class="list nigiri">
        <dt>Operating System </dt>
"""
print "<dd><a href='../machine1.html'> "+os+" </a></dd>"
print "<dd><a href='#']>Version : "+version+"</a></dd>"
print "<dd><a href='#'> "+ ostype+"</a></dd>"
print "<dd><a href='#'>Virtualisation Type : KVM</a></dd>"
print"""   
 </dl>

    <dl class="list maki">
	<dt>Package Details  </dt>
"""
print "<dd><a href='../table.html'>vCPU : "+cpu+"</a></dd>"
print "<dd><a href='../table.html'> "+power+"</a></dd>"
print "<dd><a href='../table.html'>Memory : "+ram+" GB </a></dd>"
print """    </dl>

    <dl class="list sashimi">
<dt>Storage Details </dt>
"""
print " <dd><a href='#'>Volume Type : Root  </a></dd>"
print "<dd><a href='#'>Size : 10 GB </a></dd>"
print " <dd><a href='#'>Volume Type : EBS</a></dd>"
print "<dd><a href='../extend2.html'>Size : "+size+" </a></dd>"
      
print """
        
    </dl>
"""
print """
  

<div class="warning">
    <div class="message">
        <h1>CSS 3D Not Detected :(</h1>
        <p>I couldn't detect your browser's CSS 3D capabilities. If I'm wrong, please <a href="https://github.com/soulwire/Makisu/issues" target="_blank">file an issue</a>, otherwise, try a <a href="https://www.google.com/chrome" target="_blank">sexier browser</a></p>
    </div>
</div>
<a href="icreate.py" class="button" >
        <span> Next</span>
    </a>

</div>
<script type="text/javascript" src="../javascript/jquery.min.js"></script>
<script type="text/javascript" src="../javascript/was.js"></script>

<script type="text/javascript" src="../javascript/particles.js"></script>
		<script type="text/javascript" src="../javascript/app.js"></script>


</body>
</html>
"""
