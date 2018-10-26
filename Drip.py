def Winesec():
    print(""* 100)
def Cls():
    Winesec()
    print ("\n" * 100)
import time
import sys
from time import sleep
import webbrowser
import os
User = input("Please enter your username /")
Pass = input("please enter your password /")
if User == 'root' and Pass == 'toor':
    print("wb")
else:
    print("PASSWORD WAS INCORRECT")
    exit()
Cls()
EULA = False
while EULA == False:
    Cls()
    print("By using this tool you agree to only use it within laws of")
    print("the data protection act 1988 and computer misuse act of 1990")
    print("by typing READ a webpage will open you to the website where you can read the law")
    print("")
    print("by typing YES in capitals you agree to these rules")
    print("")
    EULAINPUT = input("Do you agree /")
    if EULAINPUT == 'YES':
        EULA = True
    if EULAINPUT == 'READ':
        url = 'https://www.legislation.gov.uk/ukpga/1990/18/contents'
        chrome_path = '/usr/local/bin/firefox %s'
        webbrowser.get(chrome_path).open(url)
        url = 'https://www.gov.uk/data-protection'
        chrome_path = '/usr/local/bin/firefox %s'
        webbrowser.get(chrome_path).open(url)
    else:
        print("YOU MUST ACCEPT EULA / IGNORE IF YOU PUT YES")
        time.sleep(2)
time.sleep(1)
Cls()
print("""
██████╗ ██████╗ ██╗██████╗ 
██╔══██╗██╔══██╗██║██╔══██╗
██║  ██║██████╔╝██║██████╔╝
██║  ██║██╔══██╗██║██╔═══╝ 
██████╔╝██║  ██║██║██║     
╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝""")
print("***************************")
print("01: Vps Booter")
print("02: Scanner ")
print("03: Our Github")
print("04: Our Instagram")
print("05: Exit")
print("***************************")
Awns = input("Please select a line number /")
if Awns == '1':
       try:
            exec (open ("Booter.sh", encoding="utf8").read ())
       except:
            print("Booter not found please fix")
            time.sleep(5)
            exit()
if Awns == '2':
    try:
        exec (open ("Scanner.sh", encoding="utf8").read ())
    except:
        print("Scanner not found please fix")
        time.sleep(5)
        exit()
if Awns == '3':
            url = 'https://github.com/WineSec/DripV1'
            chrome_path = '/usr/local/bin/firefox %s'
            webbrowser.get(chrome_path).open(url)
            time.sleep(5)
            exit()
if Awns == '4':
            url = 'https://www.instagram.com/wine.sec/'
            chrome_path = '/usr/local/bin/firefox %s'
            webbrowser.get(chrome_path).open(url)
            time.sleep(5)
            exit()    
if Awns == '5':
    exit()
else:
    print("nothing selected, exiting")
    time.sleep(1)
