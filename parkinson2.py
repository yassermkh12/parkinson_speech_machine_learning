# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\hp\Desktop\app\parkinson2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from parkinson3 import Ui_parkinson3
import pymysql


class Ui_parkinson2(object):
    def openParkinson3(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_parkinson3()
        self.ui.setupUi(self.window)
        self.window.show()
    
    
    def setupUi(self, parkinson2):
        parkinson2.setObjectName("parkinson2")
        parkinson2.resize(597, 490)
        parkinson2.setStyleSheet("backgroud-color:rgba(0,0,0)")
        parkinson2.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        parkinson2.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(parkinson2)
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
        self.label_3.setGeometry(QtCore.QRect(360, 10, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(200,0,0,200)")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(330, 250, 220, 40))
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
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 300, 220, 40))
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
        self.pushButton.setGeometry(QtCore.QRect(330, 420, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color:rgba(200, 0, 0,200);\n"
"    border-radius:10px;\n"
"    color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(255, 72, 26)\n"
"    \n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 100, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(150,0,0,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"\n"
"")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(330, 150, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(150,0,0,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"\n"
"")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(330, 350, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(150,0,0,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"\n"
"")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setGeometry(QtCore.QRect(330, 200, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(150,0,0,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"\n"
"")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
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
        self.label_6.setStyleSheet("COLOR:rgba(200,200,200);")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(parkinson2)
        QtCore.QMetaObject.connectSlotsByName(parkinson2)

    def retranslateUi(self, parkinson2):
        _translate = QtCore.QCoreApplication.translate
        parkinson2.setWindowTitle(_translate("parkinson2", "Form"))
        self.label_3.setText(_translate("parkinson2", "Inscription"))
        self.lineEdit.setPlaceholderText(_translate("parkinson2", "User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("parkinson2", "Password"))
        self.pushButton.setText(_translate("parkinson2", "Inscription"))
        self.lineEdit_3.setPlaceholderText(_translate("parkinson2", "First Name"))
        self.lineEdit_4.setPlaceholderText(_translate("parkinson2", "Last Name"))
        self.lineEdit_5.setPlaceholderText(_translate("parkinson2", "Password"))
        self.lineEdit_6.setPlaceholderText(_translate("parkinson2", "Age"))
        self.label_6.setText(_translate("parkinson2", "PARKINSON"))
   
        self.pushButton.clicked.connect(self.inscription)
        
        
    def inscription(self):
            mydb = pymysql.connect(
                    host = "localhost",
                    user = "root",
                    password = "",
                    database = "parkinson"
                    )
            mycursor = mydb.cursor()
            
            last_name =  self.lineEdit_4.text()
            first_name = self.lineEdit_3.text()
            age = self.lineEdit_6.text()
            user_name = self.lineEdit.text()
            password = self.lineEdit_2.text()
            
            mycursor.execute("INSERT INTO user(nom,prenom,age,user_name,password) VALUES('"+ last_name +"','" + first_name + "','" + age + "','" + user_name + "','" + password +"')")
            result = mycursor.fetchone()
            
            if result:
                dialog = QMessageBox(parkinson2)
                dialog.setText("veuillez verifier votre user name ou bien votre mot de passe")
                dialog.setWindowTitle("erreur")
                dialog.exec_()   
            else:
                self.pushButton.clicked.connect(self.openParkinson3)
                
            mydb.commit()
            mydb.close()


import app_parkinson


if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    parkinson2 = QtWidgets.QWidget()
    ui = Ui_parkinson2()
    ui.setupUi(parkinson2)
    parkinson2.show()
    sys.exit(app.exec_())
