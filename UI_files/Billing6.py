# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Biiling_project_UI2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1888, 1029)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainTabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.MainTabWidget.setGeometry(QtCore.QRect(10, 0, 1881, 981))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.MainTabWidget.setFont(font)
        self.MainTabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.MainTabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.MainTabWidget.setTabsClosable(False)
        self.MainTabWidget.setTabBarAutoHide(False)
        self.MainTabWidget.setObjectName("MainTabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.BotFrame = QtWidgets.QFrame(self.tab)
        self.BotFrame.setGeometry(QtCore.QRect(-1, 420, 1871, 531))
        self.BotFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BotFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BotFrame.setObjectName("BotFrame")
        self.ItemNameInput = QtWidgets.QLineEdit(self.BotFrame)
        self.ItemNameInput.setGeometry(QtCore.QRect(248, 93, 281, 31))
        self.ItemNameInput.setText("")
        self.ItemNameInput.setReadOnly(False)
        self.ItemNameInput.setObjectName("ItemNameInput")
        self.label_10 = QtWidgets.QLabel(self.BotFrame)
        self.label_10.setGeometry(QtCore.QRect(28, 90, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.BotFrame)
        self.label_11.setGeometry(QtCore.QRect(640, 92, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.QtyInput = QtWidgets.QLineEdit(self.BotFrame)
        self.QtyInput.setGeometry(QtCore.QRect(800, 92, 201, 31))
        self.QtyInput.setObjectName("QtyInput")
        self.label_20 = QtWidgets.QLabel(self.BotFrame)
        self.label_20.setGeometry(QtCore.QRect(1593, 461, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.AddItemButton = QtWidgets.QPushButton(self.BotFrame)
        self.AddItemButton.setGeometry(QtCore.QRect(1630, 95, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.AddItemButton.setFont(font)
        self.AddItemButton.setObjectName("AddItemButton")
        self.TotalAmountLabel = QtWidgets.QLabel(self.BotFrame)
        self.TotalAmountLabel.setGeometry(QtCore.QRect(1730, 460, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.TotalAmountLabel.setFont(font)
        self.TotalAmountLabel.setObjectName("TotalAmountLabel")
        self.TableAreaBottom = QtWidgets.QTableView(self.BotFrame)
        self.TableAreaBottom.setGeometry(QtCore.QRect(0, 130, 1871, 231))
        self.TableAreaBottom.setObjectName("TableAreaBottom")
        self.NewLrButton = QtWidgets.QPushButton(self.BotFrame)
        self.NewLrButton.setGeometry(QtCore.QRect(20, 410, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.NewLrButton.setFont(font)
        self.NewLrButton.setObjectName("NewLrButton")
        self.EditLrButton = QtWidgets.QPushButton(self.BotFrame)
        self.EditLrButton.setGeometry(QtCore.QRect(190, 410, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.EditLrButton.setFont(font)
        self.EditLrButton.setObjectName("EditLrButton")
        self.CancelLrButton = QtWidgets.QPushButton(self.BotFrame)
        self.CancelLrButton.setGeometry(QtCore.QRect(340, 410, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.CancelLrButton.setFont(font)
        self.CancelLrButton.setObjectName("CancelLrButton")
        self.PrintLrButton = QtWidgets.QPushButton(self.BotFrame)
        self.PrintLrButton.setGeometry(QtCore.QRect(510, 410, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.PrintLrButton.setFont(font)
        self.PrintLrButton.setObjectName("PrintLrButton")
        self.label_22 = QtWidgets.QLabel(self.BotFrame)
        self.label_22.setGeometry(QtCore.QRect(1060, 91, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.labbb = QtWidgets.QLabel(self.BotFrame)
        self.labbb.setGeometry(QtCore.QRect(1460, 380, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.labbb.setFont(font)
        self.labbb.setObjectName("labbb")
        self.llab1 = QtWidgets.QLabel(self.BotFrame)
        self.llab1.setGeometry(QtCore.QRect(1460, 420, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.llab1.setFont(font)
        self.llab1.setObjectName("llab1")
        self.label_25 = QtWidgets.QLabel(self.BotFrame)
        self.label_25.setGeometry(QtCore.QRect(700, 380, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.CNRGSTInput = QtWidgets.QLineEdit(self.BotFrame)
        self.CNRGSTInput.setGeometry(QtCore.QRect(820, 381, 211, 31))
        self.CNRGSTInput.setObjectName("CNRGSTInput")
        self.CNEGSTInput = QtWidgets.QLineEdit(self.BotFrame)
        self.CNEGSTInput.setGeometry(QtCore.QRect(820, 421, 211, 31))
        self.CNEGSTInput.setObjectName("CNEGSTInput")
        self.label_26 = QtWidgets.QLabel(self.BotFrame)
        self.label_26.setGeometry(QtCore.QRect(700, 420, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.BotFrame)
        self.label_27.setGeometry(QtCore.QRect(1070, 380, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.LRTypeInput = QtWidgets.QComboBox(self.BotFrame)
        self.LRTypeInput.setGeometry(QtCore.QRect(1270, 380, 101, 31))
        self.LRTypeInput.setObjectName("LRTypeInput")
        self.LRTypeInput.addItem("")
        self.LRTypeInput.addItem("")
        self.LRTypeInput.addItem("")
        self.LRTypeInput.setItemText(2, "")
        self.DateInput = QtWidgets.QDateTimeEdit(self.BotFrame)
        self.DateInput.setGeometry(QtCore.QRect(1654, 15, 151, 31))
        self.DateInput.setObjectName("DateInput")
        self.label_7 = QtWidgets.QLabel(self.BotFrame)
        self.label_7.setGeometry(QtCore.QRect(640, 55, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.BotFrame)
        self.label_9.setGeometry(QtCore.QRect(1524, 53, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.CNRInput = QtWidgets.QLineEdit(self.BotFrame)
        self.CNRInput.setGeometry(QtCore.QRect(250, 53, 281, 31))
        self.CNRInput.setText("")
        self.CNRInput.setReadOnly(False)
        self.CNRInput.setObjectName("CNRInput")
        self.VechicleNumInput = QtWidgets.QLineEdit(self.BotFrame)
        self.VechicleNumInput.setGeometry(QtCore.QRect(1235, 16, 171, 31))
        self.VechicleNumInput.setObjectName("VechicleNumInput")
        self.CLRNumber = QtWidgets.QLineEdit(self.BotFrame)
        self.CLRNumber.setGeometry(QtCore.QRect(1655, 55, 151, 31))
        self.CLRNumber.setText("")
        self.CLRNumber.setReadOnly(False)
        self.CLRNumber.setObjectName("CLRNumber")
        self.CNEInput = QtWidgets.QLineEdit(self.BotFrame)
        self.CNEInput.setGeometry(QtCore.QRect(801, 57, 201, 31))
        self.CNEInput.setText("")
        self.CNEInput.setReadOnly(False)
        self.CNEInput.setObjectName("CNEInput")
        self.label_4 = QtWidgets.QLabel(self.BotFrame)
        self.label_4.setGeometry(QtCore.QRect(30, 13, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_21 = QtWidgets.QLabel(self.BotFrame)
        self.label_21.setGeometry(QtCore.QRect(1060, 14, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_6 = QtWidgets.QLabel(self.BotFrame)
        self.label_6.setGeometry(QtCore.QRect(640, 13, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.BotFrame)
        self.label_5.setGeometry(QtCore.QRect(30, 53, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.BotFrame)
        self.label_8.setGeometry(QtCore.QRect(1524, 14, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.FrStationInput = QtWidgets.QLineEdit(self.BotFrame)
        self.FrStationInput.setGeometry(QtCore.QRect(250, 13, 281, 31))
        self.FrStationInput.setText("")
        self.FrStationInput.setReadOnly(False)
        self.FrStationInput.setObjectName("FrStationInput")
        self.RateInput = QtWidgets.QLineEdit(self.BotFrame)
        self.RateInput.setGeometry(QtCore.QRect(1240, 91, 201, 31))
        self.RateInput.setObjectName("RateInput")
        self.ToStationInput = QtWidgets.QLineEdit(self.BotFrame)
        self.ToStationInput.setGeometry(QtCore.QRect(800, 20, 201, 31))
        self.ToStationInput.setObjectName("ToStationInput")
        self.CrossingInput = QtWidgets.QLineEdit(self.BotFrame)
        self.CrossingInput.setGeometry(QtCore.QRect(1580, 421, 211, 31))
        self.CrossingInput.setObjectName("CrossingInput")
        self.HChargeInput = QtWidgets.QLineEdit(self.BotFrame)
        self.HChargeInput.setGeometry(QtCore.QRect(1580, 381, 211, 31))
        self.HChargeInput.setObjectName("HChargeInput")
        self.TopFrame = QtWidgets.QFrame(self.tab)
        self.TopFrame.setGeometry(QtCore.QRect(0, -10, 1871, 431))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.TopFrame.setFont(font)
        self.TopFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TopFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TopFrame.setObjectName("TopFrame")
        self.TableAreaTop = QtWidgets.QTableView(self.TopFrame)
        self.TableAreaTop.setGeometry(QtCore.QRect(0, 51, 1871, 371))
        self.TableAreaTop.setObjectName("TableAreaTop")
        self.label = QtWidgets.QLabel(self.TopFrame)
        self.label.setGeometry(QtCore.QRect(10, 12, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.CLRSearchInput = QtWidgets.QLineEdit(self.TopFrame)
        self.CLRSearchInput.setGeometry(QtCore.QRect(180, 12, 241, 31))
        self.CLRSearchInput.setText("")
        self.CLRSearchInput.setObjectName("CLRSearchInput")
        self.SearchCLRButton = QtWidgets.QPushButton(self.TopFrame)
        self.SearchCLRButton.setGeometry(QtCore.QRect(432, 12, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.SearchCLRButton.setFont(font)
        self.SearchCLRButton.setObjectName("SearchCLRButton")
        self.label_2 = QtWidgets.QLabel(self.TopFrame)
        self.label_2.setGeometry(QtCore.QRect(800, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.DateLabel = QtWidgets.QLabel(self.TopFrame)
        self.DateLabel.setGeometry(QtCore.QRect(900, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.DateLabel.setFont(font)
        self.DateLabel.setObjectName("DateLabel")
        self.label_3 = QtWidgets.QLabel(self.TopFrame)
        self.label_3.setGeometry(QtCore.QRect(1360, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.BranchComboBox = QtWidgets.QComboBox(self.TopFrame)
        self.BranchComboBox.setGeometry(QtCore.QRect(1560, 10, 101, 31))
        self.BranchComboBox.setObjectName("BranchComboBox")
        self.BranchComboBox.addItem("")
        self.BranchComboBox.addItem("")
        self.BranchComboBox.addItem("")
        self.BranchComboBox.addItem("")
        self.MainTabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.InvoiceTopFrame = QtWidgets.QFrame(self.tab_2)
        self.InvoiceTopFrame.setGeometry(QtCore.QRect(0, 0, 1861, 141))
        self.InvoiceTopFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.InvoiceTopFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.InvoiceTopFrame.setObjectName("InvoiceTopFrame")
        self.label_15 = QtWidgets.QLabel(self.InvoiceTopFrame)
        self.label_15.setGeometry(QtCore.QRect(582, 50, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        # Edited
        # self.ChangeAsButtonCalInvoice = QtWidgets.QLineEdit(self.InvoiceTopFrame)
        # self.ChangeAsButtonCalInvoice.setGeometry(QtCore.QRect(810, 50, 211, 31))
        # self.ChangeAsButtonCalInvoice.setObjectName("ChangeAsButtonCalInvoice")
        # edit -> end
        self.PrintInvoiceNumInput = QtWidgets.QLineEdit(self.InvoiceTopFrame)
        self.PrintInvoiceNumInput.setGeometry(QtCore.QRect(270, 50, 211, 31))
        self.PrintInvoiceNumInput.setObjectName("PrintInvoiceNumInput")
        self.label_17 = QtWidgets.QLabel(self.InvoiceTopFrame)
        self.label_17.setGeometry(QtCore.QRect(6, 50, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        # editied
        # self.comboBox = QtWidgets.QComboBox(self.InvoiceTopFrame)
        # self.comboBox.setGeometry(QtCore.QRect(270, 100, 211, 31))
        # self.comboBox.setObjectName("comboBox")
        self.InvoiceStationInput = QtWidgets.QLineEdit(self.InvoiceTopFrame)
        self.InvoiceStationInput.setGeometry(QtCore.QRect(270, 100, 211, 31))
        # edit -> end
        self.label_40 = QtWidgets.QLabel(self.InvoiceTopFrame)
        self.label_40.setGeometry(QtCore.QRect(10, 99, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.InvoiceTopFrame)
        self.label_41.setGeometry(QtCore.QRect(580, 100, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.InvoiceVechicleNumInput = QtWidgets.QLineEdit(self.InvoiceTopFrame)
        self.InvoiceVechicleNumInput.setGeometry(QtCore.QRect(810, 100, 211, 31))
        self.InvoiceVechicleNumInput.setObjectName("InvoiceVechicleNumInput")
        self.InvoiceBranchCode = QtWidgets.QComboBox(self.InvoiceTopFrame)
        self.InvoiceBranchCode.setGeometry(QtCore.QRect(1260, 50, 101, 31))
        self.InvoiceBranchCode.setObjectName("InvoiceBranchCode")
        self.InvoiceBranchCode.addItem("")
        self.InvoiceBranchCode.addItem("")
        self.InvoiceBranchCode.addItem("")
        self.InvoiceBranchCode.addItem("")
        self.label_45 = QtWidgets.QLabel(self.InvoiceTopFrame)
        self.label_45.setGeometry(QtCore.QRect(1060, 50, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.InvoiceBotFrame = QtWidgets.QFrame(self.tab_2)
        self.InvoiceBotFrame.setGeometry(QtCore.QRect(0, 140, 1861, 801))
        self.InvoiceBotFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.InvoiceBotFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.InvoiceBotFrame.setObjectName("InvoiceBotFrame")
        self.label_12 = QtWidgets.QLabel(self.InvoiceBotFrame)
        self.label_12.setGeometry(QtCore.QRect(10, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.LRSearchInvoiceButton = QtWidgets.QPushButton(self.InvoiceBotFrame)
        self.LRSearchInvoiceButton.setGeometry(QtCore.QRect(432, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.LRSearchInvoiceButton.setFont(font)
        self.LRSearchInvoiceButton.setObjectName("LRSearchInvoiceButton")
        self.LRInvoiceSearchInput = QtWidgets.QLineEdit(self.InvoiceBotFrame)
        self.LRInvoiceSearchInput.setGeometry(QtCore.QRect(180, 10, 241, 31))
        self.LRInvoiceSearchInput.setText("")
        self.LRInvoiceSearchInput.setObjectName("LRInvoiceSearchInput")
        self.InvoiceMainTableView = QtWidgets.QTableView(self.InvoiceBotFrame)
        self.InvoiceMainTableView.setGeometry(QtCore.QRect(0, 50, 1861, 451))
        self.InvoiceMainTableView.setObjectName("InvoiceMainTableView")
        self.InvoicePrintButton = QtWidgets.QPushButton(self.InvoiceBotFrame)
        self.InvoicePrintButton.setGeometry(QtCore.QRect(1710, 520, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.InvoicePrintButton.setFont(font)
        self.InvoicePrintButton.setObjectName("InvoicePrintButton")
        self.MainTabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1888, 26))
        self.menubar.setObjectName("menubar")
        self.menuHep = QtWidgets.QMenu(self.menubar)
        self.menuHep.setObjectName("menuHep")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuPrinter_config = QtWidgets.QMenu(self.menubar)
        self.menuPrinter_config.setObjectName("menuPrinter_config")
        self.menuShortcuts = QtWidgets.QMenu(self.menubar)
        self.menuShortcuts.setObjectName("menuShortcuts")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionPrevious_Records = QtWidgets.QAction(MainWindow)
        self.actionPrevious_Records.setObjectName("actionPrevious_Records")
        self.actionFile_search = QtWidgets.QAction(MainWindow)
        self.actionFile_search.setObjectName("actionFile_search")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionChange_password = QtWidgets.QAction(MainWindow)
        self.actionChange_password.setObjectName("actionChange_password")
        self.actionCreate_User = QtWidgets.QAction(MainWindow)
        self.actionCreate_User.setObjectName("actionCreate_User")
        self.menuHep.addAction(self.actionPrevious_Records)
        self.menuHep.addAction(self.actionFile_search)
        self.menuHep.addAction(self.actionExport)
        self.menufile.addAction(self.actionCreate_User)
        self.menufile.addAction(self.actionChange_password)
        self.menufile.addAction(self.actionExit)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuHep.menuAction())
        self.menubar.addAction(self.menuPrinter_config.menuAction())
        self.menubar.addAction(self.menuShortcuts.menuAction())

        self.retranslateUi(MainWindow)
        self.MainTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Billing Application"))
        self.label_10.setText(_translate("MainWindow", "ITEM Name:"))
        self.label_11.setText(_translate("MainWindow", "QTY:"))
        self.label_20.setText(_translate("MainWindow", "RS .P"))
        self.AddItemButton.setText(_translate("MainWindow", "Add Item"))
        self.TotalAmountLabel.setText(_translate("MainWindow", "1000"))
        self.NewLrButton.setText(_translate("MainWindow", "NEW LR"))
        self.EditLrButton.setText(_translate("MainWindow", "EDIT LR"))
        self.CancelLrButton.setText(_translate("MainWindow", "CANCEL LR"))
        self.PrintLrButton.setText(_translate("MainWindow", "PRINT LR"))
        self.label_22.setText(_translate("MainWindow", "RATE:"))
        self.labbb.setText(_translate("MainWindow", "H Charge:"))
        self.llab1.setText(_translate("MainWindow", "Crossing:"))
        self.label_25.setText(_translate("MainWindow", "CNR GST:"))
        self.label_26.setText(_translate("MainWindow", "CNE GST:"))
        self.label_27.setText(_translate("MainWindow", "LR TYPE:"))
        self.LRTypeInput.setItemText(0, _translate("MainWindow", "TO PAY"))
        self.LRTypeInput.setItemText(1, _translate("MainWindow", "PAID"))
        self.label_7.setText(_translate("MainWindow", "CNE:"))
        self.label_9.setText(_translate("MainWindow", "CLR :"))
        self.label_4.setText(_translate("MainWindow", "From Station:"))
        self.label_21.setText(_translate("MainWindow", "VECHICLE NO:"))
        self.label_6.setText(_translate("MainWindow", "To Station :"))
        self.label_5.setText(_translate("MainWindow", "CNR:"))
        self.label_8.setText(_translate("MainWindow", "Date :"))
        self.label.setText(_translate("MainWindow", "CLR Number:"))
        self.SearchCLRButton.setText(_translate("MainWindow", "Search"))
        self.label_2.setText(_translate("MainWindow", "Date:"))
        self.DateLabel.setText(_translate("MainWindow", "0/0/0000"))
        self.label_3.setText(_translate("MainWindow", "Branch Code:"))
        self.BranchComboBox.setItemText(0, _translate("MainWindow", "A"))
        self.BranchComboBox.setItemText(1, _translate("MainWindow", "B"))
        self.BranchComboBox.setItemText(2, _translate("MainWindow", "C"))
        self.BranchComboBox.setItemText(3, _translate("MainWindow", "D"))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.tab), _translate("MainWindow", "BILLING"))
        self.label_15.setText(_translate("MainWindow", "INVOICE DATE:"))
        self.label_17.setText(_translate("MainWindow", " PR.INVOICE NUMBER:"))
        self.label_40.setText(_translate("MainWindow", "INVOICE STATION:"))
        self.label_41.setText(_translate("MainWindow", "VECHICLE NO:"))
        self.InvoiceBranchCode.setItemText(0, _translate("MainWindow", "A"))
        self.InvoiceBranchCode.setItemText(1, _translate("MainWindow", "B"))
        self.InvoiceBranchCode.setItemText(2, _translate("MainWindow", "C"))
        self.InvoiceBranchCode.setItemText(3, _translate("MainWindow", "D"))
        self.label_45.setText(_translate("MainWindow", "Branch Code:"))
        self.label_12.setText(_translate("MainWindow", "LR Number:"))
        self.LRSearchInvoiceButton.setText(_translate("MainWindow", "Search"))
        self.InvoicePrintButton.setText(_translate("MainWindow", "PRINT LR"))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.tab_2), _translate("MainWindow", "INVOICE"))
        self.menuHep.setTitle(_translate("MainWindow", "Search"))
        self.menufile.setTitle(_translate("MainWindow", "File"))
        self.menuPrinter_config.setTitle(_translate("MainWindow", "Printer config"))
        self.menuShortcuts.setTitle(_translate("MainWindow", "Shortcuts"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionPrevious_Records.setText(_translate("MainWindow", "Invoice search"))
        self.actionFile_search.setText(_translate("MainWindow", "File search"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionChange_password.setText(_translate("MainWindow", "Change password "))
        self.actionCreate_User.setText(_translate("MainWindow", "Create User"))
