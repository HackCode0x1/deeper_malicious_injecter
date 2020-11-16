
from termcolor import *

def COlor():
    global G, Y, B, R, W , M , C , end ,Bold,underline
    G,Y,B,R,W,M,C,end= '\033[92m','\033[93m','\033[94m','\033[91m','\x1b[37m','\x1b[35m','\x1b[36m','\033[0m'
    Bold = "\033[1m"
    underline = "\033[4m"


def Win_Payloads():

    global Payloads 
    


    Payloads = ['windows/meterpreter/reverse_tcp', \
    'windows/meterpreter/reverse_http', \
    'windows/meterpreter/reverse_https', \
    'windows/shell/reverse_tcp'

    ]
    

    

    for i in Payloads:
        print(W+"[%d]" % (Payloads.index(i)+1), colored(i, 'cyan'))


   
    

def Linux_Payloads():
    global Payloads 


    Payloads = ['linux/x86/shell/reverse_tcp ', \
    'linux/x86/meterpreter/reverse_tcp ', \
    'linux/x64/meterpreter/reverse_tcp', \
    'linux/x86/meterpreter/bind_tcp ', \
    'linux/x86/shell/bind_tcp', \
    'linux/x86/meterpreter_reverse_http', \
    'linux/x86/meterpreter_reverse_https'

    ]

    
    for i in Payloads:
        print(W+"[%d]" % (Payloads.index(i)+1), colored(i, 'cyan'))

 




def Osx_Payloads():
    global Payloads 
    Payloads = ['osx/x64/meterpreter/reverse_tcp', \
    'osx/x64/meterpreter/bind_tcp', \
    'osx/x64/shell_reverse_tcp', \
    'osx/x86/shell_reverse_tcp '

    ]

    for i in Payloads:
        print(W+"[%d]" % (Payloads.index(i)+1), colored(i, 'cyan'))


   



    
def Android_Payloads():
    global Payloads 
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
        print(W+"[%d]" % (Payloads.index(i)+1), colored(i, 'cyan'))

   


def Bash_payload():
    global Payloads 
    Payloads = "cmd/unix/reverse_bash"

    for i in Payloads:
        print(W+"[%d]" % (Payloads.index(i)+1), colored(i, 'cyan'))




def Apple_Payloads():
    global Payloads
    Payloads  = [
    'apple_ios/aarch64/meterpreter_reverse_http', \
    'apple_ios/aarch64/meterpreter_reverse_https', \
    'apple_ios/aarch64/meterpreter_reverse_tcp', \
    'apple_ios/aarch64/shell_reverse_tcp ', \
    'apple_ios/armle/meterpreter_reverse_http',\
    'apple_ios/armle/meterpreter_reverse_https',\
    'apple_ios/armle/meterpreter_reverse_tcp',\
    ]

    for i in Payloads:
        print(W+"[%d]" % (Payloads.index(i)+1), colored(i, 'cyan'))




def Perl_Payloads():
    global Payloads 
    Payloads  = [
    'cmd/unix/bind_perl', \
    'cmd/unix/bind_perl_ipv6 ', \
    'cmd/unix/reverse_perl', \
    'cmd/unix/reverse_perl_ssl  ', \
    'cmd/windows/bind_perl',\
    'cmd/windows/reverse_perl',\

    ]
    for i in Payloads:
        print(W+"[%d]" % (Payloads.index(i)+1), colored(i, 'cyan'))




def Ruby_Payloads():
    global Payloads 
    Payloads  = [
    'ruby/pingback_bind_tcp ', \
    'ruby/pingback_reverse_tcp ', \
    'ruby/shell_bind_tcp', \
    'ruby/shell_bind_tcp_ipv6  ', \
    'ruby/shell_reverse_tcp',\
    'ruby/shell_reverse_tcp_ssl',\

    ]


    for i in Payloads:
        print(W+"[%d]" % (Payloads.index(i)+1), colored(i, 'cyan'))






def Python_Payloads():
    global Payloads 
    Payloads  = [
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

    for i in Payloads:
        print(W+"[%d]" % (Payloads.index(i)+1), colored(i, 'cyan'))





def Java_Payloads():
    global Payloads

    Payloads = ["payload/java/meterpreter/reverse_http", 'payload/java/meterpreter/reverse_https ',
    "payload/java/meterpreter/reverse_tcp"]





    for i in Payloads:
        print(W+"[%d]" % (Payloads.index(i)+1), colored(i, 'cyan'))







def Php_Payloads():
    global Payloads 

    Payloads = ["payload/php/reverse_perl", "payload/php/reverse_php", "php/meterpreter_reverse_tcp"]


    for i in Payloads:
        print(W+"[%d]" % (Payloads.index(i)+1), colored(i, 'cyan'))




def Asp_Payloads():
    global Payloads 

    asp_payload = 'windows/meterpreter/reverse_tcp'

    for i in Payloads:
        print(W+"[%d]" % (Payloads.index(i)+1), colored(i, 'cyan'))




COlor()