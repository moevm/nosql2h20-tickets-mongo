# -*- coding: utf-8 -*-


import sys, os, pymongo, numpy
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from backend.backend import *
from frontend.gui_py.main_window import Ui_Dialog as main_window
from frontend.gui_py.authorization_window import Ui_Dialog as authorization_window
from frontend.gui_py.flights_window import Ui_Dialog as flights_window
from frontend.gui_py.registration_window import Ui_Dialog as registration_window
import datetime

dependent_windows = {}
user_data = [None, None]


class TRIPPART:
    from_ = None
    to_ = None
    date = None
    types = [False, False]
    classes = [False, False, False]


class MAINWIN:
    main_dialog = None
    main_ui = None
    user_trip = []
    current_trip = 0


mainwin = MAINWIN


# Вспомогательные функции
def updateWidgets():
    pass


def updateInfo():
    pass


def disable_user_trip_part():
    if mainwin.current_trip == 0:
        mainwin.main_ui.back_button.setDisabled(True)
    else:
        mainwin.main_ui.back_button.setDisabled(False)
    mainwin.main_ui.add_flight.setDisabled(False)
    mainwin.main_ui.del_flight.setDisabled(True)
    mainwin.main_ui.next_button.setDisabled(True)
    mainwin.main_ui.part.setText('')
    mainwin.main_ui.label.setDisabled(True)
    mainwin.main_ui.label_2.setDisabled(True)
    mainwin.main_ui.label_3.setDisabled(True)
    mainwin.main_ui.label_10.setDisabled(True)
    mainwin.main_ui.label_11.setDisabled(True)
    mainwin.main_ui.from_list.setDisabled(True)
    mainwin.main_ui.to_list.setDisabled(True)
    mainwin.main_ui.dateEdit.setDisabled(True)
    mainwin.main_ui.types.setDisabled(True)
    mainwin.main_ui.classes.setChecked(True)


def enable_user_trip_part():
    if mainwin.current_trip == 0:
        mainwin.main_ui.back_button.setDisabled(True)
    else:
        mainwin.main_ui.back_button.setDisabled(False)
    mainwin.main_ui.add_flight.setDisabled(True)
    if mainwin.current_trip == (len(mainwin.user_trip) - 1):
        mainwin.main_ui.del_flight.setDisabled(False)
    else:
        mainwin.main_ui.del_flight.setDisabled(True)
    mainwin.main_ui.next_button.setDisabled(False)
    mainwin.main_ui.part.setText('Part ' + str(mainwin.current_trip + 1))
    mainwin.main_ui.label.setDisabled(False)
    mainwin.main_ui.label_2.setDisabled(False)
    mainwin.main_ui.label_3.setDisabled(False)
    mainwin.main_ui.label_10.setDisabled(False)
    mainwin.main_ui.label_11.setDisabled(False)
    mainwin.main_ui.from_list.setDisabled(False)
    mainwin.main_ui.to_list.setDisabled(False)
    mainwin.main_ui.dateEdit.setDisabled(False)
    mainwin.main_ui.types.setDisabled(False)
    mainwin.main_ui.classes.setDisabled(False)


def switch_to_admin_page():
    if mainwin.main_ui:
        mainwin.main_ui.scrollArea.hide()
        mainwin.main_ui.scrollArea_2.show()
        _translate = QtCore.QCoreApplication.translate
        mainwin.main_dialog.setWindowTitle(_translate("Dialog", "TicketBase - Main Window (Administrator)"))


def switch_to_user_page():
    if mainwin.main_ui:
        mainwin.main_ui.scrollArea_2.hide()
        mainwin.main_ui.scrollArea.show()
        _translate = QtCore.QCoreApplication.translate
        mainwin.main_dialog.setWindowTitle(_translate("Dialog", "TicketBase - Main Window (User)"))
        mainwin.user_trip.clear()
        mainwin.current_trip = 0


# Обработчики эл-в гл. окна (общие)
def authorization_button():
    if dependent_windows.get('authorization'): del dependent_windows['authorization']
    auth_dialog = QtWidgets.QDialog()
    auth_ui = authorization_window()
    auth_ui.setupUi(auth_dialog)

    auth_ui.reg.clicked.connect(register_button)
    auth_ui.login.clicked.connect(login_button)
    auth_ui.logout.clicked.connect(logout_button)

    dependent_windows['authorization'] = [auth_dialog, auth_ui]
    auth_dialog.show()


def project_link_button():
    os.system('start https://github.com/moevm/nosql2h20-tickets-mongo')


# Обработчики эл-в гл. окна (user)
def search_button():
    if (len(mainwin.user_trip) > 0) and (mainwin.current_trip != len(mainwin.user_trip)): updateInfo()

    if dependent_windows.get('flights'): del dependent_windows['flights']
    fl_dialog = QtWidgets.QDialog()
    fl_ui = flights_window()
    fl_ui.setupUi(fl_dialog)

    dependent_windows['flights'] = [fl_dialog, fl_ui]
    fl_dialog.show()


def back_button():
    if (len(mainwin.user_trip) > 0) and (mainwin.current_trip != len(mainwin.user_trip)): updateInfo()
    mainwin.current_trip -= 1
    updateWidgets()
    enable_user_trip_part()


def next_button():
    if (len(mainwin.user_trip) > 0) and (mainwin.current_trip != len(mainwin.user_trip)): updateInfo()
    mainwin.current_trip += 1
    if mainwin.current_trip == len(mainwin.user_trip):
        disable_user_trip_part()
    else:
        updateWidgets()
        enable_user_trip_part()


def add_button():
    new_part = TRIPPART
    mainwin.user_trip.append(new_part)
    enable_user_trip_part()


def del_button():
    mainwin.user_trip.pop(len(mainwin.user_trip) - 1)
    disable_user_trip_part()


# Обработчики эл-в гл. окна (admin)
def add_transport_button():
    name = mainwin.main_ui.tr_name.text()
    kind_of_transport = mainwin.main_ui.kind_of_tr.currentText()
    number_of_seats = int(mainwin.main_ui.seats.value())
    add_new_transport(name, kind_of_transport, number_of_seats)
    mainwin.main_ui.tr_name_2.clear()
    mainwin.main_ui.tr_name_2.addItems(get_transport())


def add_ticket_button():
    name = mainwin.main_ui.tick_name.text()
    add_new_ticket(name)
    mainwin.main_ui.tick_name_2.clear()
    mainwin.main_ui.tick_name_2.addItems(get_tickets())


def add_kind_button():
    name = mainwin.main_ui.tick_name_3.text()
    add_kind_of_transport(name)
    mainwin.main_ui.kind_of_tr.clear()
    mainwin.main_ui.kind_of_tr.addItems(get_kind_of_transport_list())


def add_trip_button():
    from_ = mainwin.main_ui.from_line.text()
    to_ = mainwin.main_ui.to_line.text()
    dist = int(mainwin.main_ui.dist.value())
    price = int(mainwin.main_ui.price.value())
    name_tr = mainwin.main_ui.tr_name_2.currentText()
    name_tick = mainwin.main_ui.tick_name_2.currentText()
    dep_date = mainwin.main_ui.dep_date.dateTime().toPyDateTime()
    arr_date = mainwin.main_ui.arr_date.dateTime().toPyDateTime()
    add_new_trip(from_, to_, dep_date, arr_date, name_tr, dist, price, name_tick)
    completer = QtWidgets.QCompleter(get_cities())
    mainwin.main_ui.from_line.setCompleter(completer)
    mainwin.main_ui.to_line.setCompleter(completer)


def get_graph_button():
    now = datetime.datetime.now()
    start_date = None
    if mainwin.main_ui.week.isChecked():
        start_date = now - datetime.timedelta(days=datetime.date.today().weekday(), weeks=1)
    if mainwin.main_ui.month.isChecked():
            start_date = now - relativedelta(months=1)
    if mainwin.main_ui.threem.isChecked():
        start_date = now - relativedelta(months=3)
    if mainwin.main_ui.year.isChecked():
        start_date = now - relativedelta(years=1)
    if mainwin.main_ui.alltime.isChecked(): now = None

    trips = stat(start_date, now)

    if mainwin.main_ui.leave.isChecked():
        cities = get_cities()
        heights = numpy.zeros(len(cities))
        for i in range(len(trips)):
            heights[cities.index(trips[i]['from'])] += 1
        x = numpy.arange(len(cities))
        plt.bar(x, height=heights)
        plt.xticks(x, cities)
        plt.title('Top cities to leave')

    if mainwin.main_ui.visit.isChecked():
        cities = get_cities()
        heights = numpy.zeros(len(cities))
        for i in range(len(trips)):
            heights[cities.index(trips[i]['to'])] += 1
        x = numpy.arange(len(cities))
        plt.bar(x, height=heights)
        plt.xticks(x, cities)
        plt.title('Top cities to visit')

    if mainwin.main_ui.classes.isChecked():
        classes = get_tickets()
        heights = numpy.zeros(len(classes))
        for i in range(len(trips)):
            heights[classes.index(get_ticket_type_name(trips[i]['ticket_id']))] += 1
        x = numpy.arange(len(classes))
        plt.bar(x, height=heights)
        plt.xticks(x, classes)
        plt.title('Classes statistics')

    if mainwin.main_ui.transp.isChecked():
        types = get_transport()
        heights = numpy.zeros(len(types))
        for i in range(len(trips)):
            heights[types.index(get_transport_type_name(trips[i]['transport_id']))] += 1
        x = numpy.arange(len(types))
        plt.bar(x, height=heights)
        plt.xticks(x, types)
        plt.title('Popularity of flights')

    plt.grid()
    plt.show()


# Обработчики эл-в окна авторизации
def register_button():
    if dependent_windows.get('registration'): del dependent_windows['registration']
    reg_dialog = QtWidgets.QDialog()
    reg_ui = registration_window()
    reg_ui.setupUi(reg_dialog)

    reg_ui.registration.clicked.connect(registration_button)

    dependent_windows['registration'] = [reg_dialog, reg_ui]
    reg_dialog.show()


def login_button():
    if dependent_windows.get('authorization'):
        email = dependent_windows.get('authorization')[1].email_line.text()
        password = dependent_windows.get('authorization')[1].pass_line.text()
        if email == 'admin' and password == 'admin':
            switch_to_admin_page()
            del dependent_windows['authorization']
            if dependent_windows.get('registration'): del dependent_windows['registration']
        else:
            switch_to_user_page()
        if authorization(email, password):
            user_data[0] = email;
            user_data[1] = password
            del dependent_windows['authorization']
            if dependent_windows.get('registration'): del dependent_windows['registration']


def logout_button():
    switch_to_user_page()
    user_data[0] = None;
    user_data[1] = None
    if dependent_windows.get('authorization'): del dependent_windows['authorization']
    if dependent_windows.get('registration'): del dependent_windows['registration']


# Обработчики эл-в окна регистрации
def registration_button():
    switch_to_user_page()
    if dependent_windows.get('registration'):
        email = dependent_windows.get('registration')[1].email_line.text()
        password = dependent_windows.get('registration')[1].pass_line.text()
        phone = dependent_windows.get('registration')[1].phone_line.text()
        name = dependent_windows.get('registration')[1].name_line.text()
        passport = dependent_windows.get('registration')[1].passp_line.text()
        if (add_new_user(email, password, phone, name, passport)) != 'user has already exist':
            user_data[0] = email;
            user_data[1] = password
            del dependent_windows['registration']
            if dependent_windows.get('authorization'): del dependent_windows['authorization']


def start():
    app = QtWidgets.QApplication(sys.argv)
    mainwin.main_dialog = QtWidgets.QDialog()
    mainwin.main_ui = main_window()
    mainwin.main_ui.setupUi(mainwin.main_dialog)
    mainwin.main_ui.scrollArea_2.hide()

    mainwin.main_ui.auth.clicked.connect(authorization_button)
    mainwin.main_ui.search.clicked.connect(search_button)
    mainwin.main_ui.back_button.clicked.connect(back_button)
    mainwin.main_ui.next_button.clicked.connect(next_button)
    mainwin.main_ui.add_flight.clicked.connect(add_button)
    mainwin.main_ui.del_flight.clicked.connect(del_button)
    mainwin.main_ui.add_tr.clicked.connect(add_transport_button)
    mainwin.main_ui.add_tick.clicked.connect(add_ticket_button)
    mainwin.main_ui.add_kind.clicked.connect(add_kind_button)
    mainwin.main_ui.add_trip.clicked.connect(add_trip_button)
    mainwin.main_ui.graph.clicked.connect(get_graph_button)
    mainwin.main_ui.git.clicked.connect(project_link_button)

    mainwin.main_ui.tr_name_2.addItems(get_transport())
    mainwin.main_ui.tick_name_2.addItems(get_tickets())
    mainwin.main_ui.kind_of_tr.addItems(get_kind_of_transport_list())
    
    mainwin.main_ui.from_line.setCompleter(QtWidgets.QCompleter(get_cities()))
    mainwin.main_ui.to_line.setCompleter(QtWidgets.QCompleter(get_cities()))

    disable_user_trip_part()

    mainwin.main_dialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start()
