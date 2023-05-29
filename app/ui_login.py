# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(821, 568)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        Login.setMinimumSize(QSize(821, 568))
        Login.setMaximumSize(QSize(821, 568))
        Login.setStyleSheet(u"background-color: rgb(38, 162, 105);")
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(100, 130, 621, 351))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(11)
        self.frame.setFont(font)
        self.frame.setMouseTracking(False)
        self.frame.setTabletTracking(False)
        self.frame.setFocusPolicy(Qt.StrongFocus)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0,0.2);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.getLogin = QLineEdit(self.frame)
        self.getLogin.setObjectName(u"getLogin")
        self.getLogin.setGeometry(QRect(210, 130, 201, 31))
        sizePolicy1.setHeightForWidth(self.getLogin.sizePolicy().hasHeightForWidth())
        self.getLogin.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.getLogin.setFont(font1)
        self.getLogin.setMouseTracking(False)
        self.getLogin.setAutoFillBackground(False)
        self.getLogin.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.getLogin.setInputMethodHints(Qt.ImhNone)
        self.getLogin.setFrame(True)
        self.getLogin.setDragEnabled(False)
        self.getLogin.setReadOnly(False)
        self.getLogin.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.getLogin.setClearButtonEnabled(True)
        self.getPass = QLineEdit(self.frame)
        self.getPass.setObjectName(u"getPass")
        self.getPass.setGeometry(QRect(210, 200, 201, 31))
        sizePolicy1.setHeightForWidth(self.getPass.sizePolicy().hasHeightForWidth())
        self.getPass.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        self.getPass.setFont(font2)
        self.getPass.setAutoFillBackground(False)
        self.getPass.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.getPass.setEchoMode(QLineEdit.Password)
        self.getPass.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.getPass.setClearButtonEnabled(True)
        self.button = QPushButton(self.frame)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(250, 270, 121, 31))
        font3 = QFont()
        font3.setFamilies([u"KacstDecorative"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.button.setFont(font3)
        self.button.setCursor(QCursor(Qt.PointingHandCursor))
        self.button.setMouseTracking(True)
        self.button.setTabletTracking(False)
        self.button.setFocusPolicy(Qt.StrongFocus)
        self.button.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.button.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"\n"
"	border-radius:10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(0,0,0);\n"
"	\n"
"	background-color: rgb(222, 221, 218);\n"
"\n"
"}")
        self.button.setAutoDefault(False)
        self.button.setFlat(False)
        self.user_img = QLabel(self.frame)
        self.user_img.setObjectName(u"user_img")
        self.user_img.setGeometry(QRect(160, 120, 41, 41))
        sizePolicy1.setHeightForWidth(self.user_img.sizePolicy().hasHeightForWidth())
        self.user_img.setSizePolicy(sizePolicy1)
        self.user_img.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.user_img.setPixmap(QPixmap(u"../sources/user.png"))
        self.user_img.setScaledContents(True)
        self.pass_img = QLabel(self.frame)
        self.pass_img.setObjectName(u"pass_img")
        self.pass_img.setGeometry(QRect(160, 190, 41, 41))
        sizePolicy1.setHeightForWidth(self.pass_img.sizePolicy().hasHeightForWidth())
        self.pass_img.setSizePolicy(sizePolicy1)
        self.pass_img.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.pass_img.setPixmap(QPixmap(u"../sources/pass.png"))
        self.pass_img.setScaledContents(True)
        self.access_img = QLabel(self.frame)
        self.access_img.setObjectName(u"access_img")
        self.access_img.setGeometry(QRect(220, 10, 171, 91))
        sizePolicy1.setHeightForWidth(self.access_img.sizePolicy().hasHeightForWidth())
        self.access_img.setSizePolicy(sizePolicy1)
        self.access_img.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.access_img.setPixmap(QPixmap(u"../sources/logo_login.png"))
        self.access_img.setScaledContents(True)
        self.label_erro = QLabel(self.frame)
        self.label_erro.setObjectName(u"label_erro")
        self.label_erro.setGeometry(QRect(200, 240, 210, 17))
        font4 = QFont()
        font4.setBold(True)
        self.label_erro.setFont(font4)
        self.label_erro.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_erro.setAlignment(Qt.AlignCenter)
        self.getLogin.raise_()
        self.getPass.raise_()
        self.user_img.raise_()
        self.pass_img.raise_()
        self.button.raise_()
        self.access_img.raise_()
        self.label_erro.raise_()
        self.ufes_label = QLabel(Login)
        self.ufes_label.setObjectName(u"ufes_label")
        self.ufes_label.setGeometry(QRect(300, 500, 261, 51))
        sizePolicy1.setHeightForWidth(self.ufes_label.sizePolicy().hasHeightForWidth())
        self.ufes_label.setSizePolicy(sizePolicy1)
        self.ufes_label.setStyleSheet(u"")
        self.ufes_label.setPixmap(QPixmap(u"../sources/logo_ufes.png"))
        self.ufes_label.setScaledContents(True)
        self.visao_label = QLabel(Login)
        self.visao_label.setObjectName(u"visao_label")
        self.visao_label.setEnabled(True)
        self.visao_label.setGeometry(QRect(30, 10, 781, 101))
        sizePolicy1.setHeightForWidth(self.visao_label.sizePolicy().hasHeightForWidth())
        self.visao_label.setSizePolicy(sizePolicy1)
        self.visao_label.setPixmap(QPixmap(u"../sources/logo_visao.png"))
        self.visao_label.setScaledContents(True)
        QWidget.setTabOrder(self.getLogin, self.getPass)
        QWidget.setTabOrder(self.getPass, self.button)
        QWidget.setTabOrder(self.button, self.frame)

        self.retranslateUi(Login)

        self.button.setDefault(False)


        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.getLogin.setInputMask("")
        self.getLogin.setText("")
        self.getLogin.setPlaceholderText(QCoreApplication.translate("Login", u"Usu\u00e1rio", None))
        self.getPass.setInputMask("")
        self.getPass.setText("")
        self.getPass.setPlaceholderText(QCoreApplication.translate("Login", u"Senha", None))
        self.button.setText(QCoreApplication.translate("Login", u"Login", None))
        self.user_img.setText("")
        self.pass_img.setText("")
        self.access_img.setText("")
        self.label_erro.setText("")
        self.ufes_label.setText("")
        self.visao_label.setText("")
    # retranslateUi

