import os
import sys
import getpass
#from sys import argv

def yesorno(answer, run):
        if answer == "Yes":
                os.system(run)
        if answer == "yes":
                os.system(run)
        if answer == "Y":
                os.system(run)
        if answer == "y":
                os.system(run)
        if answer == "YEE YEE":
                os.system(run)

def yesornoQ(answer, run):
        if answer == "Yes":
                os.system(run); quit()
        if answer == "yes":
                os.system(run); quit()
        if answer == "Y":
                os.system(run); quit()
        if answer == "y":
                os.system(run); quit()
        if answer == "YEE YEE":
                os.system(run); quit()


def csc2(c21a):
        if c21a == "1":
                os.system("xterm -e 'cd ..; ./teamserver {} {}; $SHELL'&".format(cstsip, cstspw))
                print("./teamserver {} {}".format(cstsip, cstspw))
        elif c21a == "2":
                os.system("xterm -e 'cd ..; ./teamserver {} {} AutomationScripts/C2.profile; $SHELL'&".format(cstsip, cstspw))
                print("./teamserver {} {} AutomationScripts/C2.profile".format(cstsip, cstspw))
        elif c21a == "3":
                c2path  = input("What is the path to the c2 profile you would like to use?\n> ")
                if os.path.exists(c2path):
                        os.system("xterm -e 'cd ..; ./teamserver {} {} {}; $SHELL'&".format(cstsip, cstspw, c2path))
                        print("./teamserver {} {} {}".format(cstsip, cstspw, c2path))
                if not os.path.exists(c2path): input("That C2 profile doesn't exist. Lets Try this again with a proper argument."); quit()
        else:
                print("That was not a proper argument. Run the script again selecting a 1, 2 or 3."); quit()



qs	= input("Would You like to use the quick start feature pulling arguments from a .py file?\n> ")
yesornoQ(qs, "python3.6 QuickStart.py")
cstsip  = input("Lets get a few details out of the way first. What is the IP of your teamserver?\n> ")
cstspw	= input("What would you like the password to be for your teamserver?\n> ")
c21     = input("If you would like to use the Cobalt Strike Default C2 profile press 1\nIf you would like to use the amazon C2 profile press 2\nIf you would like to use your own C2 profile press 3\n> ")
redirun	= input("What is the username of your Redirector?\n> ")
redirpw	= getpass.getpass("What is the Redirector password?\n> ")
redirip	= input("What is the IP of your Redirectior?\n> ")
msfspfn	= input("What would you like to be the name of your MSF log file?(It will save to /root/Desktop/)\n> ")


#MSF Setup
input("OK! Now lets get Metasploit fired up.")
os.system("xterm -e 'msfconsole'&")
input("""I'm a dummy and can't figure out how to push commands to MSF sooo...
spool /root/Desktop/{}""".format(msfspfn))
input("Now we are gonna cat the log file to verify it's spooling.")
print("cat /root/Desktop/{}".format(msfspfn))
os.system("cat /root/Desktop/{}".format(msfspfn))

#CS Setup
input("\nNow we are gonna run a netstat to verify that nothing will conflict with CS.")
print("netstat -natup")
os.system("netstat -natup")
input("\nIf anything is using port 80 or 443 don't forget to kill it.\nWe are about to start the CS teamserver.""")
aggkill = input("Would you like to renew your CS trial? Yes or No\n> ")
yesorno(aggkill, "rm ~/.aggressor.prop")
csc2(c21)
input("The teamserver has been started in xterm.")
os.system("xterm -e 'cd ..; ./cobaltstrike; $SHELL'&")
print("./cobaltstrike")
input("The CS client has been started in xterm.")

#Simple HTTP server start
httpa   = input("Would you like to start a simple http server in a folder named SimpleHTTPServ on the desktop?\n> ")
yesorno(httpa, "xterm -e 'mkdir /root/Desktop/SimpleHTTPServ; cd /root/Desktop/SimpleHTTPServ; python -m SimpleHTTPServer; $SHELL'&")


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
socat tcp-listen:8000, fork tcp:{}:8000 &
netstat -natup
""".format(redirpw, redirpw, cstsip, cstsip, cstsip))

#Begin Enum
print("Congratulations! Setup is complete.")
enum	= input("Would you like to begin enumeration? Yes or No\n> ")
yesorno(enum,"python3.6 Enum.py")











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










