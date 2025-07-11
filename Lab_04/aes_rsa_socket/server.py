from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import hashlib

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

server_key = RSA.generate(2048)

clients = []

def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext



def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()



def handle_client(client_socket, client_address):
    print(f"connected to {client_address}")
    
    client_socket.send(server_key.publickey().export_key(format='PEM'))
    
    client_received_key = RSA.import_key(client_socket.recv(2048))
    aes_key = get_random_bytes(16)
    cipher = PKCS1_OAEP.new(client_received_key)
    encrypt_aes_key = cipher.encrypt(aes_key)
    client_socket.send(encrypt_aes_key)
    clients.append((client_socket, aes_key))
    while True:
        encrypted_msg = client_socket.recv(1024)
        decrypted_msg = decrypt_message(aes_key, encrypted_msg)
        print(f"Received message from {client_address}: {decrypted_msg}")
        for client, key in clients:
            if client != client_socket:
                encrypted_message = encrypt_message(key, decrypted_msg)
                client.send(encrypted_message)
        if decrypted_msg == 'exit':
            break
            clients.remove((client_socket, aes_key))
    client_socket.close()
    print(f"Connection closed for {client_address}")

# Main server loop
print("Server started on localhost:12345")
while True:
    client_socket, client_address = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    thread.start()
    print(f"Active connections: {threading.active_count() - 1}")
        