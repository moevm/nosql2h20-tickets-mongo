import pymongo
from backend import backend
from frontend.gui_py.main_window import Ui_MainWindow as  Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime


backend.clear_data()
#backend.import_data()
backend.import_database('app/api/data/data.json')


#db = pymongo.MongoClient("mongodb://db:27017/").example
#print(list(db.kind_of_transport.find({})))
#print(list(db.transport.find({})))

app = QtWidgets.QApplication(sys.argv)
main_ui = Ui_MainWindow()
win = QtWidgets.QMainWindow()
main_ui.setupUi(win)
main_ui.show()
#win.show()
sys.exit(app.exec_())