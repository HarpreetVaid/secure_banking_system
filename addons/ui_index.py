# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1119, 853)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.icon_name = QWidget(self.centralwidget)
        self.icon_name.setObjectName(u"icon_name")
        self.icon_name.setGeometry(QRect(19, -1, 175, 845))
        self.icon_name.setLayoutDirection(Qt.LeftToRight)
        self.icon_name.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(68, 68, 68);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:white;\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	text-align:left;\n"
"	border:none;\n"
"	height:40px;\n"
"	padding-left:10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"Qlabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	color:black;\n"
"	font-weight:bold;\n"
"}\n"
"\n"
"\n"
"")
        self.gridLayout = QGridLayout(self.icon_name)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, 0, -1)
        self.name = QLabel(self.icon_name)
        self.name.setObjectName(u"name")
        self.name.setEnabled(True)
        self.name.setAutoFillBackground(False)
        self.name.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"font-weight:bold;")
        self.name.setMargin(22)

        self.gridLayout.addWidget(self.name, 0, 0, 1, 1)

        self.accountt_info = QPushButton(self.icon_name)
        self.accountt_info.setObjectName(u"accountt_info")
        self.accountt_info.setIconSize(QSize(45, 20))
        self.accountt_info.setCheckable(True)
        self.accountt_info.setAutoExclusive(True)

        self.gridLayout.addWidget(self.accountt_info, 1, 0, 1, 1)

        self.balance = QPushButton(self.icon_name)
        self.balance.setObjectName(u"balance")
        self.balance.setCheckable(True)
        self.balance.setAutoExclusive(True)

        self.gridLayout.addWidget(self.balance, 2, 0, 1, 1)

        self.add_money = QPushButton(self.icon_name)
        self.add_money.setObjectName(u"add_money")
        self.add_money.setCheckable(True)
        self.add_money.setAutoExclusive(True)

        self.gridLayout.addWidget(self.add_money, 3, 0, 1, 1)

        self.withdraw_money = QPushButton(self.icon_name)
        self.withdraw_money.setObjectName(u"withdraw_money")
        self.withdraw_money.setCheckable(True)
        self.withdraw_money.setAutoExclusive(True)

        self.gridLayout.addWidget(self.withdraw_money, 4, 0, 1, 1)

        self.open_account = QPushButton(self.icon_name)
        self.open_account.setObjectName(u"open_account")
        self.open_account.setCheckable(True)
        self.open_account.setAutoExclusive(True)

        self.gridLayout.addWidget(self.open_account, 5, 0, 1, 1)

        self.delete_account = QPushButton(self.icon_name)
        self.delete_account.setObjectName(u"delete_account")
        self.delete_account.setEnabled(True)
        self.delete_account.setCheckable(True)
        self.delete_account.setAutoExclusive(True)

        self.gridLayout.addWidget(self.delete_account, 6, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 425, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 7, 0, 1, 1)

        self.quit = QPushButton(self.icon_name)
        self.quit.setObjectName(u"quit")
        self.quit.setCheckable(True)
        self.quit.setAutoExclusive(True)

        self.gridLayout.addWidget(self.quit, 8, 0, 1, 1)

        self.main_window = QWidget(self.centralwidget)
        self.main_window.setObjectName(u"main_window")
        self.main_window.setGeometry(QRect(190, 10, 901, 831))
        self.main_window.setStyleSheet(u"QWidet{\n"
"	ba\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.widget = QWidget(self.main_window)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 901, 831))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(198, 78, 911, 761))
        self.stackedWidget.setStyleSheet(u"")
        self.account_info_page = QWidget()
        self.account_info_page.setObjectName(u"account_info_page")
        self.account_label = QLabel(self.account_info_page)
        self.account_label.setObjectName(u"account_label")
        self.account_label.setGeometry(QRect(270, 200, 281, 141))
        self.stackedWidget.addWidget(self.account_info_page)
        self.balance_page = QWidget()
        self.balance_page.setObjectName(u"balance_page")
        self.balance_label = QLabel(self.balance_page)
        self.balance_label.setObjectName(u"balance_label")
        self.balance_label.setGeometry(QRect(380, 350, 281, 141))
        self.stackedWidget.addWidget(self.balance_page)
        self.deposit_page = QWidget()
        self.deposit_page.setObjectName(u"deposit_page")
        self.deposit_label = QLabel(self.deposit_page)
        self.deposit_label.setObjectName(u"deposit_label")
        self.deposit_label.setGeometry(QRect(310, 260, 151, 91))
        self.stackedWidget.addWidget(self.deposit_page)
        self.withdraw_page = QWidget()
        self.withdraw_page.setObjectName(u"withdraw_page")
        self.withdraw_label = QLabel(self.withdraw_page)
        self.withdraw_label.setObjectName(u"withdraw_label")
        self.withdraw_label.setGeometry(QRect(410, 290, 281, 141))
        self.stackedWidget.addWidget(self.withdraw_page)
        self.open_account_page = QWidget()
        self.open_account_page.setObjectName(u"open_account_page")
        self.open_acc_label = QLabel(self.open_account_page)
        self.open_acc_label.setObjectName(u"open_acc_label")
        self.open_acc_label.setGeometry(QRect(470, 170, 100, 141))
        self.stackedWidget.addWidget(self.open_account_page)
        self.logi_page = QWidget()
        self.logi_page.setObjectName(u"logi_page")
        self.login_label = QLabel(self.logi_page)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setGeometry(QRect(320, 200, 281, 141))
        self.stackedWidget.addWidget(self.logi_page)
        self.delete_account_page = QWidget()
        self.delete_account_page.setObjectName(u"delete_account_page")
        self.delete_label = QLabel(self.delete_account_page)
        self.delete_label.setObjectName(u"delete_label")
        self.delete_label.setGeometry(QRect(340, 210, 281, 141))
        self.stackedWidget.addWidget(self.delete_account_page)
        self.status_bar = QWidget(self.centralwidget)
        self.status_bar.setObjectName(u"status_bar")
        self.status_bar.setGeometry(QRect(198, 2, 911, 71))
        self.status_bar.setAutoFillBackground(False)
        self.status_bar.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(182, 182, 182);\n"
"}\n"
"QPushButton{\n"
"	color:white;\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	border:none;\n"
"	height:40px;\n"
"	width:60px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"}\n"
"\n"
"QLabel{\n"
"	color:white;\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	color:black;\n"
"	font-weight:bold;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.status_bar)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(18, 15, 15, 18)
        self.login_name_label = QLabel(self.status_bar)
        self.login_name_label.setObjectName(u"login_name_label")

        self.horizontalLayout.addWidget(self.login_name_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.login_button = QPushButton(self.status_bar)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setEnabled(True)
        self.login_button.setIconSize(QSize(29, 53))
        self.login_button.setCheckable(True)

        self.horizontalLayout.addWidget(self.login_button)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 0, 2, 2))
        self.gridLayout_2 = QGridLayout(self.widget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.main_window.raise_()
        self.icon_name.raise_()
        self.stackedWidget.raise_()
        self.status_bar.raise_()

        self.retranslateUi(MainWindow)
        self.quit.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.name.setText(QCoreApplication.translate("MainWindow", u" Secure Banking", None))
        self.accountt_info.setText(QCoreApplication.translate("MainWindow", u"Account Info", None))
        self.balance.setText(QCoreApplication.translate("MainWindow", u"Balance", None))
        self.add_money.setText(QCoreApplication.translate("MainWindow", u"Deposit", None))
        self.withdraw_money.setText(QCoreApplication.translate("MainWindow", u"Withdraw ", None))
        self.open_account.setText(QCoreApplication.translate("MainWindow", u"Open Account", None))
        self.delete_account.setText(QCoreApplication.translate("MainWindow", u"Delete Account", None))
        self.quit.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.account_label.setText(QCoreApplication.translate("MainWindow", u"Accont", None))
        self.balance_label.setText(QCoreApplication.translate("MainWindow", u"balance", None))
        self.deposit_label.setText(QCoreApplication.translate("MainWindow", u"deposit", None))
        self.withdraw_label.setText(QCoreApplication.translate("MainWindow", u"withdraw", None))
        self.open_acc_label.setText(QCoreApplication.translate("MainWindow", u"open account", None))
        self.login_label.setText(QCoreApplication.translate("MainWindow", u"ogin", None))
        self.delete_label.setText(QCoreApplication.translate("MainWindow", u"delete account", None))
        self.login_name_label.setText(QCoreApplication.translate("MainWindow", u"Welcome User 010101010", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

