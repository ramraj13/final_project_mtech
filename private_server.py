import socket
import threading
import time
import pickle
import json
import sendserver

# Define the server host and port
host = '0.0.0.0'
port = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address
server_socket.bind((host, port))

# List to store client connections and received numbers
clients = []
stored_numbers = []
last_broadcast_time = time.time()

# Function to handle individual clients
def handle_client(client_socket):
    while True:
        try:
            number = client_socket.recv(1024).decode('utf-8')
            recv_dict=json.loads(number)
            if not number:
                break
            stored_numbers.append(recv_dict)
        except Exception as e:
            print(f"Connection error: {str(e)}")
            break
        
# Function to clear stored numbers every 5 minutes
def clear_stored_numbers():
    while True:
        time.sleep(30)  # Wait for 5 minutes
        stored_numbers.clear()

# Start the clear numbers thread
clear_thread = threading.Thread(target=clear_stored_numbers)
clear_thread.daemon = True
clear_thread.start()

# Function to periodically broadcast the list of stored numbers
def broadcast_numbers():
    global last_broadcast_time
    while True:
        current_time = time.time()
        if current_time - last_broadcast_time >= 30:  # Broadcast every 10 seconds
            if stored_numbers:
                #broadcast_message = "Stored numbers: " + ", ".join(stored_numbers)
                broadcast_message = pickle.dumps(stored_numbers) #using picket to serialize the list of stored numbers and send it over the socket connection
                for client in clients: 
                    try:
                        client.send(broadcast_message)
                    except Exception as e:
                        print(f"Broadcast error: {str(e)}")
                last_broadcast_time = current_time

# Start the broadcast thread
broadcast_thread = threading.Thread(target=broadcast_numbers)
broadcast_thread.daemon = True
broadcast_thread.start()

# Start listening for incoming connections
server_socket.listen(5)
print("Server is listening on {}:{}".format(host, port))


try:
    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        print(f"Accepted connection from {client_address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()
except KeyboardInterrupt:
    print("Server is shutting down...")
    server_socket.close()
    print("Server has been shut down.")
    exit()
