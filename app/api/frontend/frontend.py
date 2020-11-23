# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from backend.backend import *
from frontend.gui_py.main_window import Ui_Dialog as main_window
from frontend.gui_py.authorization_window import Ui_Dialog as authorization_window
from frontend.gui_py.flights_window import Ui_Dialog as flights_window
from frontend.gui_py.registration_window import Ui_Dialog as registration_window


dependent_windows = {}


class MAINWIN:
    main_dialog = None
    main_ui = None


mainwin = MAINWIN


# Вспомогательные функции
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


# Обработчики эл-в гл. окна (общие)
def authorization_button():
    if dependent_windows.get('authorization'): del dependent_windows['authorization']
    auth_dialog = QtWidgets.QDialog()
    auth_ui = authorization_window()
    auth_ui.setupUi(auth_dialog)

    auth_ui.reg.clicked.connect(register_button)
    auth_ui.login.clicked.connect(login_button)

    dependent_windows['authorization'] = [auth_dialog, auth_ui]
    auth_dialog.show()


# Обработчики эл-в гл. окна (user)
def search_button():
    if dependent_windows.get('flights'): del dependent_windows['flights']
    fl_dialog = QtWidgets.QDialog()
    fl_ui = flights_window()
    fl_ui.setupUi(fl_dialog)

    dependent_windows['flights'] = [fl_dialog, fl_ui]
    fl_dialog.show()


# Обработчики эл-в гл. окна (admin)


# Обработчики эл-в окна авторизации
def register_button():
    if dependent_windows.get('registration'): del dependent_windows['registration']
    reg_dialog = QtWidgets.QDialog()
    reg_ui = registration_window()
    reg_ui.setupUi(reg_dialog)

    reg_ui.admin.clicked.connect(admin_button)
    reg_ui.user.clicked.connect(user_button)

    dependent_windows['registration'] = [reg_dialog, reg_ui]
    reg_dialog.show()


def login_button():
    if dependent_windows.get('authorization'):
        email = dependent_windows.get('authorization')[1].email_line.text()
        password = dependent_windows.get('authorization')[1].pass_line.text()
        del dependent_windows['authorization']
        if dependent_windows.get('registration'): del dependent_windows['registration']


# Обработчики эл-в окна регистрации
def admin_button():
    switch_to_admin_page()
    if dependent_windows.get('authorization'): del dependent_windows['authorization']
    if dependent_windows.get('registration'): del dependent_windows['registration']


def user_button():
    switch_to_user_page()
    if dependent_windows.get('authorization'): del dependent_windows['authorization']
    if dependent_windows.get('registration'): del dependent_windows['registration']


def start():
    app = QtWidgets.QApplication(sys.argv)
    mainwin.main_dialog = QtWidgets.QDialog()
    mainwin.main_ui = main_window()
    mainwin.main_ui.setupUi(mainwin.main_dialog)
    mainwin.main_ui.scrollArea_2.hide()

    mainwin.main_ui.auth.clicked.connect(authorization_button)
    mainwin.main_ui.search.clicked.connect(search_button)

    mainwin.main_dialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start()
