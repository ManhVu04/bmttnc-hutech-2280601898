import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Kết nối nút Encrypt và Decrypt với hàm tương ứng
        self.ui.Encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.Decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        plain_text = self.ui.plainTextEdit.toPlainText()
        key = self.ui.plainTextEdit_2.toPlainText()
        if not plain_text or not key:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Vui lòng nhập đầy đủ Plain text và Key!")
            msg.exec_()
            return
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "text": plain_text,
            "key": key
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plainTextEdit_3.setPlainText(data.get("encrypted_message", ""))
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e)

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.plainTextEdit_3.toPlainText(),
            "key": self.ui.plainTextEdit_2.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plainTextEdit.setPlainText(data.get("decrypted_message", ""))
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
