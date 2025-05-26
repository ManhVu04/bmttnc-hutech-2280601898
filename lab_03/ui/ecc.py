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
        
        # Message Section
        self.label_message = QtWidgets.QLabel(self.centralwidget)
        self.label_message.setGeometry(QtCore.QRect(40, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_message.setFont(font)
        self.label_message.setObjectName("label_message")
        
        self.txt_message = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_message.setGeometry(QtCore.QRect(180, 120, 571, 87))
        self.txt_message.setObjectName("txt_message")
        
        # Sign/Verify Buttons
        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(210, 220, 93, 28))
        self.btn_sign.setObjectName("btn_sign")
        
        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(570, 220, 93, 28))
        self.btn_verify.setObjectName("btn_verify")
        
        # Signature Section
        self.label_signature = QtWidgets.QLabel(self.centralwidget)
        self.label_signature.setGeometry(QtCore.QRect(40, 260, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_signature.setFont(font)
        self.label_signature.setObjectName("label_signature")
        
        self.txt_signature = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_signature.setGeometry(QtCore.QRect(180, 260, 571, 120))
        self.txt_signature.setObjectName("txt_signature")
        
        # Result Section
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(40, 400, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_result.setFont(font)
        self.label_result.setObjectName("label_result")
        
        self.txt_result = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_result.setGeometry(QtCore.QRect(180, 400, 571, 87))
        self.txt_result.setObjectName("txt_result")
        self.txt_result.setReadOnly(True)
        
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
        MainWindow.setWindowTitle(_translate("MainWindow", "ECC Cipher"))
        self.label_title.setText(_translate("MainWindow", "ECC Cipher"))
        self.btn_gen_keys.setText(_translate("MainWindow", "Generate Keys"))
        self.label_message.setText(_translate("MainWindow", "Message"))
        self.btn_sign.setText(_translate("MainWindow", "Sign"))
        self.btn_verify.setText(_translate("MainWindow", "Verify"))
        self.label_signature.setText(_translate("MainWindow", "Signature"))
        self.label_result.setText(_translate("MainWindow", "Result"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
