# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui_xml/registration_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 260)
        Dialog.setMinimumSize(QtCore.QSize(480, 260))
        Dialog.setMaximumSize(QtCore.QSize(480, 260))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./frontend/resources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.email_line = QtWidgets.QLineEdit(Dialog)
        self.email_line.setGeometry(QtCore.QRect(200, 10, 271, 22))
        self.email_line.setObjectName("email_line")
        self.passw = QtWidgets.QLabel(Dialog)
        self.passw.setGeometry(QtCore.QRect(10, 50, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.passw.setFont(font)
        self.passw.setScaledContents(True)
        self.passw.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.passw.setObjectName("passw")
        self.email = QtWidgets.QLabel(Dialog)
        self.email.setGeometry(QtCore.QRect(10, 10, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.email.setFont(font)
        self.email.setScaledContents(True)
        self.email.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.email.setObjectName("email")
        self.pass_line = QtWidgets.QLineEdit(Dialog)
        self.pass_line.setGeometry(QtCore.QRect(200, 50, 271, 22))
        self.pass_line.setText("")
        self.pass_line.setObjectName("pass_line")
        self.name_line = QtWidgets.QLineEdit(Dialog)
        self.name_line.setGeometry(QtCore.QRect(200, 130, 271, 22))
        self.name_line.setText("")
        self.name_line.setObjectName("name_line")
        self.phone = QtWidgets.QLabel(Dialog)
        self.phone.setGeometry(QtCore.QRect(10, 90, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.phone.setFont(font)
        self.phone.setScaledContents(True)
        self.phone.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.phone.setObjectName("phone")
        self.phone_line = QtWidgets.QLineEdit(Dialog)
        self.phone_line.setGeometry(QtCore.QRect(200, 90, 271, 22))
        self.phone_line.setObjectName("phone_line")
        self.name = QtWidgets.QLabel(Dialog)
        self.name.setGeometry(QtCore.QRect(10, 130, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.name.setFont(font)
        self.name.setScaledContents(True)
        self.name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name.setObjectName("name")
        self.passp_line = QtWidgets.QLineEdit(Dialog)
        self.passp_line.setGeometry(QtCore.QRect(200, 170, 271, 22))
        self.passp_line.setText("")
        self.passp_line.setObjectName("passp_line")
        self.passp = QtWidgets.QLabel(Dialog)
        self.passp.setGeometry(QtCore.QRect(10, 170, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.passp.setFont(font)
        self.passp.setScaledContents(True)
        self.passp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.passp.setObjectName("passp")
        self.registration = QtWidgets.QPushButton(Dialog)
        self.registration.setGeometry(QtCore.QRect(170, 210, 141, 41))
        self.registration.setObjectName("registration")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TicketBase - Registration"))
        self.passw.setText(_translate("Dialog", "Password:"))
        self.email.setText(_translate("Dialog", "E-mail:"))
        self.phone.setText(_translate("Dialog", "Phone number:"))
        self.name.setText(_translate("Dialog", "Full name:"))
        self.passp.setText(_translate("Dialog", "Passport:"))
        self.registration.setText(_translate("Dialog", "Registration"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
