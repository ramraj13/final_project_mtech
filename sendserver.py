import socket
import time
import signal
import sys
import threading
# Create a list to store messages
messages = []

def handle_client(client_socket):
    while True:
        try:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break  # If no data is received, break the loop

            # Decode and store the message
            message = data.decode('utf-8')
            messages.append(message)
            print(f"Received message: {message}")

        except Exception as e:
            print(f"Error handling client: {e}")
            break

    # Close the client socket when the loop exits
    client_socket.close()

def restart_server():
    while True:
        time.sleep(30)
        print("\nRestarting server and flushing messages...")
        messages.clear()

def start_server():
    # Register the signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_socket.bind(('localhost', 5555))
    server_socket.listen(5)
    print("Server listening on port 5555")

    # Start the restart server loop in the background
    restart_server_thread = threading.Thread(target=restart_server)
    restart_server_thread.start()

    while True:
        # Accept a connection from a client
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")

        # Handle the client
        handle_client(client_socket)

def signal_handler(sig, frame):
    print("\nServer terminated by Ctrl+C")
    sys.exit(0)

if __name__ == "__main__":
    start_server()
