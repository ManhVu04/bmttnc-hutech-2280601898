import os
import sys

# Thêm thư mục gốc của dự án vào sys.path để import module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Title Label
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(320, 20, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        
        # Generate Keys Button
        self.btn_gen_keys = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_keys.setGeometry(QtCore.QRect(320, 70, 150, 30))
        self.btn_gen_keys.setObjectName("btn_gen_keys")
        
        # Plain Text Section
        self.label_plain = QtWidgets.QLabel(self.centralwidget)
        self.label_plain.setGeometry(QtCore.QRect(40, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_plain.setFont(font)
        self.label_plain.setObjectName("label_plain")
        
        self.txt_plain_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_plain_text.setGeometry(QtCore.QRect(180, 120, 571, 87))
        self.txt_plain_text.setObjectName("txt_plain_text")
        
        # Encryption/Decryption Buttons
        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(210, 220, 93, 28))
        self.btn_encrypt.setObjectName("btn_encrypt")
        
        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(570, 220, 93, 28))
        self.btn_decrypt.setObjectName("btn_decrypt")
        
        # Cipher Text Section
        self.label_cipher = QtWidgets.QLabel(self.centralwidget)
        self.label_cipher.setGeometry(QtCore.QRect(40, 260, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_cipher.setFont(font)
        self.label_cipher.setObjectName("label_cipher")
        
        self.txt_cipher_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_cipher_text.setGeometry(QtCore.QRect(180, 260, 571, 87))
        self.txt_cipher_text.setObjectName("txt_cipher_text")
        
        # Signing/Verification Section
        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(40, 360, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_info.setFont(font)
        self.label_info.setObjectName("label_info")
        
        self.txt_info = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_info.setGeometry(QtCore.QRect(180, 360, 571, 50))
        self.txt_info.setObjectName("txt_info")
        
        # Sign/Verify Buttons
        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(210, 420, 93, 28))
        self.btn_sign.setObjectName("btn_sign")
        
        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(570, 420, 93, 28))
        self.btn_verify.setObjectName("btn_verify")
        
        # Signature Section
        self.label_sign = QtWidgets.QLabel(self.centralwidget)
        self.label_sign.setGeometry(QtCore.QRect(40, 460, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_sign.setFont(font)
        self.label_sign.setObjectName("label_sign")
        
        self.txt_sign = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_sign.setGeometry(QtCore.QRect(180, 460, 571, 87))
        self.txt_sign.setObjectName("txt_sign")
        
        # Set up main window
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSA Cipher"))
        self.label_title.setText(_translate("MainWindow", "RSA Cipher"))
        self.btn_gen_keys.setText(_translate("MainWindow", "Generate Keys"))
        self.label_plain.setText(_translate("MainWindow", "Plain Text"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.label_cipher.setText(_translate("MainWindow", "Cipher Text"))
        self.label_info.setText(_translate("MainWindow", "Message"))
        self.btn_sign.setText(_translate("MainWindow", "Sign"))
        self.btn_verify.setText(_translate("MainWindow", "Verify"))
        self.label_sign.setText(_translate("MainWindow", "Signature"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
