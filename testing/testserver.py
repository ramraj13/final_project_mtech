import socket

def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(1)

    print(f"Server listening on port {port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received data: {data}")

        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    server_port = 12345  # Replace with the desired port number
    start_server(server_port)
