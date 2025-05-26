import sys
import os

# Thêm thư mục chứa mã nguồn vào path để import được module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
          # Kết nối các nút với hàm xử lý tương ứng
        self.ui.btn_gen_keys.clicked.connect(self.call_api_gen_keys)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(data["message"])
                msg.exec_()
            else:
                print("Error while calling API")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Error while calling API. Make sure the API server is running.")
                msg.exec_()
        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e)}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Connection error: {str(e)}")
            msg.exec_()

    def call_api_encrypt(self):
        message = self.ui.txt_plain_text.toPlainText()
        if not message:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Vui lòng nhập nội dung cần mã hóa!")
            msg.exec_()
            return
            
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        payload = {
            "message": message,
            "key_type": "public"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setPlainText(data["encrypted_message"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Error while calling encryption API")
                msg.exec_()
        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e)}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Connection error: {str(e)}")
            msg.exec_()

    def call_api_decrypt(self):
        ciphertext = self.ui.txt_cipher_text.toPlainText()
        if not ciphertext:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Vui lòng nhập nội dung cần giải mã!")
            msg.exec_()
            return
            
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        payload = {
            "ciphertext": ciphertext,
            "key_type": "private"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setPlainText(data["decrypted_message"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Error while calling decryption API")
                msg.exec_()
        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e)}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Connection error: {str(e)}")
            msg.exec_()

    def call_api_sign(self):
        message = self.ui.txt_info.toPlainText()
        if not message:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Vui lòng nhập nội dung cần ký!")
            msg.exec_()
            return
            
        url = "http://127.0.0.1:5000/api/rsa/sign"
        payload = {
            "message": message
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_sign.setPlainText(data["signature"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Signed Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Error while calling signing API")
                msg.exec_()
        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e)}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Connection error: {str(e)}")
            msg.exec_()

    def call_api_verify(self):
        message = self.ui.txt_info.toPlainText()
        signature = self.ui.txt_sign.toPlainText()
        
        if not message or not signature:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Vui lòng nhập đầy đủ nội dung và chữ ký!")
            msg.exec_()
            return
            
        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {
            "message": message,
            "signature": signature
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if data["is_verified"]:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Verified Successfully")
                    msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Verification Failed")
                    msg.exec_()
            else:
                print("Error while calling API")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Error while calling verification API")
                msg.exec_()
        except requests.exceptions.RequestException as e:
            print(f"Error: {str(e)}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Connection error: {str(e)}")
            msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Thiết lập đường dẫn cho plugins Qt
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "platforms")
    
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
