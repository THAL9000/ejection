'''
to more information,send message in creator github account:THAL9000
'''
from colorama import Fore, Back, Style
import time
import sys
from scan import scan
from arpspoof import arpspoof
def main():
    present=["Software to eject a user from the network","version 0.1"]
    file = open("ascii.txt", "r")
    for x in file:
        print(Fore.GREEN + x)
        time.sleep(1)
    for i in range(0,2):
        print(Fore.BLUE+present[i])  
    if len(sys.argv)==1 or sys.argv[1]=="help":
       file_help=open("help.txt","r")
       for y in file_help:
           print(Fore.BLACK+y)
    elif sys.argv[1]=="--scan":
        while True:
         try:   
          time_attack=int(input("Enter the duration of the attack(in minutes):"))
          scanner=scan(time_attack)
          scanner.make()
          break
         except ValueError:
           print(Fore.RED+"Not an integer! Try again.")
           break
    elif sys.argv[1]=="--ip_box" and sys.argv[3]=="--ip_attack" and sys.argv[5]=="--mac_victim" and sys.argv[7]=="--time":
        if sys.argv[2].isnumeric() != True and sys.argv[4].isnumeric() != True and sys.argv[8].isnumeric() != True :
            print(Fore.RED+"the ip and mac address send are not number")
        else:    
            attack=arpspoof(sys.argv[2],sys.argv[4],sys.argv[6],sys.argv[8])
            attack.make()
    else:
        print(Fore.RED+"Your order is not correct,follow this instruction: main.py --help")        
if __name__=="__main__":
    main()        
