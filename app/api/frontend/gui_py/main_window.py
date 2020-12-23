# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_xml/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from backend.backend import *
from frontend.gui_py.add_transp import Ui_Form as add_transp
from frontend.gui_py.add_ticket import Ui_Form as add_ticket
from frontend.gui_py.add_trip import Ui_Form as add_trip
from frontend.gui_py.add_kind_of_transp import Ui_Form as add_kind_of_transp
from frontend.gui_py.statis import Ui_Form as statis
from frontend.gui_py.trip_card import Ui_Form as trip_card


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Ui_MainWindow, self).__init__(*args, **kwargs)

    def show_admin_page(self):
        self.menuShow_user.menuAction().setVisible(False)
        self.stackedWidget.setCurrentWidget(self.admin_page)
        self.resize(1100, 500)
        self.menubar.setVisible(True)
        self.menuFile.menuAction().setVisible(True)
        self.menuShow.menuAction().setVisible(True)
        self.menuImport.menuAction().setVisible(True)
        self.menuExport.menuAction().setVisible(True)
        self.show_data_trip()
        export_database("kek")

    def show_data_kind_of_trans(self):
        data = get_kind_of_transport_data()
        self.label_4.setText("Kind of transport")
        self.tableWidget.setColumnCount(len(data['keys']))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(data['keys'])
        self.tableWidget.setFixedSize(QtCore.QSize(200, len(data['keys']) * 200))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for rowNumber in range(0, len(data['data'])):
            self.tableWidget.insertRow(rowNumber)
            for column_number in range(0, len(data['keys'])):
                self.tableWidget.setItem(rowNumber, column_number,
                                         QtWidgets.QTableWidgetItem(str(data['data'][rowNumber][column_number])))

    def show_data_ticket(self):
        data = get_ticket_data()
        print(data)
        self.label_4.setText("Ticket")
        self.tableWidget.setColumnCount(len(data['keys']))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(data['keys'])
        # self.resize(1100, 500)
        self.tableWidget.setFixedSize(QtCore.QSize(200, len(data['keys']) * 200))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for rowNumber in range(0, len(data['data'])):
            self.tableWidget.insertRow(rowNumber)
            for column_number in range(0, len(data['keys'])):
                self.tableWidget.setItem(rowNumber, column_number,
                                         QtWidgets.QTableWidgetItem(str(data['data'][rowNumber][column_number])))


    def show_data_user(self):
        data = get_user_data()
        print(data)
        self.label_4.setText("User")
        self.tableWidget.setColumnCount(len(data['keys']))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(data['keys'])
        self.tableWidget.setFixedSize(QtCore.QSize(800, len(data['data']) * 70))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for rowNumber in range(0, len(data['data'])):
            self.tableWidget.insertRow(rowNumber)
            for column_number in range(0, len(data['keys'])):
                self.tableWidget.setItem(rowNumber, column_number,
                                         QtWidgets.QTableWidgetItem(str(data['data'][rowNumber][column_number])))

    def show_data_transpor(self):
        data = get_transp_data()
        self.label_4.setText("Transport")
        self.tableWidget.setColumnCount(len(data['keys']))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(data['keys'])
        # self.resize(1100, 500)
        self.tableWidget.setFixedSize(QtCore.QSize(400, len(data['keys']) * 80))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for rowNumber in range(0, len(data['data'])):
            self.tableWidget.insertRow(rowNumber)
            for column_number in range(0, len(data['keys'])):
                self.tableWidget.setItem(rowNumber, column_number,
                                         QtWidgets.QTableWidgetItem(str(data['data'][rowNumber][column_number])))

    def closeEvent(self, event):
        result = QtWidgets.QMessageBox.question(self,
                                                "Confirm Exit...",
                                                "Are you sure you want to exit ?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        event.ignore()

        if result == QtWidgets.QMessageBox.Yes:
            event.accept()

    def show_data_trip(self):
        data = get_ticket_list(None)
        self.label_4.setText("Trip")
        self.tableWidget.setColumnCount(len(data['keys']))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(data['keys'])
        # self.resize(1100, 500)
        self.tableWidget.setFixedSize(QtCore.QSize(1100, 500))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for rowNumber in range(0, len(data['trip'])):
            self.tableWidget.insertRow(rowNumber)
            for column_number in range(0, len(data['keys'])):
                self.tableWidget.setItem(rowNumber, column_number,
                                         QtWidgets.QTableWidgetItem(str(data['trip'][rowNumber][column_number])))

    def search_but_clicked(self):
        # self.search_but.clicked.connect(self.search_but_clicked)
        self.tableWidget_my_trips.hide()
        from_ = self.from_line.text()
        to_ = self.to_line.text()

        # name_tr = self.tr_name_2.currentText()
        # name_tick = self.tick_name_2.currentText()
        dep_date = self.dep_date.dateTime().toPyDateTime().strftime("%Y-%m-%dT%H:%M:%S.000Z")
        # arr_date = self.arr_date.dateTime().toPyDateTime()
        tickets = []

        for x in self.tickets_radioBut:
            if x.isChecked():
                tickets.append(str(x.text()))
        trips = find_trip(from_, to_, dep_date, tickets)
        print("Triiips", trips)

        for i in reversed(range(self.trips_search_layout.count())):
            self.trips_search_layout.itemAt(i).widget().setParent(None)

        for i in range(len(trips)):
            if any(isinstance(el, list) for el in trips[i]):
                temp = trip_card(trips[i], self.user_auth__data)
                temp.pushButton.clicked.connect(self.search_but_clicked)
                self.trips_search_layout.addRow(temp)
            else:
                temp = trip_card([trips[i]], self.user_auth__data)
                temp.pushButton.clicked.connect(self.search_but_clicked)
                self.trips_search_layout.addRow(temp)

        self.trips_search_layout_w = QtWidgets.QWidget()
        self.trips_search_layout_w.setLayout(self.trips_search_layout)
        self.search_scrollarea.setWidget(self.trips_search_layout_w)

        completer = QtWidgets.QCompleter(get_cities())
        self.from_line.setCompleter(completer)
        self.to_line.setCompleter(completer)

    def show_user_page(self):
        self.search_but.clicked.connect(self.search_but_clicked)
        self.stackedWidget.setCurrentWidget(self.user_page)
        self.menubar.setVisible(True)
        self.menuShow_user.menuAction().setVisible(True)
        self.menuExport.menuAction().setVisible(False)
        self.menuImport.menuAction().setVisible(False)
        self.menuFile.menuAction().setVisible(False)
        self.menuShow.menuAction().setVisible(False)
        self.resize(1300, 700)

        if "trips_search_layout" in locals():
            for i in reversed(range(self.trips_search_layout.count())):
                self.trips_search_layout.itemAt(i).widget().setParent(None)

        self.to_line.clear()
        self.from_line.clear()

        tickets = get_ticket_data()
        self.tickets_radioBut = []

        self.buttonGroup_2 = QtWidgets.QButtonGroup(self)
        self.buttonGroup_2.setExclusive(False)
        self.trips_search_layout_ticket = QtWidgets.QFormLayout()
        print("tickets", tickets['data'][0][0])

        for i in range(len(tickets['data'])):
            radio_but = QtWidgets.QRadioButton(str(tickets['data'][i][0]))
            self.buttonGroup_2.addButton(radio_but)
            self.tickets_radioBut.append(radio_but)
            self.trips_search_layout_ticket.addRow(radio_but)

        self.search_scrollarea_ticket_w = QtWidgets.QWidget()
        self.search_scrollarea_ticket_w.setLayout(self.trips_search_layout_ticket)
        self.search_scrollarea_ticket.setWidget(self.search_scrollarea_ticket_w)

    def show_register_page(self):
        self.stackedWidget.setCurrentWidget(self.reg_page)
        self.menubar.setVisible(False)
        self.reg_acc_email.clear()
        self.reg_acc_name.clear()
        self.reg_acc_pass.clear()
        self.reg_acc_passp.clear()
        self.reg_acc_phone.clear()
        # self.resize(500, 300)

    def cr_new_acc_butt_clicked(self):
        self.show_register_page()

    def show_auth_page(self):
        self.tableWidget_my_trips.hide()
        self.tableWidget_my_trips_shown = False
        self.auth_acc_name.clear()
        self.auth_acc_pass.clear()
        self.user_auth__data = []
        for i in reversed(range(self.trips_search_layout.count())):
            self.trips_search_layout.itemAt(i).widget().setParent(None)
        self.stackedWidget.setCurrentWidget(self.auth_page)
        self.resize(600, 280)
        self.menubar.setVisible(False)


    def reg_cancel_butt_clicked(self):
        self.show_auth_page()

    def show_add_transp_page(self):
        self.win = add_transp()
        self.win.add_tr.clicked.connect(self.show_data_transpor)

    def show_add_ticket_page(self):
        self.win = add_ticket()
        self.win.add_tick.clicked.connect(self.show_data_ticket)

    def show_add_kind_of_transp_page(self):
        self.win = add_kind_of_transp()
        self.win.add_kind.clicked.connect(self.show_data_kind_of_trans)

    def show_trip_page(self):
        self.win = add_trip()
        self.win.add_trip.clicked.connect(self.show_data_trip)

    def show_stat_page(self):
        self.win = statis()

    def login_butt_clicked(self):
        email = self.auth_acc_name.text()
        password = self.auth_acc_pass.text()
        if email == 'admin' and password == 'admin':
            self.show_admin_page()
        elif authorization(email, password):
            self.user_auth__data = {"email": email, "password": password}
            self.show_user_page()
        else:
            self.no_auth_mess = QtWidgets.QMessageBox.information(self, 'Login failed',
                                                                   'Incorrect e-mail or password entered.')

    def registration_clicked(self):
        email = self.reg_acc_email.text()
        password = self.reg_acc_pass.text()
        phone = self.reg_acc_phone.text()
        name = self.reg_acc_name.text()
        passport = self.reg_acc_passp.text()
        if (add_new_user(email, password, phone, name, passport, [])) != 'user has already exist':
            self.show_auth_page()

    def tableWidgetdouble_clicked(self, data):
        print(data.row())

    def _handleDoubleClick(self, item):
        color = item.background()
        item.setBackground(self._red if color == self._green else self._green)
        item.setSelected(False)

    def update_users_tickets(self):
        user_trips_id = get_user_trips_by_email_pass(self.user_auth__data['email'], self.user_auth__data['password'])
        if len(user_trips_id):
            data = get_ticket_list(user_trips_id)
            self.tableWidget_my_trips.setColumnCount(8)
            self.tableWidget_my_trips.setColumnCount(len(data['keys']))
            self.tableWidget_my_trips.setRowCount(0)
            self.tableWidget_my_trips.setHorizontalHeaderLabels(data['keys'])
            self.tableWidget_my_trips.setFixedSize(QtCore.QSize(1050, 160))
            self.tableWidget_my_trips.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            for rowNumber in range(0, len(data['trip'])):
                self.tableWidget_my_trips.insertRow(rowNumber)
                for column_number in range(0, len(data['keys'])):
                    self.tableWidget_my_trips.setItem(rowNumber, column_number,
                                                      QtWidgets.QTableWidgetItem(
                                                          str(data['trip'][rowNumber][column_number])))
            return True
        return False

    def actionTrip_user_clicked(self):
        if self.update_users_tickets():
            self.tableWidget_my_trips.show()
        else:
            self.no_trips_mess = QtWidgets.QMessageBox.information(self, 'No trips',
                                                                   'Please buy trip.')
        print("Clicked")

    def actionimpAlldata_clicked(self):
        self.dialog = QtWidgets.QFileDialog(self)
        self.dialog.setWindowTitle('Open file')
        self.dialog.setNameFilter('Image files (*.json)')
        self.dialog.setDirectory(QtCore.QDir.currentPath())
        self.dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        if self.dialog.exec_() == QtWidgets.QDialog.Accepted:
            clear_data()
            self.fname = str(self.dialog.selectedFiles()[0])
            import_database(self.fname)



    def actionexpAlldata_clicked(self):
        outfile = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', QtCore.QDir.currentPath() , 'Image files (*.json)')[0]
        if len(outfile):
            export_database(str(outfile))

    def set_connections(self):
        self.actionUser.triggered.connect(self.show_data_user)
        self.actionimpAlldata.triggered.connect(self.actionimpAlldata_clicked)
        self.actionexpAlldata.triggered.connect(self.actionexpAlldata_clicked)
        self.tableWidget.itemDoubleClicked.connect(self.tableWidgetdouble_clicked)
        self.registration.clicked.connect(self.registration_clicked)
        self.login_butt.clicked.connect(self.login_butt_clicked)
        self.actionStatistics.triggered.connect(self.show_stat_page)
        self.actionExit.triggered.connect(self.show_auth_page)
        self.actionTransport.triggered.connect(self.show_add_transp_page)
        self.actionTransport_2.triggered.connect(self.show_data_transpor)
        self.actionTicket.triggered.connect(self.show_add_ticket_page)
        self.actionTicket_2.triggered.connect(self.show_data_ticket)
        self.actionTrip.triggered.connect(self.show_trip_page)
        self.actionTrip_2.triggered.connect(self.show_data_trip)
        self.actionKind_of_transport.triggered.connect(self.show_add_kind_of_transp_page)
        self.actionKind_of_transport_2.triggered.connect(self.show_data_kind_of_trans)
        self.cr_new_acc_butt.clicked.connect(self.cr_new_acc_butt_clicked)
        self.reg_cancel_butt.clicked.connect(self.reg_cancel_butt_clicked)
        self.search_but.clicked.connect(self.search_but_clicked)
        self.from_line.setCompleter(QtWidgets.QCompleter(get_cities()))
        self.to_line.setCompleter(QtWidgets.QCompleter(get_cities()))
        self.actionTrip_user.triggered.connect(self.actionTrip_user_clicked)

    def setupUi(self, MainWindow):
        self.resize(936, 394)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1551, 841))
        self.stackedWidget.setObjectName("stackedWidget")
        self.auth_page = QtWidgets.QWidget()
        self.auth_page.setObjectName("auth_page")
        self.auth_acc_pass = QtWidgets.QLineEdit(self.auth_page)
        self.auth_acc_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.auth_acc_pass.setGeometry(QtCore.QRect(190, 80, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.auth_acc_pass.setFont(font)
        self.auth_acc_pass.setObjectName("auth_acc_pass")
        self.label_3 = QtWidgets.QLabel(self.auth_page)
        self.label_3.setGeometry(QtCore.QRect(20, 210, 231, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.cr_new_acc_butt = QtWidgets.QPushButton(self.auth_page)
        self.cr_new_acc_butt.setGeometry(QtCore.QRect(250, 200, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.cr_new_acc_butt.setFont(font)
        self.cr_new_acc_butt.setObjectName("cr_new_acc_butt")
        self.line = QtWidgets.QFrame(self.auth_page)
        self.line.setGeometry(QtCore.QRect(0, 180, 851, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.auth_page)
        self.label.setGeometry(QtCore.QRect(90, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.auth_page)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.login_butt = QtWidgets.QPushButton(self.auth_page)
        self.login_butt.setGeometry(QtCore.QRect(290, 130, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.login_butt.setFont(font)
        self.login_butt.setObjectName("login_butt")
        self.auth_acc_name = QtWidgets.QLineEdit(self.auth_page)
        self.auth_acc_name.setGeometry(QtCore.QRect(190, 30, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.auth_acc_name.setFont(font)
        self.auth_acc_name.setObjectName("auth_acc_name")
        self.stackedWidget.addWidget(self.auth_page)
        self.reg_page = QtWidgets.QWidget()
        self.reg_page.setObjectName("reg_page")
        self.label1 = QtWidgets.QLabel(self.reg_page)
        self.label1.setGeometry(QtCore.QRect(-50, 20, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label1.setFont(font)
        self.label1.setScaledContents(True)
        self.label1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label1.setObjectName("label1")
        self.label4 = QtWidgets.QLabel(self.reg_page)
        self.label4.setGeometry(QtCore.QRect(-50, 60, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label4.setFont(font)
        self.label4.setScaledContents(True)
        self.label4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label4.setObjectName("label4")
        self.reg_acc_email = QtWidgets.QLineEdit(self.reg_page)
        self.reg_acc_email.setGeometry(QtCore.QRect(140, 20, 271, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.reg_acc_email.setFont(font)
        self.reg_acc_email.setObjectName("reg_acc_email")
        self.label3 = QtWidgets.QLabel(self.reg_page)
        self.label3.setGeometry(QtCore.QRect(-50, 180, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label3.setFont(font)
        self.label3.setScaledContents(True)
        self.label3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label3.setObjectName("label3")
        self.reg_acc_name = QtWidgets.QLineEdit(self.reg_page)
        self.reg_acc_name.setGeometry(QtCore.QRect(140, 140, 271, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.reg_acc_name.setFont(font)
        self.reg_acc_name.setText("")
        self.reg_acc_name.setObjectName("reg_acc_name")
        self.reg_acc_pass = QtWidgets.QLineEdit(self.reg_page)
        self.reg_acc_pass.setGeometry(QtCore.QRect(140, 60, 271, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.reg_acc_pass.setFont(font)
        self.reg_acc_pass.setText("")
        self.reg_acc_pass.setObjectName("reg_acc_pass")
        self.reg_acc_passp = QtWidgets.QLineEdit(self.reg_page)
        self.reg_acc_passp.setGeometry(QtCore.QRect(140, 180, 271, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.reg_acc_passp.setFont(font)
        self.reg_acc_passp.setText("")
        self.reg_acc_passp.setObjectName("reg_acc_passp")
        self.label2 = QtWidgets.QLabel(self.reg_page)
        self.label2.setGeometry(QtCore.QRect(-50, 140, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label2.setFont(font)
        self.label2.setScaledContents(True)
        self.label2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label2.setObjectName("label2")
        self.label5 = QtWidgets.QLabel(self.reg_page)
        self.label5.setGeometry(QtCore.QRect(-50, 100, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label5.setFont(font)
        self.label5.setScaledContents(True)
        self.label5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label5.setObjectName("label5")
        self.reg_acc_phone = QtWidgets.QLineEdit(self.reg_page)
        self.reg_acc_phone.setGeometry(QtCore.QRect(140, 100, 271, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.reg_acc_phone.setFont(font)
        self.reg_acc_phone.setObjectName("reg_acc_phone")
        self.registration = QtWidgets.QPushButton(self.reg_page)
        self.registration.setGeometry(QtCore.QRect(260, 220, 141, 41))
        self.registration.setObjectName("registration")
        self.reg_cancel_butt = QtWidgets.QPushButton(self.reg_page)
        self.reg_cancel_butt.setGeometry(QtCore.QRect(110, 220, 141, 41))
        self.reg_cancel_butt.setObjectName("reg_cancel_butt")
        self.stackedWidget.addWidget(self.reg_page)
        self.admin_page = QtWidgets.QWidget()
        self.admin_page.setObjectName("admin_page")
        self.tableWidget = QtWidgets.QTableWidget(self.admin_page)
        self.tableWidget.setGeometry(QtCore.QRect(30, 50, 801, 521))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_4 = QtWidgets.QLabel(self.admin_page)
        self.label_4.setGeometry(QtCore.QRect(380, 25, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.admin_page)
        self.user_page = QtWidgets.QWidget()
        self.user_page.setObjectName("user_page")
        self.stackedWidget.addWidget(self.user_page)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 936, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuShow = QtWidgets.QMenu(self.menubar)
        self.menuShow.setObjectName("menuShow")

        self.menuExport = QtWidgets.QMenu(self.menubar)
        self.menuExport.setObjectName("menuExport")

        self.menuImport = QtWidgets.QMenu(self.menubar)
        self.menuImport.setObjectName("menuImport")

        self.menuShow_user = QtWidgets.QMenu(self.menubar)
        self.menuShow_user.setObjectName("menuTrips")

        self.menuAccount = QtWidgets.QMenu(self.menubar)
        self.menuAccount.setObjectName("menuAccount")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionTransport = QtWidgets.QAction(self)
        self.actionTransport.setObjectName("actionTransport")

        self.actionUser = QtWidgets.QAction(self)
        self.actionUser.setObjectName("actionUser")

        self.actionMyTrips = QtWidgets.QAction(self)
        self.actionMyTrips.setObjectName("actionMyTrips")

        self.actionTrip_user = QtWidgets.QAction(self)
        self.actionTrip_user.setObjectName("actionTransport")

        self.actionexpAlldata = QtWidgets.QAction(self)
        self.actionexpAlldata.setObjectName("actionTransport")

        self.actionimpAlldata = QtWidgets.QAction(self)
        self.actionimpAlldata.setObjectName("actionTransport")

        self.actionTicket = QtWidgets.QAction(self)
        self.actionTicket.setObjectName("actionTicket")
        self.actionTrip = QtWidgets.QAction(self)
        self.actionTrip.setObjectName("actionTrip")
        self.actionStatistics = QtWidgets.QAction(self)
        self.actionStatistics.setObjectName("actionStatistics")
        self.actionExit = QtWidgets.QAction(self)
        self.actionExit.setObjectName("actionExit")
        self.actionKind_of_transport = QtWidgets.QAction(self)
        self.actionKind_of_transport.setObjectName("actionKind_of_transport")
        self.actionTransport_2 = QtWidgets.QAction(self)
        self.actionTransport_2.setObjectName("actionTransport_2")
        self.actionTicket_2 = QtWidgets.QAction(self)
        self.actionTicket_2.setObjectName("actionTicket_2")
        self.actionTrip_2 = QtWidgets.QAction(self)
        self.actionTrip_2.setObjectName("actionTrip_2")
        self.actionKind_of_transport_2 = QtWidgets.QAction(self)
        self.actionKind_of_transport_2.setObjectName("actionKind_of_transport_2")
        self.menuFile.addAction(self.actionTransport)

        self.menuFile.addAction(self.actionTicket)
        self.menuFile.addAction(self.actionTrip)
        self.menuFile.addAction(self.actionKind_of_transport)
        self.menuShow.addAction(self.actionStatistics)
        self.menuShow.addAction(self.actionUser)

        self.menuShow.addAction(self.actionTransport_2)
        self.menuShow.addAction(self.actionTicket_2)
        self.menuShow.addAction(self.actionTrip_2)
        self.menuShow.addAction(self.actionKind_of_transport_2)
        self.menuShow_user.addAction(self.actionTrip_user)
        self.menuExport.addAction(self.actionexpAlldata)
        self.menuImport.addAction(self.actionimpAlldata)
        self.menuAccount.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuShow.menuAction())
        self.menubar.addAction(self.menuShow_user.menuAction())
        self.menubar.addAction(self.menuExport.menuAction())
        self.menubar.addAction(self.menuImport.menuAction())
        self.menubar.addAction(self.menuAccount.menuAction())

        self.tableWidget_my_trips = QtWidgets.QTableWidget()
        # self.arr_date = QtWidgets.QDateTimeEdit(self.user_page)
        # self.arr_date.setGeometry(QtCore.QRect(378, 120, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        # self.arr_date.setFont(font)
        # self.arr_date.setObjectName("arr_date")
        self.label_16 = QtWidgets.QLabel(self.user_page)
        self.label_16.setGeometry(QtCore.QRect(8, 133, 55, 61))
        self.label_16.setText("")
        self.label_16.setPixmap(
            QtGui.QPixmap("gui_py\\../../../../../double/nosql2h20-tickets-mongo/app/api/frontend/resources/to.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.dep_date = QtWidgets.QDateEdit(self.user_page)
        self.dep_date.setGeometry(QtCore.QRect(378, 40, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.dep_date.setFont(font)
        self.dep_date.setObjectName("dep_date")
        self.label_15 = QtWidgets.QLabel(self.user_page)
        self.label_15.setGeometry(QtCore.QRect(8, 63, 55, 61))
        self.label_15.setText("")
        self.label_15.setPixmap(
            QtGui.QPixmap("gui_xml\\../../../../../double/nosql2h20-tickets-mongo/app/api/frontend/resources/from.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.user_page)
        self.label_17.setGeometry(QtCore.QRect(78, 20, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        # self.label_21 = QtWidgets.QLabel(self.user_page)
        # self.label_21.setGeometry(QtCore.QRect(548, 20, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        # self.label_21.setFont(font)
        # self.label_21.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        # self.label_21.setObjectName("label_21")
        self.from_line = QtWidgets.QLineEdit(self.user_page)
        self.from_line.setGeometry(QtCore.QRect(78, 40, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.from_line.setFont(font)
        self.from_line.setObjectName("from_line")
        self.label_22 = QtWidgets.QLabel(self.user_page)
        self.label_22.setGeometry(QtCore.QRect(548, 20, 60, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.label_18 = QtWidgets.QLabel(self.user_page)
        self.label_18.setGeometry(QtCore.QRect(78, 90, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.to_line = QtWidgets.QLineEdit(self.user_page)
        self.to_line.setGeometry(QtCore.QRect(78, 120, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.to_line.setFont(font)
        self.to_line.setObjectName("to_line")
        self.search_but = QtWidgets.QPushButton(self.user_page)
        self.search_but.setGeometry(QtCore.QRect(1000, 70, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.search_but.setFont(font)
        self.search_but.setObjectName("pushButton")

        self.trips_search_layout = QtWidgets.QFormLayout()
        self.set_connections()
        self.search_scrollarea = QtWidgets.QScrollArea(self.user_page)
        self.search_scrollarea.setGeometry(78, 170, 1200, 500)

        self.search_scrollarea_ticket = QtWidgets.QScrollArea(self.user_page)
        self.search_scrollarea_ticket.setGeometry(630, 20, 150, 140)
        self.show_auth_page()
        # self.show_user_page()
        # self.show_admin_page()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # MainWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Don\'t have a account ?"))
        self.cr_new_acc_butt.setText(_translate("MainWindow", "CREATE A NEW ACCOUNT"))
        self.label.setText(_translate("MainWindow", "E-mail"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.login_butt.setText(_translate("MainWindow", "LOGIN"))
        self.label1.setText(_translate("MainWindow", "E-mail"))
        self.label4.setText(_translate("MainWindow", "Password"))
        self.label3.setText(_translate("MainWindow", "Passport"))
        self.label2.setText(_translate("MainWindow", "Full name"))
        self.label5.setText(_translate("MainWindow", "Phone number"))
        self.registration.setText(_translate("MainWindow", "REGISTER"))
        self.reg_cancel_butt.setText(_translate("MainWindow", "CANCEL"))
        self.label_4.setText(_translate("MainWindow", "Data"))
        self.menuFile.setTitle(_translate("MainWindow", "Add"))
        self.menuShow.setTitle(_translate("MainWindow", "Show"))
        self.menuShow_user.setTitle(_translate("MainWindow", "Show"))
        self.menuExport.setTitle(_translate("MainWindow", "Export"))
        self.menuImport.setTitle(_translate("MainWindow", "Import"))
        self.menuAccount.setTitle(_translate("MainWindow", "Account"))
        self.actionTransport.setText(_translate("MainWindow", "Transport"))
        self.actionUser.setText(_translate("MainWindow", "User"))
        self.actionTrip_user.setText(_translate("MainWindow", "My trips"))
        self.actionexpAlldata.setText(_translate("MainWindow", "All data"))
        self.actionimpAlldata.setText(_translate("MainWindow", "All data"))
        self.actionTicket.setText(_translate("MainWindow", "Ticket"))
        self.actionTrip.setText(_translate("MainWindow", "Trip"))
        self.actionStatistics.setText(_translate("MainWindow", "Statistics"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionKind_of_transport.setText(_translate("MainWindow", "Kind of transport"))
        self.actionTransport_2.setText(_translate("MainWindow", "Transport"))
        self.actionTicket_2.setText(_translate("MainWindow", "Ticket"))
        self.actionTrip_2.setText(_translate("MainWindow", "Trip"))
        self.actionKind_of_transport_2.setText(_translate("MainWindow", "Kind of transport"))

        self.label_17.setText(_translate("MainWindow", "From:"))
        # self.label_21.setText(_translate("MainWindow", "Transport:"))
        self.label_22.setText(_translate("MainWindow", "Ticket:"))
        self.label_18.setText(_translate("MainWindow", "To:"))
        self.search_but.setText(_translate("MainWindow", "Search"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
