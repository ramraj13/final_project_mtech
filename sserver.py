import socket
import subprocess
import threading

# Function to handle client connections
def handle_client(client_socket, data_list):
    try:
        while True:
            data = client_socket.recv(1024).decode('utf-8')

            if not data:
                break

            if data == '1':
                print("Received 1. Printing and clearing list:")
                subprocess.run(["bash", "final_1.sh"] + data_list)
                data_list.clear()

            else:
                data_list.append(data)
    except ConnectionResetError:
        pass  # Handle client disconnecting

    client_socket.close()

# Function to start the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    print("[Server listening on port]: 9999")

    data_list = []

    try:
        while True:
            client_socket, addr = server.accept()
            print(f"Accepted connection from {addr}")
            client_handler = threading.Thread(target=handle_client, args=(client_socket, data_list))
            client_handler.start()
    except KeyboardInterrupt:
        print("Server shutting down...")
        server.close()

if __name__ == "__main__":
    start_server()
