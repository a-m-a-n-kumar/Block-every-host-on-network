# Block-every-host-on-network

This python program blocks every host on the network to gain access to the internet except the devices you want to exclude including yours!

/////  REQUIREMENTS /////

-> Make sure that Bettercap is installed in your system. Link to installation guide:  https://www.bettercap.org/installation/

-> Make sure that you have a python compiler installed in your system

-> Make sure that subprocess module is installed in your system.


///////// HOW TO RUN PROGRAM  ////////

-> First find out what your internal/local ipv4 address is
 
-> When you run the program on your compiler, it first ask you to input first three octects of your local ip address.
    ---For ex, if your local ip address is 192.168.0.10, then you have to input 192.168.0
    
-> Then it asks you to enter the number of hosts you want to 'exclude' form blocking their internet
    ---For ex, if you want you and your friend to exclude from blocking, input 2
    
-> Then it asks you to enter the local ip address of the hosts you want to exclude from blocking. Make sure that you enter the full local ipv4 address of devices.    

-> After that, the python program will create a file named "block.cap" in the same directory/folder in which you are running your program. This file contains all the commands 
   bundled together to run bettercap.
   
-> The bettercap will execute the commands written in this file and block every other hosts on your network except yours and your friend.


ENJOY
