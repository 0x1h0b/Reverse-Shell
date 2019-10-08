# Reverse-Shell
A simple reverse shell written in Python.

 This project is under progress.. but you can use it.
 Planning on adding extra functions.

any ideas are welcomed.

## Requirements :-
   Python3 on both client and server PCs.
## steps:-
  (Linux)
1. download the project.
2. Navigate to the project directory.
3. run the  server.py file in terminal

        sudo python3 server.py <your_ip_addr> <port_no_to_use>
        
   
     sudo beacause we need root privileges to create a sockets. 
     give a port no that is not commonly used by other services. that is to avoid conflicts.
         
 4. on the clients Pc run the client.py file in  terminal
 
           sudo python3 client.py <server_ip_addr> <port_no_to_use> 
            
      the same port used at server side
      
 NOTE:- if you are testing on same machine or host.. then you can use 127.0.0.1 (the loopback address) as the IP addr for both 
 server and client .
 
 NOTE:- if you are testing on same network you can use your private IP, else you must use your public IP.
      
     
  (WINDOWS)
    
 1. open cmd as Administrator, then simply navigate to the project file and run the scipts as mentioned above just omit the sudo
    part and continue (python3 server.py <port...).
  
  

  
  
  ## NOTE:- 
   before running client file make sure server is running and ready to listen to any incoming connections (just make sure 
   it executes perfectly without any errors :-) )
