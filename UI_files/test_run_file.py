import sys

from UI_files.calenderpopup import Ui_CalenderInputDialog
from UI_files.searchDiagDerived import SearchBox
from UI_files.ButtonCalender import ButtonCalender
from UI_files.SelfLearnQLineEdit import SLQLineEdit
from UI_files.LoginForm import Ui_Dialog
from UI_files.LoginDerived import LoginBox
from PyQt5.QtWidgets import QCalendarWidget, QApplication, QDialog, QPushButton
from UI_files.Billing6 import Ui_MainWindow
from UI_files.STable import STable

# from SRC.Main import AppClass

TEST_WIDGET = STable


class WW(TEST_WIDGET):  # ,QDialog
    def __init__(self, parent):
        super(WW, self).__init__(parent)
        self.init_table(3, 3)
        # self.setupUi(self)
        self.show()
        # self.pushButton.clicked.connect()
        # self.wid=self.calendarWidget
        self.a = QPushButton(self)
        self.a.clicked.connect(self.get_row_contents)

app = QApplication(sys.argv)
# x = LoginBox()
a = QDialog()
x = WW(a)
a.show()



# QCalendarWidget().selectedDate()
# w.show()
app.exec_()

# BELOW => Login Template
# $CHECK => if it's okay to innvoke a application.exec_() instance right after
# some other MainWindow used it
# if x.approved:
#     x.destroy()
#     w = AppClass()
#     w.show()
#     app.exec_()
# # the date attribute persists in the Calender widget....
# # replace this widget in the Main Billing section date selection!
# print("selected date was ",w.end_date,w.start_date)
