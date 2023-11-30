import base64
import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import subprocess
import json
import cryptography


def generate_key_pair():
    private_key = RSA.generate(2048)
    public_key = private_key.publickey()

    return private_key, public_key

def encrypt(message, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(message.encode('utf-8'))

    return ciphertext, len(ciphertext)

def decrypt(ciphertext, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher.decrypt(ciphertext).decode('utf-8')

    return decrypted_message



# Example usage:

'''def run_requests(private_key, encrypted_message):
    # Ensure that the private key is encoded in base64
    #if isinstance(private_key, bytes):
    #    private_key_base64 = base64.b64encode(private_key).decode('utf-8')
    #else:
    private_key_base64 = private_key

    # Ensure that the encrypted message is encoded in base64
    if isinstance(encrypted_message, bytes):
        encrypted_message_base64 = base64.b64encode(encrypted_message).decode('utf-8')
    else:
        encrypted_message_base64 = encrypted_message

    # Ensure that the private key and encrypted message are properly escaped
    bash_command = [
        "./test.sh",
        f'"{json.dumps(private_key_base64)}"',  # Wrap the private key in quotes
        f'"{json.dumps(encrypted_message_base64)}"'  # Wrap the encrypted message in quotes
    ]

    process = subprocess.Popen(bash_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()

    if process.returncode != 0:
        print(f"Error: {err.decode('utf-8')}")
    else:
        print(f"Output: {out.decode('utf-8')}")
'''