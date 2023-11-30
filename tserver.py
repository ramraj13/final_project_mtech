import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import subprocess

def receive_encrypted_data():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 7777))
    server_socket.listen(1)

    print("Server listening on port 7777...")

    while True:
        connection, address = server_socket.accept()
        print("Connection from", address)

        encrypted_data = connection.recv(4096)
        if not encrypted_data:
            break

       
        print("Decrypted data:", encrypted_data.decode('utf-8'))

        # Execute bash script with the decrypted data
        subprocess.run(['bash', 'final_2.sh', encrypted_data])

        # Clear data and continue listening
        connection.send(b'Data received successfully!')
        connection.close()


receive_encrypted_data()