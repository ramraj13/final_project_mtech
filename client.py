import socket
import pickle
import time
import randomid
import os
import json
import client_first
import findip
import encryption

import serverornot
import miniserver

# Define the server host and port
host = '192.168.110.9'  
port = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host ip_address

def get_private_ip():
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Connect to a server (doesn't have to be reachable)
        s.connect(('10.255.255.255', 1))

        # Get the private IP address
        private_ip = s.getsockname()[0]

        # Close the socket
        s.close()

        return private_ip
    except Exception as e:
        print(f"Error: {e}")
        return None

ip_address=get_private_ip()



# Connect to the server
client_socket.connect((host, port))

# Generate and send a random number to the server
random_number = str(randomid.generate_random_number_with_seed(os.getpid()))


data={  'PID': random_number,
         'IP': ip_address }

data_json=json.dumps(data) #serialize the dictonary via json
client_socket.send(data_json.encode('utf-8'))



try:
 
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        l=pickle.loads(data)
        
        #using list comphrehension to make a non-type to list of dictinaries
      
        list_of_dicts = [item for item in l if isinstance(item, dict)] if l else []
        
        sorted_list_of_dicts = sorted(list_of_dicts, key=lambda x: int(x['PID']))
        
        #print(sorted_list_of_dicts)
        address,flag=findip.find_next_ip(sorted_list_of_dicts,random_number) #giving list of list
        #print(type(address))
        print(findip.find_next_ip(sorted_list_of_dicts,random_number))


        print(sorted_list_of_dicts)
        private_key,public_key=encryption.generate_key_pair()

        #for the list to be only one ie only one machine was active in the contention period
        if( len(sorted_list_of_dicts)==1 ):
            message=input("Enter your message")
            encoded_data=encryption.encrypt(message,public_key)
            print(encoded_data[0])
            exit()

        yorn=serverornot.serveryorn(sorted_list_of_dicts,random_number)

       



        #check if the variable yorn is 1 then its a server
        if yorn==1:
            print("Starting server at : ",address[len(address)-1])
            recv_data=miniserver.start_server(address[len(address)-1],8888)
            
            print("Recv data: ", repr(recv_data))
    


        #if the client is the first one
        if   flag==0:
            print("Welcome you are first to start")
            message=input("Enter your message: ")
            encoded_data=encryption.encrypt(message,public_key)
            client_first.send_message_to_server(address[0],8888,encoded_data[0])
            client_first.send_message_to_server('192.168.110.9',9999,private_key.export_key())

        #if the client is in the middle of the list
        elif flag==1:
            print("You are in the middle ")
            message=input("Enter your  message")
            encoded_data=encryption.encrypt(message,public_key)
           
            
            client_first.send_message_to_server(address[1],8888,recv_data+encoded_data[0])
            client_first.send_message_to_server('192.168.110.9',9999,private_key.export_key())

        #if the client is the last one
        elif flag==2:
            
            print("You are at last")
            message=input("Enter your message: ")
            encoded_data=encryption.encrypt(message,public_key)

            client_first.send_message_to_server('192.168.110.9',9999,private_key.export_key())
            client_first.send_message_to_server('192.168.110.9',9999,'1'.encode('utf-8'))
            #print(str(recv_data)+message)

            #print("final message: ",recv_data+encoded_data[0])
            m=recv_data.hex()+encoded_data[0].hex()
            client_first.send_message_to_server('192.168.110.9',7777,m.encode('utf-8'))
            print("length  ",len(recv_data.hex()+encoded_data[0].hex()))
        
        break
    
    
except KeyboardInterrupt:
    print("Client is shutting down...")
    client_socket.close()
    print("Client has been shut down.")
    exit()
