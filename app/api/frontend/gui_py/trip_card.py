# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_xml/trip_card.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from backend.backend import *


##class Ui_Form(QtWidgets.QWidget):
#  def __init__( self, parent=None):
#    super(Ui_Form, self).__init__(parent)

#   self.pushButton = QtWidgets.QPushButton('I am in Test widget')

#   layout = QtWidgets.QHBoxLayout()
#   layout.addWidget(self.pushButton)
#   self.setLayout(layout)

class Ui_Form(QtWidgets.QWidget):
    def __init__(self, data, user_data, parent=None):
        super(Ui_Form, self).__init__(parent)
        self.data = data
        self.user_id = get_user_id(user_data['email'], user_data['password'])
        self.keys = get_trip_keys()
        self.setupUi()
        self.show_trips()

    def pushButton_clicked(self):
        print("Shooop")
        for i in range(len(self.data)):
            add_trip_to_user(self.user_id, self.data[i][0])
            print(self.data[i][0])
        print(get_user_by_id(self.user_id))

    def show_trips(self):
        self.tableWidget.setHorizontalHeaderLabels(self.keys)
        self.tableWidget.setRowCount(0)
        for rowNumber in range(len(self.data)):
            self.tableWidget.insertRow(rowNumber)
            for column_number in range(1, len(self.keys) + 1):
                self.tableWidget.setItem(rowNumber, column_number - 1,
                                         QtWidgets.QTableWidgetItem(str(self.data[rowNumber][column_number])))

    def setupUi(self):
        # Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("buy")

        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(2)
        if len(self.data) == 2:
            self.tableWidget.setFixedSize(QtCore.QSize(1050, 120))
        else:
            print("kekeees")
            self.tableWidget.setFixedSize(QtCore.QSize(1050, 80))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        total = 0
        for i in range(len(self.data)):
            total += int(self.data[i][8])

        self.label_22 = QtWidgets.QLabel("Total price: " + str(total))

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.layout.addWidget(self.label_22)
        self.layout.addWidget(self.pushButton)

        self.pushButton.clicked.connect(self.pushButton_clicked)

        self.setLayout(self.layout)
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        # Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Buy"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
