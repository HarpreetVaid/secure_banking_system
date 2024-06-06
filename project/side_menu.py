from PySide6.QtCore import (QCoreApplication,QMetaObject, QRect,QSize,  Qt)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSplitter, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Secure Banking System")
        MainWindow.resize(1125, 750)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(200, 90, 901, 741))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;"
"border:none;")
        self.account_info_page = QWidget()
        self.account_info_page.setObjectName(u"account_info_page")
        self.account_info_label = QLabel(self.account_info_page)
        self.account_info_label.setObjectName(u"account_info_label")
        self.account_info_label.setGeometry(QRect(0, 0, 901, 91))
        self.account_info_label.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"font: 48pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.account_info_label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.layoutWidget_5 = QWidget(self.account_info_page)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(100, 170, 681, 131))
        self.acount_info_page_Layout = QVBoxLayout(self.layoutWidget_5)
        self.acount_info_page_Layout.setSpacing(25)
        self.acount_info_page_Layout.setObjectName(u"acount_info_page_Layout")
        self.acount_info_page_Layout.setContentsMargins(5, 10, 0, 0)
        self.username_label_acc = QLabel(self.layoutWidget_5)
        self.username_label_acc.setObjectName(u"username_label_acc")
        self.username_label_acc.setStyleSheet(u"color: black;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"")
        self.username_label_acc.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.username_label_acc.setMargin(0)
        self.username_label_acc.setIndent(12)

        self.acount_info_page_Layout.addWidget(self.username_label_acc)

        self.username_field_acc = QLineEdit(self.layoutWidget_5)
        self.username_field_acc.setObjectName(u"username_field_acc")
        self.username_field_acc.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username_field_acc.sizePolicy().hasHeightForWidth())
        self.username_field_acc.setSizePolicy(sizePolicy)
        self.username_field_acc.setStyleSheet(u"height:30px;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"border-radius:10px;\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.username_field_acc.setMaxLength(32773)
        self.username_field_acc.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.username_field_acc.setClearButtonEnabled(True)

        self.acount_info_page_Layout.addWidget(self.username_field_acc)

        self.search_account_info = QPushButton(self.account_info_page)
        self.search_account_info.setObjectName(u"search_account_info")
        self.search_account_info.setGeometry(QRect(690, 360, 90, 40))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(34)
        sizePolicy1.setVerticalStretch(35)
        sizePolicy1.setHeightForWidth(self.search_account_info.sizePolicy().hasHeightForWidth())
        self.search_account_info.setSizePolicy(sizePolicy1)
        self.search_account_info.setMinimumSize(QSize(90, 0))
        self.search_account_info.setLayoutDirection(Qt.LeftToRight)
        self.search_account_info.setAutoFillBackground(False)
        self.search_account_info.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(117, 117, 117);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	border:none;\n"
"	height:40px;\n"
"	padding-left:10px;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:white;\n"
"	color:black;\n"
"	font-weight:bold;\n"
"}\n"
"")
        self.search_account_info.setIconSize(QSize(20, 20))
        self.search_account_info.setCheckable(True)
        self.search_account_info.setAutoExclusive(True)
        self.search_account_info.setAutoRepeatDelay(0)
        self.stackedWidget.addWidget(self.account_info_page)
        self.account_info_details = QWidget()
        self.account_info_details.setObjectName(u"account_info_details")
        self.account_info_detail_label = QLabel(self.account_info_details)
        self.account_info_detail_label.setObjectName(u"account_info_detail_label")
        self.account_info_detail_label.setGeometry(QRect(-30, 0, 931, 91))
        self.account_info_detail_label.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"font: 48pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.account_info_detail_label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.back_account_info = QPushButton(self.account_info_details)
        self.back_account_info.setObjectName(u"back_account_info")
        self.back_account_info.setGeometry(QRect(660, 550, 90, 40))
        sizePolicy1.setHeightForWidth(self.back_account_info.sizePolicy().hasHeightForWidth())
        self.back_account_info.setSizePolicy(sizePolicy1)
        self.back_account_info.setMinimumSize(QSize(90, 0))
        self.back_account_info.setLayoutDirection(Qt.LeftToRight)
        self.back_account_info.setAutoFillBackground(False)
        self.back_account_info.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(117, 117, 117);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	border:none;\n"
"	height:40px;\n"
"	padding-left:10px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color:white;\n"
"	color:black;\n"
"	font-weight:bold;\n"
"}\n"
"")
        self.back_account_info.setIconSize(QSize(20, 20))
        self.back_account_info.setCheckable(True)
        self.back_account_info.setAutoExclusive(True)
        self.back_account_info.setAutoRepeatDelay(0)
        self.layoutWidget = QWidget(self.account_info_details)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(80, 130, 491, 371))
        self.gridLayout_3 = QGridLayout(self.layoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.name_account_info_value = QLabel(self.layoutWidget)
        self.name_account_info_value.setObjectName(u"name_account_info_value")
        self.name_account_info_value.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.name_account_info_value.setScaledContents(False)
        self.name_account_info_value.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.name_account_info_value.setWordWrap(True)
        self.name_account_info_value.setMargin(0)
        self.name_account_info_value.setIndent(0)

        self.verticalLayout.addWidget(self.name_account_info_value)

        self.name_account_info = QLabel(self.layoutWidget)
        self.name_account_info.setObjectName(u"name_account_info")
        self.name_account_info.setStyleSheet(u"color: black;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"")
        self.name_account_info.setScaledContents(False)
        self.name_account_info.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.name_account_info.setWordWrap(True)
        self.name_account_info.setMargin(0)
        self.name_account_info.setIndent(0)

        self.verticalLayout.addWidget(self.name_account_info)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.account_no_accinfo = QLabel(self.layoutWidget)
        self.account_no_accinfo.setObjectName(u"account_no_accinfo")
        self.account_no_accinfo.setStyleSheet(u"color: black;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"")
        self.account_no_accinfo.setScaledContents(False)
        self.account_no_accinfo.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.account_no_accinfo.setWordWrap(True)
        self.account_no_accinfo.setMargin(0)
        self.account_no_accinfo.setIndent(0)

        self.verticalLayout_2.addWidget(self.account_no_accinfo)

        self.account_no_value_accinfo = QLabel(self.layoutWidget)
        self.account_no_value_accinfo.setObjectName(u"account_no_value_accinfo")
        self.account_no_value_accinfo.setStyleSheet(u"color: black;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"")
        self.account_no_value_accinfo.setScaledContents(False)
        self.account_no_value_accinfo.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.account_no_value_accinfo.setWordWrap(True)
        self.account_no_value_accinfo.setMargin(0)
        self.account_no_value_accinfo.setIndent(0)

        self.verticalLayout_2.addWidget(self.account_no_value_accinfo)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.balance_account_info = QLabel(self.layoutWidget)
        self.balance_account_info.setObjectName(u"balance_account_info")
        self.balance_account_info.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.balance_account_info.setScaledContents(False)
        self.balance_account_info.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.balance_account_info.setWordWrap(True)
        self.balance_account_info.setMargin(0)
        self.balance_account_info.setIndent(0)

        self.verticalLayout_3.addWidget(self.balance_account_info)

        self.balance_value_account_info_value = QLabel(self.layoutWidget)
        self.balance_value_account_info_value.setObjectName(u"balance_value_account_info_value")
        self.balance_value_account_info_value.setStyleSheet(u"color: black;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"")
        self.balance_value_account_info_value.setScaledContents(False)
        self.balance_value_account_info_value.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.balance_value_account_info_value.setWordWrap(True)
        self.balance_value_account_info_value.setMargin(0)
        self.balance_value_account_info_value.setIndent(0)

        self.verticalLayout_3.addWidget(self.balance_value_account_info_value)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 2, 0, 1, 1)

        self.layoutWidget1 = QWidget(self.account_info_details)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(610, 130, 261, 371))
        self.gridLayout_4 = QGridLayout(self.layoutWidget1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(12)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pic_account_info = QLabel(self.layoutWidget1)
        self.pic_account_info.setObjectName(u"pic_account_info")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(4)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pic_account_info.sizePolicy().hasHeightForWidth())
        self.pic_account_info.setSizePolicy(sizePolicy2)
        self.pic_account_info.setMinimumSize(QSize(241, 240))
        self.pic_account_info.setMaximumSize(QSize(350, 350))

        self.gridLayout_4.addWidget(self.pic_account_info, 0, 0, 1, 1)

        self.signature_account_info = QLabel(self.layoutWidget1)
        self.signature_account_info.setObjectName(u"signature_account_info")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(4)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.signature_account_info.sizePolicy().hasHeightForWidth())
        self.signature_account_info.setSizePolicy(sizePolicy3)
        self.signature_account_info.setMinimumSize(QSize(244, 67))
        self.signature_account_info.setMaximumSize(QSize(133, 87))

        self.gridLayout_4.addWidget(self.signature_account_info, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.account_info_details)
        self.balance_page = QWidget()
        self.balance_page.setObjectName(u"balance_page")
        self.check_balance_label = QLabel(self.balance_page)
        self.check_balance_label.setObjectName(u"check_balance_label")
        self.check_balance_label.setGeometry(QRect(0, 0, 901, 91))
        self.check_balance_label.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"font: 48pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.check_balance_label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.layoutWidget2 = QWidget(self.balance_page)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(80, 131, 731, 380))
        self.gridLayout_5 = QGridLayout(self.layoutWidget2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.value_label_check_balance = QLabel(self.layoutWidget2)
        self.value_label_check_balance.setObjectName(u"value_label_check_balance")
        self.value_label_check_balance.setStyleSheet(u"color: black;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"")
        self.value_label_check_balance.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.value_label_check_balance.setMargin(0)
        self.value_label_check_balance.setIndent(12)

        self.gridLayout_5.addWidget(self.value_label_check_balance, 1, 0, 1, 2)

        self.check_balance_page_layout = QVBoxLayout()
        self.check_balance_page_layout.setSpacing(25)
        self.check_balance_page_layout.setObjectName(u"check_balance_page_layout")
        self.check_balance_page_layout.setContentsMargins(5, 10, 0, 0)
        self.username_label_check_balance = QLabel(self.layoutWidget2)
        self.username_label_check_balance.setObjectName(u"username_label_check_balance")
        self.username_label_check_balance.setStyleSheet(u"color: black;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"")
        self.username_label_check_balance.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.username_label_check_balance.setMargin(0)
        self.username_label_check_balance.setIndent(12)

        self.check_balance_page_layout.addWidget(self.username_label_check_balance)

        self.username_field_check_balance = QLineEdit(self.layoutWidget2)
        self.username_field_check_balance.setObjectName(u"username_field_check_balance")
        self.username_field_check_balance.setEnabled(True)
        sizePolicy.setHeightForWidth(self.username_field_check_balance.sizePolicy().hasHeightForWidth())
        self.username_field_check_balance.setSizePolicy(sizePolicy)
        self.username_field_check_balance.setStyleSheet(u"height:30px;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"border-radius:10px;\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.username_field_check_balance.setMaxLength(32773)
        self.username_field_check_balance.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.username_field_check_balance.setClearButtonEnabled(True)

        self.check_balance_page_layout.addWidget(self.username_field_check_balance)

        self.search_button_check_balance = QPushButton(self.layoutWidget2)
        self.search_button_check_balance.setObjectName(u"search_button_check_balance")
        sizePolicy1.setHeightForWidth(self.search_button_check_balance.sizePolicy().hasHeightForWidth())
        self.search_button_check_balance.setSizePolicy(sizePolicy1)
        self.search_button_check_balance.setMinimumSize(QSize(90, 0))
        self.search_button_check_balance.setLayoutDirection(Qt.LeftToRight)
        self.search_button_check_balance.setAutoFillBackground(False)
        self.search_button_check_balance.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(117, 117, 117);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	border:none;\n"
"	height:40px;\n"
"	padding-left:10px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color:white;\n"
"	color:black;\n"
"	font-weight:bold;\n"
"}\n"
"")
        self.search_button_check_balance.setIconSize(QSize(20, 20))
        self.search_button_check_balance.setCheckable(True)
        self.search_button_check_balance.setAutoExclusive(True)
        self.search_button_check_balance.setAutoRepeatDelay(0)

        self.check_balance_page_layout.addWidget(self.search_button_check_balance)


        self.gridLayout_5.addLayout(self.check_balance_page_layout, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.balance_page)
        self.deposit_page = QWidget()
        self.deposit_page.setObjectName(u"deposit_page")
        self.add_money_label = QLabel(self.deposit_page)
        self.add_money_label.setObjectName(u"add_money_label")
        self.add_money_label.setGeometry(QRect(0, 0, 901, 91))
        self.add_money_label.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"font: 48pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.add_money_label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.layoutWidget3 = QWidget(self.deposit_page)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(120, 141, 641, 381))
        self.gridLayout_6 = QGridLayout(self.layoutWidget3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setVerticalSpacing(90)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.username_label_deposit = QLabel(self.layoutWidget3)
        self.username_label_deposit.setObjectName(u"username_label_deposit")
        self.username_label_deposit.setStyleSheet(u"color: black;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"")
        self.username_label_deposit.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.username_label_deposit.setMargin(0)
        self.username_label_deposit.setIndent(13)

        self.verticalLayout_4.addWidget(self.username_label_deposit)

        self.username_field_deposit_value = QLineEdit(self.layoutWidget3)
        self.username_field_deposit_value.setObjectName(u"username_field_deposit_value")
        self.username_field_deposit_value.setEnabled(True)
        sizePolicy.setHeightForWidth(self.username_field_deposit_value.sizePolicy().hasHeightForWidth())
        self.username_field_deposit_value.setSizePolicy(sizePolicy)
        self.username_field_deposit_value.setStyleSheet(u"height:30px;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"border-radius:10px;\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.username_field_deposit_value.setMaxLength(32773)
        self.username_field_deposit_value.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.username_field_deposit_value.setClearButtonEnabled(True)

        self.verticalLayout_4.addWidget(self.username_field_deposit_value)


        self.gridLayout_6.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.amount_label_deposit = QLabel(self.layoutWidget3)
        self.amount_label_deposit.setObjectName(u"amount_label_deposit")
        self.amount_label_deposit.setStyleSheet(u"color: black;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"")
        self.amount_label_deposit.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.amount_label_deposit.setMargin(0)
        self.amount_label_deposit.setIndent(13)
        self.amount_label_deposit.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_5.addWidget(self.amount_label_deposit)

        self.amount_field_deposit = QLineEdit(self.layoutWidget3)
        self.amount_field_deposit.setObjectName(u"amount_field_deposit")
        self.amount_field_deposit.setEnabled(True)
        sizePolicy.setHeightForWidth(self.amount_field_deposit.sizePolicy().hasHeightForWidth())
        self.amount_field_deposit.setSizePolicy(sizePolicy)
        self.amount_field_deposit.setStyleSheet(u"height:30px;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"border-radius:10px;\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.amount_field_deposit.setMaxLength(32773)
        self.amount_field_deposit.setEchoMode(QLineEdit.Normal)
        self.amount_field_deposit.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.amount_field_deposit.setClearButtonEnabled(True)

        self.verticalLayout_5.addWidget(self.amount_field_deposit)


        self.gridLayout_6.addLayout(self.verticalLayout_5, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.status_label_add_money = QLabel(self.layoutWidget3)
        self.status_label_add_money.setObjectName(u"status_label_add_money")
        self.status_label_add_money.setStyleSheet(u"color: black;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"")
        self.status_label_add_money.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.status_label_add_money.setMargin(0)
        self.status_label_add_money.setIndent(12)

        self.horizontalLayout_2.addWidget(self.status_label_add_money)

        self.deposit_button_deposit = QPushButton(self.layoutWidget3)
        self.deposit_button_deposit.setObjectName(u"deposit_button_deposit")
        self.deposit_button_deposit.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(117, 117, 117);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	border:none;\n"
"	height:40px;\n"
"	padding-left:10px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color:white;\n"
"	color:black;\n"
"	font-weight:bold;\n"
"}\n"
"")
        self.deposit_button_deposit.setCheckable(True)
        self.deposit_button_deposit.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.deposit_button_deposit)


        self.gridLayout_6.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.deposit_page)
        self.withdraw_page = QWidget()
        self.withdraw_page.setObjectName(u"withdraw_page")
        self.withdraw_money_label = QLabel(self.withdraw_page)
        self.withdraw_money_label.setObjectName(u"withdraw_money_label")
        self.withdraw_money_label.setGeometry(QRect(0, 0, 901, 91))
        self.withdraw_money_label.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"font: 48pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.withdraw_money_label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.layoutWidget_9 = QWidget(self.withdraw_page)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(130, 150, 671, 381))
        self.gridLayout_7 = QGridLayout(self.layoutWidget_9)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setVerticalSpacing(76)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.username_label_withdraw = QLabel(self.layoutWidget_9)
        self.username_label_withdraw.setObjectName(u"username_label_withdraw")
        self.username_label_withdraw.setStyleSheet(u"color: black;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"")
        self.username_label_withdraw.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.username_label_withdraw.setMargin(0)
        self.username_label_withdraw.setIndent(13)

        self.verticalLayout_6.addWidget(self.username_label_withdraw)

        self.username_field_withdraw_value = QLineEdit(self.layoutWidget_9)
        self.username_field_withdraw_value.setObjectName(u"username_field_withdraw_value")
        self.username_field_withdraw_value.setEnabled(True)
        sizePolicy.setHeightForWidth(self.username_field_withdraw_value.sizePolicy().hasHeightForWidth())
        self.username_field_withdraw_value.setSizePolicy(sizePolicy)
        self.username_field_withdraw_value.setStyleSheet(u"height:30px;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"border-radius:10px;\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.username_field_withdraw_value.setMaxLength(32773)
        self.username_field_withdraw_value.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.username_field_withdraw_value.setClearButtonEnabled(True)

        self.verticalLayout_6.addWidget(self.username_field_withdraw_value)


        self.gridLayout_7.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.amount_label_withdraw = QLabel(self.layoutWidget_9)
        self.amount_label_withdraw.setObjectName(u"amount_label_withdraw")
        self.amount_label_withdraw.setStyleSheet(u"color: black;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"")
        self.amount_label_withdraw.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.amount_label_withdraw.setMargin(0)
        self.amount_label_withdraw.setIndent(13)
        self.amount_label_withdraw.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_7.addWidget(self.amount_label_withdraw)

        self.amount_field_withdraw = QLineEdit(self.layoutWidget_9)
        self.amount_field_withdraw.setObjectName(u"amount_field_withdraw")
        self.amount_field_withdraw.setEnabled(True)
        sizePolicy.setHeightForWidth(self.amount_field_withdraw.sizePolicy().hasHeightForWidth())
        self.amount_field_withdraw.setSizePolicy(sizePolicy)
        self.amount_field_withdraw.setStyleSheet(u"height:30px;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"border-radius:10px;\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.amount_field_withdraw.setMaxLength(32773)
        self.amount_field_withdraw.setEchoMode(QLineEdit.Normal)
        self.amount_field_withdraw.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.amount_field_withdraw.setClearButtonEnabled(True)

        self.verticalLayout_7.addWidget(self.amount_field_withdraw)


        self.gridLayout_7.addLayout(self.verticalLayout_7, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.status_label_withdraw = QLabel(self.layoutWidget_9)
        self.status_label_withdraw.setObjectName(u"status_label_withdraw")
        self.status_label_withdraw.setStyleSheet(u"color: black;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"")
        self.status_label_withdraw.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.status_label_withdraw.setMargin(0)
        self.status_label_withdraw.setIndent(12)

        self.horizontalLayout_3.addWidget(self.status_label_withdraw)

        self.deposit_button_withdraw = QPushButton(self.layoutWidget_9)
        self.deposit_button_withdraw.setObjectName(u"deposit_button_withdraw")
        self.deposit_button_withdraw.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(117, 117, 117);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	border:none;\n"
"	height:40px;\n"
"	padding-left:10px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color:white;\n"
"	color:black;\n"
"	font-weight:bold;\n"
"}\n"
"")
        self.deposit_button_withdraw.setCheckable(True)
        self.deposit_button_withdraw.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.deposit_button_withdraw)


        self.gridLayout_7.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.withdraw_page)
        self.open_account_page = QWidget()
        self.open_account_page.setObjectName(u"open_account_page")
        self.open_account_label = QLabel(self.open_account_page)
        self.open_account_label.setObjectName(u"open_account_label")
        self.open_account_label.setGeometry(QRect(0, 0, 901, 91))
        self.open_account_label.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"font: 48pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.open_account_label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.layoutWidget_10 = QWidget(self.open_account_page)
        self.layoutWidget_10.setObjectName(u"layoutWidget_10")
        self.layoutWidget_10.setGeometry(QRect(50, 150, 491, 381))
        self.gridLayout_8 = QGridLayout(self.layoutWidget_10)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(0)
        self.gridLayout_8.setVerticalSpacing(50)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.account_no_accopen = QLabel(self.layoutWidget_10)
        self.account_no_accopen.setObjectName(u"account_no_accopen")
        self.account_no_accopen.setStyleSheet(u"color: black;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"")
        self.account_no_accopen.setScaledContents(False)
        self.account_no_accopen.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.account_no_accopen.setWordWrap(True)
        self.account_no_accopen.setMargin(0)
        self.account_no_accopen.setIndent(0)

        self.verticalLayout_9.addWidget(self.account_no_accopen)

        self.account_number_lineEdit_open_account = QLineEdit(self.layoutWidget_10)
        self.account_number_lineEdit_open_account.setObjectName(u"account_number_lineEdit_open_account")
        self.account_number_lineEdit_open_account.setStyleSheet(u"height:30px;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"border-radius:10px;\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.account_number_lineEdit_open_account.setClearButtonEnabled(True)

        self.verticalLayout_9.addWidget(self.account_number_lineEdit_open_account)


        self.gridLayout_8.addLayout(self.verticalLayout_9, 1, 0, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.balance_account_open = QLabel(self.layoutWidget_10)
        self.balance_account_open.setObjectName(u"balance_account_open")
        self.balance_account_open.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.balance_account_open.setScaledContents(False)
        self.balance_account_open.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.balance_account_open.setWordWrap(True)
        self.balance_account_open.setMargin(0)
        self.balance_account_open.setIndent(0)

        self.verticalLayout_10.addWidget(self.balance_account_open)

        self.amount_lineEdit_open_account = QLineEdit(self.layoutWidget_10)
        self.amount_lineEdit_open_account.setObjectName(u"amount_lineEdit_open_account")
        self.amount_lineEdit_open_account.setStyleSheet(u"height:30px;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"border-radius:10px;\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.amount_lineEdit_open_account.setClearButtonEnabled(True)

        self.verticalLayout_10.addWidget(self.amount_lineEdit_open_account)


        self.gridLayout_8.addLayout(self.verticalLayout_10, 2, 0, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.usernamename_account_open_label = QLabel(self.layoutWidget_10)
        self.usernamename_account_open_label.setObjectName(u"usernamename_account_open_label")
        self.usernamename_account_open_label.setStyleSheet(u"color: black;\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"")
        self.usernamename_account_open_label.setScaledContents(False)
        self.usernamename_account_open_label.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.usernamename_account_open_label.setWordWrap(True)
        self.usernamename_account_open_label.setMargin(0)
        self.usernamename_account_open_label.setIndent(0)

        self.verticalLayout_8.addWidget(self.usernamename_account_open_label)

        self.username_lineEdit_open_account = QLineEdit(self.layoutWidget_10)
        self.username_lineEdit_open_account.setObjectName(u"username_lineEdit_open_account")
        self.username_lineEdit_open_account.setStyleSheet(u"height:30px;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"border-radius:10px;\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.username_lineEdit_open_account.setClearButtonEnabled(True)

        self.verticalLayout_8.addWidget(self.username_lineEdit_open_account)


        self.gridLayout_8.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.picture_label_open_account = QLabel(self.open_account_page)
        self.picture_label_open_account.setObjectName(u"picture_label_open_account")
        self.picture_label_open_account.setGeometry(QRect(630, 160, 191, 162))
        self.picture_label_open_account.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:none;")
        self.picture_button_open_account = QPushButton(self.open_account_page)
        self.picture_button_open_account.setObjectName(u"picture_button_open_account")
        self.picture_button_open_account.setGeometry(QRect(670, 330, 151, 40))
        self.picture_button_open_account.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(117, 117, 117);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	border:none;\n"
"	height:40px;\n"
"	padding-left:10px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color:white;\n"
"	color:black;\n"
"	font-weight:bold;\n"
"}\n"
"")
        self.picture_button_open_account.setCheckable(True)
        self.picture_button_open_account.setAutoExclusive(True)
        self.signature_upload_button_open_account = QPushButton(self.open_account_page)
        self.signature_upload_button_open_account.setObjectName(u"signature_upload_button_open_account")
        self.signature_upload_button_open_account.setGeometry(QRect(700, 450, 111, 34))
        self.signature_upload_button_open_account.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(117, 117, 117);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	border:none;\n"
"	height:40px;\n"
"	padding-left:10px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color:white;\n"
"	color:black;\n"
"	font-weight:bold;\n"
"}\n"
"")
        self.signature_upload_button_open_account.setCheckable(True)
        self.signature_upload_button_open_account.setAutoExclusive(True)
        self.signature_label_open_account = QLabel(self.open_account_page)
        self.signature_label_open_account.setObjectName(u"signature_label_open_account")
        self.signature_label_open_account.setGeometry(QRect(630, 390, 191, 51))
        self.signature_label_open_account.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.status_label_open_account = QLabel(self.open_account_page)
        self.status_label_open_account.setObjectName(u"status_label_open_account")
        self.status_label_open_account.setGeometry(QRect(40, 570, 251, 21))
        self.status_label_open_account.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";")
        self.splitter_8 = QSplitter(self.open_account_page)
        self.splitter_8.setObjectName(u"splitter_8")
        self.splitter_8.setGeometry(QRect(190, 570, 461, 41))
        self.splitter_8.setOrientation(Qt.Horizontal)
        self.open_button_open_account = QPushButton(self.splitter_8)
        self.open_button_open_account.setObjectName(u"open_button_open_account")
        self.open_button_open_account.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(117, 117, 117);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	border:none;\n"
"	height:40px;\n"
"	padding-left:10px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color:white;\n"
"	color:black;\n"
"	font-weight:bold;\n"
"}\n"
"")
        self.open_button_open_account.setCheckable(True)
        self.open_button_open_account.setAutoExclusive(True)
        self.splitter_8.addWidget(self.open_button_open_account)
        self.cancel_button_open_account = QPushButton(self.splitter_8)
        self.cancel_button_open_account.setObjectName(u"cancel_button_open_account")
        self.cancel_button_open_account.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(117, 117, 117);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	border:none;\n"
"	height:40px;\n"
"	padding-left:10px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color:white;\n"
"	color:black;\n"
"	font-weight:bold;\n"
"}\n"
"")
        self.cancel_button_open_account.setCheckable(True)
        self.cancel_button_open_account.setAutoExclusive(True)
        self.splitter_8.addWidget(self.cancel_button_open_account)
        self.stackedWidget.addWidget(self.open_account_page)
        self.logi_page = QWidget()
        self.logi_page.setObjectName(u"logi_page")
        self.login_label = QLabel(self.logi_page)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setGeometry(QRect(0, 0, 901, 91))
        self.login_label.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"font: 48pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.login_label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.splitter = QSplitter(self.logi_page)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(130, 140, 661, 431))
        self.splitter.setOrientation(Qt.Vertical)
        self.layoutWidget4 = QWidget(self.splitter)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.username_logi_page_Layout = QVBoxLayout(self.layoutWidget4)
        self.username_logi_page_Layout.setSpacing(0)
        self.username_logi_page_Layout.setObjectName(u"username_logi_page_Layout")
        self.username_logi_page_Layout.setContentsMargins(0, 10, 10, 50)
        self.username_label = QLabel(self.layoutWidget4)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setStyleSheet(u"color: black;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"")
        self.username_label.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.username_label.setMargin(0)
        self.username_label.setIndent(13)

        self.username_logi_page_Layout.addWidget(self.username_label)

        self.username_field = QLineEdit(self.layoutWidget4)
        self.username_field.setObjectName(u"username_field")
        self.username_field.setEnabled(True)
        sizePolicy.setHeightForWidth(self.username_field.sizePolicy().hasHeightForWidth())
        self.username_field.setSizePolicy(sizePolicy)
        self.username_field.setStyleSheet(u"height:30px;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"border-radius:10px;\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.username_field.setMaxLength(32773)
        self.username_field.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.username_field.setClearButtonEnabled(True)

        self.username_logi_page_Layout.addWidget(self.username_field)

        self.splitter.addWidget(self.layoutWidget4)
        self.layoutWidget_2 = QWidget(self.splitter)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.password_space = QVBoxLayout(self.layoutWidget_2)
        self.password_space.setSpacing(0)
        self.password_space.setObjectName(u"password_space")
        self.password_space.setContentsMargins(0, 11, 10, 50)
        self.password_label = QLabel(self.layoutWidget_2)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setStyleSheet(u"color: black;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"")
        self.password_label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.password_label.setMargin(0)
        self.password_label.setIndent(13)
        self.password_label.setTextInteractionFlags(Qt.NoTextInteraction)

        self.password_space.addWidget(self.password_label)

        self.password_field = QLineEdit(self.layoutWidget_2)
        self.password_field.setObjectName(u"password_field")
        self.password_field.setEnabled(True)
        sizePolicy.setHeightForWidth(self.password_field.sizePolicy().hasHeightForWidth())
        self.password_field.setSizePolicy(sizePolicy)
        self.password_field.setStyleSheet(u"height:30px;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"border-radius:10px;\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.password_field.setMaxLength(32773)
        self.password_field.setEchoMode(QLineEdit.Password)
        self.password_field.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.password_field.setClearButtonEnabled(True)

        self.password_space.addWidget(self.password_field)

        self.splitter.addWidget(self.layoutWidget_2)
        self.login_failed_text = QLabel(self.splitter)
        self.login_failed_text.setObjectName(u"login_failed_text")
        self.login_failed_text.setLayoutDirection(Qt.RightToLeft)
        self.login_failed_text.setStyleSheet(u"color: white;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.login_failed_text.setTextInteractionFlags(Qt.NoTextInteraction)
        self.splitter.addWidget(self.login_failed_text)
        self.layoutWidget5 = QWidget(self.splitter)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.login_cancel_buttons = QHBoxLayout(self.layoutWidget5)
        self.login_cancel_buttons.setSpacing(26)
        self.login_cancel_buttons.setObjectName(u"login_cancel_buttons")
        self.login_cancel_buttons.setContentsMargins(150, 0, 0, 0)
        self.login_button_page = QPushButton(self.layoutWidget5)
        self.login_button_page.setObjectName(u"login_button_page")
        self.login_button_page.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(117, 117, 117);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	border:none;\n"
"	height:40px;\n"
"	padding-left:10px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color:white;\n"
"	color:black;\n"
"	font-weight:bold;\n"
"}\n"
"")
        self.login_button_page.setCheckable(True)
        self.login_button_page.setAutoExclusive(True)

        self.login_cancel_buttons.addWidget(self.login_button_page)

        self.cancel_page = QPushButton(self.layoutWidget5)
        self.cancel_page.setObjectName(u"cancel_page")
        self.cancel_page.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(117, 117, 117);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	border:none;\n"
"	height:40px;\n"
"	padding-left:10px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color:white;\n"
"	color:black;\n"
"	font-weight:bold;\n"
"}")
        self.cancel_page.setCheckable(True)
        self.cancel_page.setAutoExclusive(True)

        self.login_cancel_buttons.addWidget(self.cancel_page)

        self.splitter.addWidget(self.layoutWidget5)
        self.stackedWidget.addWidget(self.logi_page)
        self.delete_account_page = QWidget()
        self.delete_account_page.setObjectName(u"delete_account_page")
        self.login_label_2 = QLabel(self.delete_account_page)
        self.login_label_2.setObjectName(u"login_label_2")
        self.login_label_2.setGeometry(QRect(0, 0, 901, 91))
        self.login_label_2.setStyleSheet(u"background-color: rgb(227, 227, 227);\n"
"font: 48pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.login_label_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.splitter_2 = QSplitter(self.delete_account_page)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(130, 120, 681, 361))
        self.splitter_2.setOrientation(Qt.Vertical)
        self.layoutWidget_4 = QWidget(self.splitter_2)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.delete_acount_login_page_Layout = QVBoxLayout(self.layoutWidget_4)
        self.delete_acount_login_page_Layout.setSpacing(0)
        self.delete_acount_login_page_Layout.setObjectName(u"delete_acount_login_page_Layout")
        self.delete_acount_login_page_Layout.setContentsMargins(0, 10, 10, 57)
        self.username_label_2 = QLabel(self.layoutWidget_4)
        self.username_label_2.setObjectName(u"username_label_2")
        self.username_label_2.setStyleSheet(u"color: black;\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"")
        self.username_label_2.setAlignment(Qt.AlignBottom|Qt.AlignJustify)
        self.username_label_2.setMargin(0)
        self.username_label_2.setIndent(13)

        self.delete_acount_login_page_Layout.addWidget(self.username_label_2)

        self.username_field_2 = QLineEdit(self.layoutWidget_4)
        self.username_field_2.setObjectName(u"username_field_2")
        self.username_field_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.username_field_2.sizePolicy().hasHeightForWidth())
        self.username_field_2.setSizePolicy(sizePolicy)
        self.username_field_2.setStyleSheet(u"height:30px;\n"
"font: 9pt \"MS Shell Dlg 2\";\n"
"border-radius:10px;\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.username_field_2.setMaxLength(32773)
        self.username_field_2.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.username_field_2.setClearButtonEnabled(True)

        self.delete_acount_login_page_Layout.addWidget(self.username_field_2)

        self.splitter_2.addWidget(self.layoutWidget_4)
        self.login_failed_text_2 = QLabel(self.splitter_2)
        self.login_failed_text_2.setObjectName(u"login_failed_text_2")
        self.login_failed_text_2.setLayoutDirection(Qt.RightToLeft)
        self.login_failed_text_2.setStyleSheet(u"color: black;\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.login_failed_text_2.setTextInteractionFlags(Qt.NoTextInteraction)
        self.splitter_2.addWidget(self.login_failed_text_2)
        self.layoutWidget_3 = QWidget(self.splitter_2)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.delete_user_cancel_buttons = QHBoxLayout(self.layoutWidget_3)
        self.delete_user_cancel_buttons.setSpacing(26)
        self.delete_user_cancel_buttons.setObjectName(u"delete_user_cancel_buttons")
        self.delete_user_cancel_buttons.setContentsMargins(150, 0, 0, 0)
        self.delete_account_button_page = QPushButton(self.layoutWidget_3)
        self.delete_account_button_page.setObjectName(u"delete_account_button_page")
        self.delete_account_button_page.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(117, 117, 117);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	border:none;\n"
"	height:40px;\n"
"	padding-left:10px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color:white;\n"
"	color:black;\n"
"	font-weight:bold;\n"
"}\n"
"")
        self.delete_account_button_page.setCheckable(True)
        self.delete_account_button_page.setAutoExclusive(True)

        self.delete_user_cancel_buttons.addWidget(self.delete_account_button_page)

        self.delete_page_cancel_page = QPushButton(self.layoutWidget_3)
        self.delete_page_cancel_page.setObjectName(u"delete_page_cancel_page")
        self.delete_page_cancel_page.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(117, 117, 117);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	border:none;\n"
"	height:40px;\n"
"	padding-left:10px;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	background-color:white;\n"
"	color:black;\n"
"	font-weight:bold;\n"
"}")
        self.delete_page_cancel_page.setCheckable(True)
        self.delete_page_cancel_page.setAutoExclusive(True)

        self.delete_user_cancel_buttons.addWidget(self.delete_page_cancel_page)

        self.splitter_2.addWidget(self.layoutWidget_3)
        self.stackedWidget.addWidget(self.delete_account_page)
        self.icon_name = QWidget(self.centralwidget)
        self.icon_name.setObjectName(u"icon_name")
        self.icon_name.setGeometry(QRect(0, 0, 175, 755))
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
"}"
"QPushButton:hover{\n"
"	background-color:white;\n"
"	color:grey;\n"
"	font-weight:bold;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:white;\n"
"	color:black;\n"
"	font-weight:bold;\n"
"}\n"

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

        self.withdraw_money = QPushButton(self.icon_name)
        self.withdraw_money.setObjectName(u"withdraw_money")
        self.withdraw_money.setCheckable(True)
        self.withdraw_money.setAutoExclusive(True)

        self.gridLayout.addWidget(self.withdraw_money, 4, 0, 1, 1)

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

        self.quit = QPushButton(self.icon_name)
        self.quit.setObjectName(u"quit")
        self.quit.setCheckable(True)
        self.quit.setAutoExclusive(True)

        self.gridLayout.addWidget(self.quit, 8, 0, 1, 1)

        self.delete_account = QPushButton(self.icon_name)
        self.delete_account.setObjectName(u"delete_account")
        self.delete_account.setEnabled(True)
        self.delete_account.setCheckable(True)
        self.delete_account.setAutoExclusive(True)

        self.gridLayout.addWidget(self.delete_account, 6, 0, 1, 1)

        self.open_account = QPushButton(self.icon_name)
        self.open_account.setObjectName(u"open_account")
        self.open_account.setCheckable(True)
        self.open_account.setAutoExclusive(True)

        self.gridLayout.addWidget(self.open_account, 5, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 300, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 7, 0, 1, 1)

        self.status_bar = QWidget(self.centralwidget)
        self.status_bar.setObjectName(u"status_bar")
        self.status_bar.setGeometry(QRect(203, 12, 901, 73))
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
        self.login_button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.login_button)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.quit.toggled.connect(MainWindow.close)
        self.delete_page_cancel_page.toggled.connect(self.accountt_info.toggle)
        self.cancel_page.toggled.connect(self.quit.toggle)
        self.back_account_info.toggled.connect(self.accountt_info.clicked)
        self.cancel_button_open_account.toggled.connect(self.accountt_info.toggle)

        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.account_info_label.setText(QCoreApplication.translate("MainWindow", u"Account Info", None))
        self.username_label_acc.setText(QCoreApplication.translate("MainWindow", u"User Account Number", None))
        self.username_field_acc.setPlaceholderText("")
        self.search_account_info.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.account_info_detail_label.setText(QCoreApplication.translate("MainWindow", u"Account Info", None))
        self.back_account_info.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.name_account_info_value.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.name_account_info.setText(QCoreApplication.translate("MainWindow", u"Username value", None))
        self.account_no_accinfo.setText(QCoreApplication.translate("MainWindow", u"Unique ID", None))
        self.account_no_value_accinfo.setText(QCoreApplication.translate("MainWindow", u"Account Number value", None))
        self.balance_account_info.setText(QCoreApplication.translate("MainWindow", u"Balance", None))
        self.balance_value_account_info_value.setText(QCoreApplication.translate("MainWindow", u"Balance", None))
        self.check_balance_label.setText(QCoreApplication.translate("MainWindow", u"Check Balance", None))
        self.value_label_check_balance.setText("")
        self.username_label_check_balance.setText(QCoreApplication.translate("MainWindow", u"User Account Number", None))
        self.username_field_check_balance.setPlaceholderText("")
        self.search_button_check_balance.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.add_money_label.setText(QCoreApplication.translate("MainWindow", u"Add Money", None))
        self.username_label_deposit.setText(QCoreApplication.translate("MainWindow", u"Account Number", None))
        self.username_field_deposit_value.setPlaceholderText("")
        self.amount_label_deposit.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.amount_field_deposit.setPlaceholderText("")
        self.status_label_add_money.setText("")
        self.deposit_button_deposit.setText(QCoreApplication.translate("MainWindow", u"Add Money", None))
        self.withdraw_money_label.setText(QCoreApplication.translate("MainWindow", u"Withdraw Money", None))
        self.username_label_withdraw.setText(QCoreApplication.translate("MainWindow", u"Account Number", None))
        self.username_field_withdraw_value.setPlaceholderText("")
        self.amount_label_withdraw.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.amount_field_withdraw.setPlaceholderText("")
        self.status_label_withdraw.setText("")
        self.deposit_button_withdraw.setText(QCoreApplication.translate("MainWindow", u"Withdraw", None))
        self.open_account_label.setText(QCoreApplication.translate("MainWindow", u"Open Account", None))
        self.account_no_accopen.setText(QCoreApplication.translate("MainWindow", u"Account number", None))
        self.balance_account_open.setText(QCoreApplication.translate("MainWindow", u"Balance", None))
        self.usernamename_account_open_label.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.picture_label_open_account.setText("")
        self.picture_button_open_account.setText(QCoreApplication.translate("MainWindow", u"Upload Picture", None))
        self.signature_upload_button_open_account.setText(QCoreApplication.translate("MainWindow", u"Signature", None))
        self.signature_label_open_account.setText("")
        self.status_label_open_account.setText("")
        self.open_button_open_account.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.cancel_button_open_account.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.login_label.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.username_label.setText(QCoreApplication.translate("MainWindow", u"  Username", None))
        self.username_field.setPlaceholderText("")
        self.password_label.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.password_field.setPlaceholderText("")
#if QT_CONFIG(accessibility)
        self.login_failed_text.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.login_failed_text.setText(QCoreApplication.translate("MainWindow", u"Login Failed", None))
        self.login_button_page.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.cancel_page.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.login_label_2.setText(QCoreApplication.translate("MainWindow", u"Delete Account", None))
        self.username_label_2.setText(QCoreApplication.translate("MainWindow", u"User Account Number", None))
        self.username_field_2.setPlaceholderText("")
#if QT_CONFIG(accessibility)
        self.login_failed_text_2.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.login_failed_text_2.setText("")
        self.delete_account_button_page.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.delete_page_cancel_page.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.name.setText(QCoreApplication.translate("MainWindow", u" Secure Banking", None))
        self.accountt_info.setText(QCoreApplication.translate("MainWindow", u"Account Info", None))
        self.withdraw_money.setText(QCoreApplication.translate("MainWindow", u"Withdraw ", None))
        self.balance.setText(QCoreApplication.translate("MainWindow", u"Balance", None))
        self.add_money.setText(QCoreApplication.translate("MainWindow", u"Deposit", None))
        self.quit.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.delete_account.setText(QCoreApplication.translate("MainWindow", u"Delete Account", None))
        self.open_account.setText(QCoreApplication.translate("MainWindow", u"Open Account", None))
        self.login_name_label.setText(QCoreApplication.translate("MainWindow", u"Welcome ", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

