import socket
import sys
from datetime import datetime
target=input("enter the ip adresses or URL code ")
try:
    target_ip=socket.gethostbyname(target)
except socket.gaierror:
    print("\n  [!] host name could not be resolved . Exiting.")
    sys.exit()
print("_"*50)    
print(f"scanning the target: {target_ip}")
print(f"scanning start at : {str(datetime.now())}")
print("_"* 50)
try :
    for port in range(1,101):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(0.5)
        result=s.connect_ex((target_ip,port))
    if result == 0 :
        print(f"port {port} : [OPEN]")  
    else :
        print(f"port {port} : checking...")
        s.close()
except KeyboardInterrupt:
    print("\n [!] user stoped the scan") 
    sys.exit()       
except socket.error:
    print("\n [!] server not responding")
    sys.exit()
print("_" * 50)   
print(" Scanning Completed .")
#end