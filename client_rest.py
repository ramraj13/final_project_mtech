import socket

def receive_message_and_send_to_another_ip(listen_ip, listen_port, send_ip, send_port, own_message):
   
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
      
        server_socket.bind((listen_ip, listen_port))
        server_socket.listen(1)
        print(f"Listening for incoming connections on {listen_ip}:{listen_port}")

        connection, address = server_socket.accept()
        print(f"Connection established with {address}")

        received_message = connection.recv(1024).decode('utf-8')
        print(f"Received message from client: {received_message}")

        combined_message = f"{own_message} - {received_message}"

        send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            send_socket.connect((send_ip, send_port))

            send_socket.sendall(combined_message.encode('utf-8'))
            print(f"Sent combined message to {send_ip}:{send_port}")

        except Exception as e:
            print(f"Error while sending message to {send_ip}:{send_port}: {e}")

        finally:
            send_socket.close()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        
        server_socket.close()
