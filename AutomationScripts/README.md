Move and run the entire AutomationScripts folder into the same directory as CS client and teamserver

In order to configure the redir, MSF, CS Teamserver, CS Client, and run proxychains nmap commands use SetupScript.py

Run SetupScript.py with python3.6 (others may work but havn't been tested).


C2.profile		- Amazon C2 profile with a sleep of zero.
Enum.py			- Proxychains netdiscover and Proxychains nmap commands. Should be enough to enumerate Quantico (will be prompted to run after SetupScript.py).
SetupScript.py		- Configures redir, MSF, CS Teamserver, CS Client, and can kickoff Enum.py
QuickStart.py		- nano this and fill out then run to do run SetupScript.py faster
QuickStartBackground.py	- This is called by QuickStart.py to run setup quickly.




