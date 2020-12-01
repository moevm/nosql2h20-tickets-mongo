# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui_xml/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 720)
        Dialog.setMinimumSize(QtCore.QSize(1280, 720))
        Dialog.setMaximumSize(QtCore.QSize(1280, 720))
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./frontend/resources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(29, 130, 1181, 521))
        self.scrollArea.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1179, 519))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 1131, 241))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 49, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(240, 200, 121, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.from_list = QtWidgets.QComboBox(self.groupBox)
        self.from_list.setGeometry(QtCore.QRect(160, 50, 361, 31))
        self.from_list.setObjectName("from_list")
        self.to_list = QtWidgets.QComboBox(self.groupBox)
        self.to_list.setGeometry(QtCore.QRect(160, 120, 361, 31))
        self.to_list.setObjectName("to_list")
        self.part = QtWidgets.QLabel(self.groupBox)
        self.part.setGeometry(QtCore.QRect(10, 10, 1111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.part.setFont(font)
        self.part.setObjectName("part")
        self.types = QtWidgets.QComboBox(self.groupBox)
        self.types.setGeometry(QtCore.QRect(760, 51, 361, 31))
        self.types.setObjectName("types")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(540, 50, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(540, 119, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.classes_2 = QtWidgets.QComboBox(self.groupBox)
        self.classes_2.setGeometry(QtCore.QRect(760, 120, 361, 31))
        self.classes_2.setObjectName("classes_2")
        self.search = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.search.setGeometry(QtCore.QRect(490, 440, 171, 41))
        self.search.setObjectName("search")
        self.back_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.back_button.setGeometry(QtCore.QRect(280, 310, 171, 41))
        self.back_button.setObjectName("back_button")
        self.next_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.next_button.setGeometry(QtCore.QRect(700, 310, 171, 41))
        self.next_button.setObjectName("next_button")
        self.add_flight = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.add_flight.setGeometry(QtCore.QRect(490, 280, 171, 41))
        self.add_flight.setObjectName("add_flight")
        self.del_flight = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.del_flight.setGeometry(QtCore.QRect(490, 340, 171, 41))
        self.del_flight.setObjectName("del_flight")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.sign = QtWidgets.QLabel(Dialog)
        self.sign.setGeometry(QtCore.QRect(28, 663, 591, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sign.setFont(font)
        self.sign.setStyleSheet("QLabel {\n"
"color: white;\n"
"}")
        self.sign.setTextFormat(QtCore.Qt.RichText)
        self.sign.setScaledContents(True)
        self.sign.setObjectName("sign")
        self.git = QtWidgets.QPushButton(Dialog)
        self.git.setGeometry(QtCore.QRect(1030, 660, 181, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./frontend/resources/git.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.git.setIcon(icon1)
        self.git.setIconSize(QtCore.QSize(64, 64))
        self.git.setObjectName("git")
        self.auth = QtWidgets.QPushButton(Dialog)
        self.auth.setGeometry(QtCore.QRect(1030, 60, 181, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./frontend/resources/auth.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.auth.setIcon(icon2)
        self.auth.setIconSize(QtCore.QSize(48, 48))
        self.auth.setObjectName("auth")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 1281, 721))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("./frontend/resources/background.jpg"))
        self.label_4.setObjectName("label_4")
        self.scrollArea_2 = QtWidgets.QScrollArea(Dialog)
        self.scrollArea_2.setGeometry(QtCore.QRect(30, 130, 1181, 521))
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1179, 519))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setGeometry(QtCore.QRect(10, 380, 1131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.week = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.week.setGeometry(QtCore.QRect(20, 410, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.week.setFont(font)
        self.week.setChecked(True)
        self.week.setObjectName("week")
        self.buttonGroup = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.week)
        self.month = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.month.setGeometry(QtCore.QRect(20, 430, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.month.setFont(font)
        self.month.setObjectName("month")
        self.buttonGroup.addButton(self.month)
        self.threem = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.threem.setGeometry(QtCore.QRect(20, 450, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.threem.setFont(font)
        self.threem.setObjectName("threem")
        self.buttonGroup.addButton(self.threem)
        self.year = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.year.setGeometry(QtCore.QRect(20, 470, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.year.setFont(font)
        self.year.setObjectName("year")
        self.buttonGroup.addButton(self.year)
        self.alltime = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.alltime.setGeometry(QtCore.QRect(20, 490, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.alltime.setFont(font)
        self.alltime.setObjectName("alltime")
        self.buttonGroup.addButton(self.alltime)
        self.leave = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.leave.setGeometry(QtCore.QRect(430, 410, 531, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.leave.setFont(font)
        self.leave.setChecked(True)
        self.leave.setObjectName("leave")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.leave)
        self.visit = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.visit.setGeometry(QtCore.QRect(430, 430, 531, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.visit.setFont(font)
        self.visit.setObjectName("visit")
        self.buttonGroup_2.addButton(self.visit)
        self.classes = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.classes.setGeometry(QtCore.QRect(430, 450, 531, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.classes.setFont(font)
        self.classes.setObjectName("classes")
        self.buttonGroup_2.addButton(self.classes)
        self.transp = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.transp.setGeometry(QtCore.QRect(430, 470, 531, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.transp.setFont(font)
        self.transp.setObjectName("transp")
        self.buttonGroup_2.addButton(self.transp)
        self.graph = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.graph.setGeometry(QtCore.QRect(1030, 470, 141, 41))
        self.graph.setObjectName("graph")
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line.setGeometry(QtCore.QRect(10, 360, 1161, 31))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 561, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setGeometry(QtCore.QRect(590, 10, 581, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setGeometry(QtCore.QRect(10, 60, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.tr_name = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.tr_name.setGeometry(QtCore.QRect(200, 60, 371, 31))
        self.tr_name.setObjectName("tr_name")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setGeometry(QtCore.QRect(10, 100, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setGeometry(QtCore.QRect(10, 140, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.seats = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_2)
        self.seats.setGeometry(QtCore.QRect(200, 140, 81, 31))
        self.seats.setMaximum(99999)
        self.seats.setObjectName("seats")
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_13.setGeometry(QtCore.QRect(590, 60, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.tick_name = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.tick_name.setGeometry(QtCore.QRect(800, 60, 371, 31))
        self.tick_name.setObjectName("tick_name")
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_2.setGeometry(QtCore.QRect(10, 170, 1161, 31))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_3.setGeometry(QtCore.QRect(575, 10, 21, 161))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.add_tr = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.add_tr.setGeometry(QtCore.QRect(430, 130, 141, 41))
        self.add_tr.setObjectName("add_tr")
        self.add_tick = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.add_tick.setGeometry(QtCore.QRect(1030, 130, 141, 41))
        self.add_tick.setObjectName("add_tick")
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_14.setGeometry(QtCore.QRect(10, 190, 1161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.add_trip = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.add_trip.setGeometry(QtCore.QRect(1030, 320, 141, 41))
        self.add_trip.setObjectName("add_trip")
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_15.setGeometry(QtCore.QRect(10, 230, 55, 61))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("./frontend/resources/from.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_16.setGeometry(QtCore.QRect(10, 300, 55, 61))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("./frontend/resources/to.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.from_line = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.from_line.setGeometry(QtCore.QRect(80, 250, 291, 31))
        self.from_line.setObjectName("from_line")
        self.to_line = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.to_line.setGeometry(QtCore.QRect(80, 330, 291, 31))
        self.to_line.setObjectName("to_line")
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_17.setGeometry(QtCore.QRect(80, 230, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_18.setGeometry(QtCore.QRect(80, 310, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.dep_date = QtWidgets.QDateTimeEdit(self.scrollAreaWidgetContents_2)
        self.dep_date.setGeometry(QtCore.QRect(380, 250, 141, 31))
        self.dep_date.setObjectName("dep_date")
        self.arr_date = QtWidgets.QDateTimeEdit(self.scrollAreaWidgetContents_2)
        self.arr_date.setGeometry(QtCore.QRect(380, 330, 141, 31))
        self.arr_date.setObjectName("arr_date")
        self.dist = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_2)
        self.dist.setGeometry(QtCore.QRect(550, 251, 131, 31))
        self.dist.setMaximum(99999)
        self.dist.setObjectName("dist")
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_19.setGeometry(QtCore.QRect(550, 230, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.price = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_2)
        self.price.setGeometry(QtCore.QRect(550, 331, 131, 31))
        self.price.setMaximum(99999)
        self.price.setObjectName("price")
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_20.setGeometry(QtCore.QRect(550, 310, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.tr_name_2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.tr_name_2.setGeometry(QtCore.QRect(700, 250, 311, 31))
        self.tr_name_2.setObjectName("tr_name_2")
        self.tick_name_2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.tick_name_2.setGeometry(QtCore.QRect(700, 330, 311, 31))
        self.tick_name_2.setObjectName("tick_name_2")
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setGeometry(QtCore.QRect(700, 230, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_22.setGeometry(QtCore.QRect(700, 310, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.kind_of_tr = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.kind_of_tr.setGeometry(QtCore.QRect(200, 100, 201, 31))
        self.kind_of_tr.setObjectName("kind_of_tr")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.label_4.raise_()
        self.sign.raise_()
        self.git.raise_()
        self.auth.raise_()
        self.scrollArea.raise_()
        self.scrollArea_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TicketBase - Main Window (User)"))
        self.label.setText(_translate("Dialog", "From:"))
        self.label_2.setText(_translate("Dialog", "To:"))
        self.label_3.setText(_translate("Dialog", "Departure date:"))
        self.part.setText(_translate("Dialog", "Part 1"))
        self.label_10.setText(_translate("Dialog", "Type of transport:"))
        self.label_11.setText(_translate("Dialog", "Class:"))
        self.search.setText(_translate("Dialog", "Search"))
        self.back_button.setText(_translate("Dialog", "Back"))
        self.next_button.setText(_translate("Dialog", "Next"))
        self.add_flight.setText(_translate("Dialog", "Attach"))
        self.del_flight.setText(_translate("Dialog", "Detach"))
        self.sign.setText(_translate("Dialog", "Saint-Petersburg, 2020"))
        self.git.setText(_translate("Dialog", "Project link"))
        self.auth.setText(_translate("Dialog", "Authorization"))
        self.label_7.setText(_translate("Dialog", "Statistics:"))
        self.week.setText(_translate("Dialog", "Week"))
        self.month.setText(_translate("Dialog", "Month"))
        self.threem.setText(_translate("Dialog", "3 months"))
        self.year.setText(_translate("Dialog", "Year"))
        self.alltime.setText(_translate("Dialog", "All time"))
        self.leave.setText(_translate("Dialog", "Top cities to leave"))
        self.visit.setText(_translate("Dialog", "Top cities to visit"))
        self.classes.setText(_translate("Dialog", "Classes statistics"))
        self.transp.setText(_translate("Dialog", "Popularity of transport types"))
        self.graph.setText(_translate("Dialog", "Get graph"))
        self.label_5.setText(_translate("Dialog", "Transport:"))
        self.label_6.setText(_translate("Dialog", "Ticket:"))
        self.label_8.setText(_translate("Dialog", "Name:"))
        self.label_9.setText(_translate("Dialog", "Kind of transport:"))
        self.label_12.setText(_translate("Dialog", "Number of seats:"))
        self.label_13.setText(_translate("Dialog", "Name of class:"))
        self.add_tr.setText(_translate("Dialog", "Add transport"))
        self.add_tick.setText(_translate("Dialog", "Add ticket:"))
        self.label_14.setText(_translate("Dialog", "Trip:"))
        self.add_trip.setText(_translate("Dialog", "Add trip"))
        self.label_17.setText(_translate("Dialog", "From:"))
        self.label_18.setText(_translate("Dialog", "To:"))
        self.label_19.setText(_translate("Dialog", "Distance, km:"))
        self.label_20.setText(_translate("Dialog", "Price, rub.:"))
        self.label_21.setText(_translate("Dialog", "Transport:"))
        self.label_22.setText(_translate("Dialog", "Ticket:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
