#!/usr/bin/python2

print "content-type: text/html"
print 

import commands
import cgi
import re
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


uname=userName.split("@")[0]

print """
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="../css/mit.css">
<link rel="stylesheet" href="../css/mit2i.css">
<script>

function remove(file)
{
      
	document.location='iassdelete.py?x='+file 
	alert(file + " Operating System Termination in progress !!!")	
		
}

</script>

</head>




<body>



<div id ="particles-js">
<h1 class="mainh">Your Operating System </h1>
<div class="my">
<div class="file-upload2">
   <a href='../machine1.html'> <label  class="file-upload__label">Create Instance</label>
    </a>
</div>
<div class="file-upload2">
    <a href='../twooptions.html'> <label  class="file-upload__label">Change Service</label>
    </a>
</div>


</div>
"""
y=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1}  virsh list --all |grep '{2}' ".format(serverPass,serverIP,uname))
#print y
z=y[1].split("\n")
i=[]
del z[0]
del z[0]

for j in z:
  i.append(re.sub(' +',' ',j).split(" "))


for k in i:
  print """
  <section class="card">
    

        <div class="card_inner">
   
             <div class="card_inner__circle">
   <form action="iasstoggle.py" method="POST" >                                
     <label class="labelc"for="checkbox1" id="redgf"></label>
  """
  
  m= k[2].replace(uname,"",1)
  print "<button class='btnn' name='os' value="+m+"> <img src='../image/Off.png' /> </button>"
  print """
	</form>
 </div>
   


             <div class="card_inner__header">
                    <img src="../image/blue.jpg">
                </div>
     


           <div class="card_inner__content">
        
 
  """
  print "<div class='title'>OS : "+k[2].replace(uname,"",1)+"</div>"
  print "<br/> <div class='price'>Status: "+k[3]+"</div>"
  if(k[3]=="running"):
   z=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} virsh vncdisplay {2}".format(serverPass,serverIP,k[2]))
   
   #print k[-2]
   if z[0]==0:
	   p=z[1].split("\n")
	   port=int(p[-2].strip(':'))
	   port=port+5900
	   #print port
	    #print("You may connect to IP: {} and port no. :{}".format(serverIP,5900+port))               
	   print """
	   <div class="text">You may connect to given IP and port using application given on home page : <br/>
	   """
	   print "IP : {}".format(serverIP)
	   print "<br/>Port : {}".format(port)
	   print "<br/>Please click on Toggle button to shut down Operating System</div>"
   else:
	   print "<script> alert(' Please register yourself first !!'); </script>"
	   print "<META HTTP-EQUIV='refresh' content='0; url=../login.html'/>"

  else:
   print """<div class="text"> IP : Unavailable <br/> Port : Unavailable <br/> Please click on Toggle button to start your Operating System <br/> The OS can be remotely accessed from only one device only!!</div>	"""
  print """  
	
              </div>
          


      <div class="card_inner__cta">
                    
  """
  print "<button onclick=\"remove('"+k[2].replace(uname,"",1)+"')\"> "
  print """
	
       <span>
            <a >TERMINATE</a>
          </span>
                    </button>

                </div>
            </div>
        </section>
  """
print """

</div>


 
<script type="text/javascript" src="../javascript/jquery.min.js"></script>

		<script type="text/javascript" src="../javascript/particles.js"></script>
		<script type="text/javascript" src="../javascript/app.js"></script>



</body>
</html>
"""
