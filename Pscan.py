import  pyfiglet
import  sys
import  socket
from     datetime import datetime
import  nmap
import   color
from  colorama import  init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format
##############################

text ="port scanner"
cprint(figlet_format(text, font="standard"), "red")
text ="by X-dev"
cprint(figlet_format(text, font="standard"), "red")

print("\033[1;37;mEducational purpose Only: Coded by X-dev  WA : 0771523607")
print("\033[0;0;0 ")
print("\033[1;32;mcommon ports list")
print(" ")
print("port no 21   : FTP")
print("port no 80   : HTTP ")
print("port no 443  : HTTPS ")
print("port no 22   : SSH")
print(" ")

begin =  int(input("which port you want to scan >> "))
print(" ")



url = input("Enter web address >> ")
 
IP= socket.gethostbyname(url)
print(" ")
 
print("scanning >>> " + IP )

scanner = nmap.PortScanner()

for i in range(begin, begin+1):
	
	res = scanner.scan(IP,str(i))
	
	res = res['scan'][IP]['tcp'][i]['state']
	print(" ")
	print(f'port {i} is {res}.') 

