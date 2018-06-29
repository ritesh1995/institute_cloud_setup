#!/usr/bin/python2


print "content-type: text/html"
print

import commands
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

print """
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="../css/mit.css">
<link rel="stylesheet" href="../css/mit2.css">
<script>

function remove(file)
{
      
	document.location='remove.py?x='+file 
	alert(file + " Deletion in progress !!!")	
		
}

</script>

</head>
<body>
<div id ="particles-js">
<h1 class="mainh"> File Management</h1>
<div class="my">
	<div class="file-upload1">
	<form enctype="multipart/form-data" action="upload.py" method="POST">
    	<label for="upload" class="file-upload__label"> Upload File</label>
    	<input id="upload" class="file-upload__input" onchange='form.submit()' type="file" name="file"/>
	</form>
	</div>
	<div class="file-upload2">
    		<a href='../twooptions.html'><label  class="file-upload__label">Change Service</label>
    		</a>
	</div>
	<div class="file-upload2">
    		<a href='../extend1.html'> <label  class="file-upload__label">Extend</label>
    		</a>
	</div>
</div>
"""

z=0

for i in commands.getoutput(" ls ../mounted/{0} -l ".format(userName)).split('\n'):
	if z<1:
		
		pass
 	else:
		j=i.split()
		#print j
		size=int(j[-5])
		if size>1073741000:
			size=float(size/1073741824.0)
			size=("%.2f" %size)
			size=size+" GB"
		
		elif size>1048576:
			size=float(size/1048576.0)
			size=("%.2f" %size)
			size=size+" MB"
			
		elif size>1000:
			size=float(size/1024.0)
			size=("%.2f" %size)
			size=size+" KB"
		else:
			size=str(size)+" bytes"
			
		print """
			<section class="card">
	    

		<div class="card_inner">

	   
		     <div class="card_inner__circle">
		            <img src="../image/icon.png">
		        </div>
	   


		     <div class="card_inner__header">
		            <img src="../image/blue.jpg">
		        </div>
	     


		   <div class="card_inner__content">
		
	 
		   <div class="title">
		"""
		

		print "	<a href=download.py?file={}>".format(j[-1])+j[-1]+"</a> </div>"
		print "<br/> <div class='price'>Size : {}".format(size)
		print "</div> <div class='text'> <br/>Date : "+j[-3]+" "+j[-4]+ "<br/>Last Modified Time : "+j[-2]
		print """<br/> Owner : Apache <br/> Click on File name to Download the file..<br/>
			</div>
		         </div>
		  
		      <div class="card_inner__cta">
		            

		"""
		
		print "<button onclick=\"remove('"+j[-1] +"')\"> "
		print """
		   <span>
		    <a>REMOVE</a>
		  </span>
		            </button>

		        </div>
		    </div>
		</section>

		"""
	
	z=z+1

print """  
</div>


		<script type="text/javascript" src="../javascript/jquery.min.js"></script>
		<script type="text/javascript" src="../javascript/particles.js"></script>
		<script type="text/javascript" src="../javascript/app.js"></script>



</body>
</html>

"""
