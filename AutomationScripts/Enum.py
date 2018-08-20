import os
import sys


ccr	= input("""First let's do a netdiscover.\nWhat is the class C ip range you would like to enumerate?\n> """)
os.system("xterm -e 'proxychains netdiscover -r {} -P; $SHELL'&".format(ccr))

psr	= input("Now lets enumerate ports 135,139,445 where the machines are.\nInput an ip range EX:192.168.32.25-35\n> ")
psn	= input("What would you like to name the scan? It will be saved to ~/Desktop/\n> ")
os.system("xterm -e 'proxychains nmap -sT -Pn -p 445,139,135 {} -oG ~/Desktop/{}; $Shell'&".format(psr, psn)) 
#service discovery- 		Proxychains nmap -sT -Pn -n -v -p- -A 192.168.32.6
#service version discovery- 	Proxychains nmap -sV -sC -n -v -p- -A 192.168.32.6 (very slow scan)
q1	= input("Would you like to cat the results? They are also saved to the file on your desktop. Yes or No\n> ")
if q1 == "Yes" or "yes" or "Y" or "y" or "Yee Yee":
	os.system("xterm -e 'cat /root/Desktop/{}; $SHELL'&".format(psn))

idip	= input("What Ip would you like to scan more in depth?\n> ")
idn	= input("What would you like to name the scan? It will be saved to ~/Desktop/\n> ")
os.system("xterm -e 'proxychains nmap -sT -Pn -n -v -A {} -oG  ~/Desktop/{}; $Shell'&".format(idip, idn))

q2	= input("Would you like to cat the results? They are also saved to the file on your desktop. Yes or No\n> ")
if q2 == "Yes" or "yes" or "Y" or "y" or "Yee Yee":
        os.system("xterm -e 'cat /root/Desktop/{}; $SHELL'&".format(idn))

