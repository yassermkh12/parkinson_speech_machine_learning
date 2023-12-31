# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\hp\Desktop\app\parkinson1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from parkinson2 import Ui_parkinson2
from parkinson3 import Ui_parkinson3
import pymysql

class Ui_parkinson1(object):
    def openWindow(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_parkinson2()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def openParkinson3(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_parkinson3()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def setupUi(self, parkinson1):
        parkinson1.setObjectName("parkinson1")
        parkinson1.resize(700, 600)
        parkinson1.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        parkinson1.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(parkinson1)
        self.widget.setGeometry(QtCore.QRect(0, 0, 590, 490))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 290, 491))
        self.label.setStyleSheet("border-image: url(:/image/parkinson.jpg);\n"
"border-top-left-radius:50px;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(290, 0, 301, 491))
        self.label_2.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:50px;\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(380, 30, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(200,0,0,200);\n"
"background-color:rgba(255,255,255,255)\n"
"")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(330, 170, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(150,0,0,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 235, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(150,0,0,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"\n"
"")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(330, 320, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color:rgba(200, 0, 0,200);\n"
"    border-top-left-radius:40px;\n"
"    color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(255, 72, 26)\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget, clicked = lambda: self.openWindow() )
        self.pushButton_2.setGeometry(QtCore.QRect(330, 370, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color:rgba(200, 0, 0,200);\n"
"    border-bottom-right-radius:40px;\n"
"    color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(255, 72, 26)\n"
"}\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 290, 491))
        self.label_4.setStyleSheet("background-color:rgba(0,0,0,50);\n"
"border-top-left-radius:50px;\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(0, 70, 290, 150))
        self.label_5.setStyleSheet("background-color:rgba(0,0,0,50);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(50, 90, 161, 40))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("COLOR:rgba(200,200,200);\n"
"background-color:none;")
        self.label_6.setObjectName("label_6")
        self.exit = QtWidgets.QPushButton(self.widget)
        self.exit.setGeometry(QtCore.QRect(560, 5, 20, 20))
        self.exit.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-bottom:2px solid rgba(150,0,0,200);\n"
"}\n"
"QPushButton:Hover{\n"
"color : rgb(255, 255, 255);\n"
"background : rgba(150,0,0,200);\n"
"}")
        self.exit.setObjectName("exit")
        self.reduire = QtWidgets.QPushButton(self.widget)
        self.reduire.setGeometry(QtCore.QRect(535, 5, 20, 20))
        self.reduire.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-bottom:2px solid rgba(150,0,0,200);\n"
"}\n"
"QPushButton:Hover{\n"
"color : rgb(255, 255, 255);\n"
"background : rgba(150,0,0,200);\n"
"}")
        self.reduire.setObjectName("reduire")
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()

        self.retranslateUi(parkinson1)
        QtCore.QMetaObject.connectSlotsByName(parkinson1)

    def retranslateUi(self, parkinson1):
        _translate = QtCore.QCoreApplication.translate
        parkinson1.setWindowTitle(_translate("parkinson1", "Form"))
        self.label_3.setText(_translate("parkinson1", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("parkinson1", "User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("parkinson1", "Password"))
        self.pushButton.setText(_translate("parkinson1", "L o g  I n"))
        self.pushButton_2.setText(_translate("parkinson1", "Inscription"))
        self.label_6.setText(_translate("parkinson1", "PARKINSON"))
        self.exit.setText(_translate("parkinson1", "x"))
        self.reduire.setText(_translate("parkinson1", "-"))

        self.pushButton.clicked.connect(self.login)
        
    def login(self):
        mydb = pymysql.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "parkinson"
                )
        mycursor = mydb.cursor()
        
        user_name = self.lineEdit.text()
        password = self.lineEdit_2.text()
        
        mycursor.execute("SELECT * FROM user where user_name = '" + user_name + "' and password ='" + password + "'")
        
        result = mycursor.fetchone()
        
        if result:
            self.pushButton.clicked.connect(self.openParkinson3)
        else:
            dialog = QMessageBox(parkinson1)
            dialog.setText("veuillez verifier votre user name ou bien votre mot de passe")
            dialog.setWindowTitle("erreur")
            dialog.exec_()

        
        mydb.commit()
        mydb.close()
    
        
import app_parkinson


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    parkinson1 = QtWidgets.QWidget()
    ui = Ui_parkinson1()
    ui.setupUi(parkinson1)
    parkinson1.show()
    sys.exit(app.exec_())
