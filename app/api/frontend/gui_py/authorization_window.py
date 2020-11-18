# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui_xml/authorization_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 150)
        Dialog.setMinimumSize(QtCore.QSize(480, 150))
        Dialog.setMaximumSize(QtCore.QSize(480, 150))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.email = QtWidgets.QLabel(Dialog)
        self.email.setGeometry(QtCore.QRect(10, 10, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.email.setFont(font)
        self.email.setScaledContents(True)
        self.email.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.email.setObjectName("email")
        self.email_line = QtWidgets.QLineEdit(Dialog)
        self.email_line.setGeometry(QtCore.QRect(200, 10, 271, 22))
        self.email_line.setObjectName("email_line")
        self.pass_line = QtWidgets.QLineEdit(Dialog)
        self.pass_line.setGeometry(QtCore.QRect(200, 50, 271, 22))
        self.pass_line.setText("")
        self.pass_line.setObjectName("pass_line")
        self.passw = QtWidgets.QLabel(Dialog)
        self.passw.setGeometry(QtCore.QRect(10, 50, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.passw.setFont(font)
        self.passw.setScaledContents(True)
        self.passw.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.passw.setObjectName("passw")
        self.login = QtWidgets.QPushButton(Dialog)
        self.login.setGeometry(QtCore.QRect(10, 100, 141, 41))
        self.login.setObjectName("login")
        self.reg = QtWidgets.QPushButton(Dialog)
        self.reg.setGeometry(QtCore.QRect(332, 100, 141, 41))
        self.reg.setObjectName("reg")
        self.logout = QtWidgets.QPushButton(Dialog)
        self.logout.setGeometry(QtCore.QRect(170, 100, 141, 41))
        self.logout.setObjectName("logout")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TicketBase - Authorization"))
        self.email.setText(_translate("Dialog", "E-mail:"))
        self.passw.setText(_translate("Dialog", "Password:"))
        self.login.setText(_translate("Dialog", "Log in"))
        self.reg.setText(_translate("Dialog", "Register"))
        self.logout.setText(_translate("Dialog", "Log out"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
