import rsa
import os


class RSACipher:
    def __init__(self):
        self.keys_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'keys')
        if not os.path.exists(self.keys_dir):
            os.makedirs(self.keys_dir)
        self.public_key_file = os.path.join(self.keys_dir, 'publicKey.pem')
        self.private_key_file = os.path.join(self.keys_dir, 'privateKey.pem')

    def generate_keys(self):
        (public_key, private_key) = rsa.newkeys(1024)
        with open(self.public_key_file, 'wb') as p:
            p.write(public_key.save_pkcs1('PEM'))
        with open(self.private_key_file, 'wb') as p:
            p.write(private_key.save_pkcs1('PEM'))

    def load_keys(self):
        try:
            with open(self.public_key_file, 'rb') as p:
                public_key = rsa.PublicKey.load_pkcs1(p.read())
            with open(self.private_key_file, 'rb') as p:
                private_key = rsa.PrivateKey.load_pkcs1(p.read())
            return private_key, public_key
        except FileNotFoundError:
            # Nếu chưa có key, tạo key mới
            return self.generate_keys()

    def encrypt(self, message, key):
        return rsa.encrypt(message.encode('utf-8'), key)

    def decrypt(self, ciphertext, key):
        try:
            return rsa.decrypt(ciphertext, key).decode('utf-8')
        except:
            return False

    def sign(self, message, key):
        return rsa.sign(message.encode('utf-8'), key, 'SHA-1')

    def verify(self, message, signature, key):
        try:
            encoded_message = message.encode('utf-8')
            rsa.verify(encoded_message, signature, key)
            return True
        except Exception as e:
            print(f"Verification failed: {str(e)}")
            return False