import socket

def receive_and_print_message(listen_ip, listen_port):
    # Create a socket object for receiving connections
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Bind the socket to a specific address and port
        server_socket.bind((listen_ip, listen_port))

        # Listen for incoming connections
        server_socket.listen(1)
        print(f"Listening for incoming connections on {listen_ip}:{listen_port}")

        # Accept a connection
        connection, address = server_socket.accept()
        print(f"Connection established with {address}")

        # Receive a message from the connected client
        received_message = connection.recv(1024).decode('utf-8')
        return received_message
        #print(f"Received final message from client: {received_message}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the listening socket
        server_socket.close()