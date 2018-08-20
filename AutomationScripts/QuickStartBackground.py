import os
import sys
from sys import argv

script, cstsip, cstspw, redirun, redirpw, redirip, msfspfn	= argv

#cstsip  = input("Lets get a few details out of the way first. What is the IP of your teamserver?\n> ")
#cstspw	= input("What would you like the password to be for your teamserver?\n> ")
#redirun	= input("What is the username of your Redirector?\n> ")
#redirpw	= input("What is the Redirector password?\n> ")
#redirip	= input("What is the IP of your Redirectior?\n> ")
#msfspfn	= input("What would you like to be the name of your MSF log file?(It will save to /root/Desktop/)\n> ")

def yesorno(answer, run):
        if answer == "Yes": 
                os.system(run)
        if answer == "yes":
                os.system(run)
        if answer == "Y":
                os.system(run)
        if answer == "y":
                os.system(run)
        if answer == "yee yee":
                os.system(run)

#MSF Setup
input("OK! Now lets get Metasploit fired up.")
os.system("xterm -e 'msfconsole'&")
input("""I'm a dummy and can't figure out how to push commands to MSF sooo...
spool /root/Desktop/{}""".format(msfspfn))
input("Now we are gonna cat the log file to verify it's spooling.")
print("cat /root/Desktop/{}".format(msfspfn))
os.system("cat /root/Desktop/{}".format(msfspfn))
input("\nNow we are gonna run a netstat to verify that nothing will conflict with CS.")
print("netstat -natup")
os.system("netstat -natup")
input("\nIf anything is using port 80 or 443 don't forget to kill it.")

#CS Setup
input("We are about to start the CS teamserver.")
aggkill = input("Would you like to renew your CS trial? Yes or No\n> ")
yesorno(aggkill, "rm ~/.aggressor.prop")
os.system("xterm -e 'nano C2.profile; $SHELL'&")
input("Does this C2 profile look good?")
os.system("xterm -e 'cd ..; ./teamserver {} {} AutomationScripts/C2.profile; $SHELL'&".format(cstsip, cstspw))
#os.system("xterm -e 'cd ..; ./teamserver {} {}; $SHELL'&".format(cstsip, cstspw))
#os.system("xterm -e 'cd ..; ./teamserver {} {} /root/Desktop/Malleable-C2-Profiles-master/normal/amazon.profile; $SHELL'&".format(cstsip, cstspw))
input("The teamserver has been started in xterm.")
os.system("xterm -e 'cd ..; ./cobaltstrike; $SHELL'&")
input("The CS client has been started in xterm.")

#Redir Setup
print("""Lets verify that proxychains.conf is properly configured.
socks4 127.0.0.1 6969""")
os.system("xterm -e 'nano /etc/proxychains.conf; $SHELL'&")
input("Continue?")
os.system("xterm -e 'ssh -D 127.0.0.1:6969 {}@{}; $SHELL'&".format(redirun, redirip)) 
input("""
This will have to do until I become less dumb.
password {}
sudo bash
password {}
netstat -natup
socat tcp-listen:80,fork tcp:{}:80 &
socat tcp-listen:443,fork tcp:{}:443 &
netstat -natup
""".format(redirpw, redirpw, cstsip, cstsip))

#Begin Enum
print("Congratulations! Setup is complete.")
enum	= input("Would you like to begin enumeration? Yes or No\n> ")
yesorno(enum,"python3.6 Enum.py")

quit()










#os.system("ssh-keygen")
#os.system("ssh-copy-id cschmid@192.168.32.3")
#os.system("ssh cschmid@192.168.32.3")

#os.system("ssh-keygen")
#os.system("ssh-copy-id {}@{}".format(redirun, redirip))
#os.system("xterm -e 'ssh{}@{}; echo WHEW! That was harder than it had to be! Now lets go ahead and bec$
#input("WHEW! That was harder than it had to be! Now lets go ahead and become root.")
#os.system("sudo bash")
#input("Now a netstat to verify 80 and 443 arent currently being used.")
#os.system("netstat -natup")
#input("Now the 2 socat commands to forward any traffic from 80 or 443 to the kali box.")
#os.system("socat tcp-listen:80,fork tcp:192.168.32.2:80 &")
#os.system("socat tcp-listen:443,fork tcp:192.168.32.2:443 &")
#input("Now another netstat to verify that 80 and 443 are listening")
#input("Congratulations! Setup is complete.")










