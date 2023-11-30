import socket

def handle_client(client_socket):
    data = client_socket.recv(1024)
    print(f"Received data: {data}")
    client_socket.close()
    return data

def start_server(ip, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(5)
    print(f"Server listening on {ip}:{port}")

    try:
        while True:
            # Accept a connection from a client
            client_socket, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")

            # Handle the client in the main thread
            processed_data = handle_client(client_socket)

            # Process data in the main thread
            print(f"Processing data in main thread: {processed_data}")

            return processed_data

    except KeyboardInterrupt:
        print("Server stopping...")
    finally:
        server_socket.close()

#print(start_server('0.0.0.0', 12345))
