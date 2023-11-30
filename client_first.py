import socket

def send_message_to_server(ip, port, message):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((ip, port))
        
        # Send the message to the server
        client_socket.sendall(message)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the socket
        client_socket.close()