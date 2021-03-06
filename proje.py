# Imports for PyQt5 Lib and Functions to be used
# -*- coding: utf-8 -*-
import sys
import os, io
import logging
import json, requests
from cevapVer import Chat
from datetime import datetime
from PyQt5.QtSql import QSqlDatabase
from sqlDialog import SqlKonusmaModeli
from cevapVer import pairs, reflections
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir, QFile, Qt, QSize
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QDesktopWidget, QMainWindow, QAbstractItemView, \
    QVBoxLayout, QLayout, QHBoxLayout
from PyQt5.QtWebEngineWidgets import *
from os import listdir
from os.path import isfile, join

logging.basicConfig(filename="chat.log", level=logging.DEBUG)
logger = logging.getLogger("logger")


# region Veritabanı bağlantı işlemleri
def veritabaniBaglan():
    veritabani = QSqlDatabase.database()
    if not veritabani.isValid():
        veritabani = QSqlDatabase.addDatabase("QSQLITE")
        if not veritabani.isValid():
            logger.error("Veritabanı Eklenemedi !")

    yaz_dir = QDir()
    if not yaz_dir.mkpath("."):
        logger.error("Yazılabilir dizin oluşturulamadı !")

    # Erişilebilir bir veritabanı dosyası oluşturulmuştur.
    dosyaAdi = "{}/chat-database.sqlite3".format(yaz_dir.absolutePath())

    # Veritabanı mevcut değilse open() fonksiyonu SQLite'ı oluşturacaktır.
    veritabani.setDatabaseName(dosyaAdi)
    if not veritabani.open():
        logger.error("Veritabanı Açılamadı")
        QFile.remove(dosyaAdi)


# endregion

# region interfaceCodes

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 754)
        MainWindow.setMinimumSize(QtCore.QSize(1330, 750))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #394b58;")  # TODO:
        self.frame_show = QtWidgets.QFrame(self.centralwidget)
        self.frame_show.setGeometry(QtCore.QRect(130, 30, 261, 261))
        self.frame_show.setStyleSheet("")
        self.frame_show.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_show.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_show.setObjectName("frame_show")
        MainWindow.setCentralWidget(self.centralwidget)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftMenuLayout = QtWidgets.QVBoxLayout()
        self.leftMenuLayout.setObjectName("leftMenuLayout")
        self.horizontalLayout.addLayout(self.leftMenuLayout)
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.treeView.setMinimumSize(QtCore.QSize(341, 500))
        self.treeView.setMaximumSize(QtCore.QSize(341, 16777215))
        self.treeView.setStyleSheet("QTreeView {\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "    border: 1px solid;\n"
                                    "    border-color: rgb(255, 255, 255);\n"
                                    "    border-radius: 8px 8px 8px 8px;\n"
                                    "    padding: 10px;\n"
                                    "    outline: 0px;\n"
                                    "    font:   rgb(255, 255, 255);\n"
                                    "    font:  16pt \"MS Shell Dlg 2\";\n"
                                    "}\n"
                                    "\n"
                                    "QTreeView::item {\n"
                                    "         border-radius: 10px 10px 10px 10px;       \n"
                                    "         border: 3px solid  rgb(0, 170, 255);                \n"
                                    "         height: 50px;                            \n"
                                    "         padding-left: 20px;                      \n"
                                    "         margin:10px;       \n"
                                    "          /*#B3E5FC;#b9e6fb;   */\n"
                                    "         background-color:  #b9e6fb;\n"
                                    "         color: rgb(0, 170, 255);      \n"
                                    "    }\n"
                                    "\n"
                                    "QTreeView::item::hover {\n"
                                    "       background-color:  rgb(255, 255, 255);\n"
                                    "}\n"
                                    "\n"
                                    "QTreeView::branch:has-siblings:!adjoins-item {\n"
                                    "    border-image: url(images/vline.png) 0;\n"
                                    "}\n"
                                    "\n"
                                    "QTreeView::branch:has-siblings:adjoins-item {\n"
                                    "    border-image: url(images/branch-more.png) 0;\n"
                                    "}\n"
                                    "\n"
                                    "QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
                                    "    border-image: url(images/branch-end.png) 0;\n"
                                    "}\n"
                                    "\n"
                                    "QTreeView::branch:has-children:!has-siblings:closed,\n"
                                    "QTreeView::branch:closed:has-children:has-siblings {\n"
                                    "        border-image: none;\n"
                                    "        image: url(images/branch-closed.png);\n"
                                    "}\n"
                                    "\n"
                                    "QTreeView::branch:open:has-children:!has-siblings,\n"
                                    "QTreeView::branch:open:has-children:has-siblings  {\n"
                                    "        border-image: none;\n"
                                    "        image: url(images/branch-open.png);\n"
                                    "}\n"
                                    "\n"
                                    "QTreeView::item:!has-children{\n"
                                    "\n"
                                    "      border-radius: 0px 0px 0px 0px;\n"
                                    "      border:3px solid  #e7a61a;  \n"
                                    "      height: 50px;\n"
                                    "      padding-left: 20px;                      \n"
                                    "      margin:10px;                      \n"
                                    "      background-color: #e7a61a;        \n"
                                    "      color: rgb(255, 255, 255);\n"
                                    "\n"
                                    "}\n"
                                    "QTreeView::item:!has-children::hover {\n"
                                    "      border-radius: 0px 0px 0px 0px;\n"
                                    "      border: 3px solid #e7a61a;\n"
                                    "      height: 50px;                        \n"
                                    "      padding-left: 20px;                      \n"
                                    "      margin:10px;                      \n"
                                    "      background-color:  rgb(255, 255, 255); \n"
                                    "      color: #e7a61a;\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "")
        self.treeView.setItemsExpandable(True)
        self.treeView.setObjectName("treeView")
        self.horizontalLayout.addWidget(self.treeView)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit_kodBlogu = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_kodBlogu.setMinimumSize(QtCore.QSize(500, 100))
        self.textEdit_kodBlogu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textEdit_kodBlogu.setStyleSheet("border: 1px solid;\n"
                                             "font: 16pt \"MS Shell Dlg 2\";\n"
                                             "border-radius: 8px 8px 8px 8px;\n"
                                             "background-color: palette(base);\n"
                                             "color: rgb(102, 102, 102);\n"
                                             "border-color: rgb(255, 255, 255);")
        self.textEdit_kodBlogu.setLineWidth(1)
        self.textEdit_kodBlogu.setObjectName("textEdit_kodBlogu")
        self.verticalLayout.addWidget(self.textEdit_kodBlogu)
        self.textEdit_console = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_console.setMinimumSize(QtCore.QSize(500, 0))
        self.textEdit_console.setMaximumSize(QtCore.QSize(16777215, 200))
        self.textEdit_console.setStyleSheet("border: 1px solid;\n"
                                            "font: 16pt \"MS Shell Dlg 2\";\n"
                                            "border-radius: 8px 8px 8px 8px;\n"
                                            "background-color: palette(base);\n"
                                            "color: rgb(170, 0, 127);\n"
                                            "border-color: rgb(255, 255, 255);")
        self.textEdit_console.setObjectName("textEdit_console")
        self.verticalLayout.addWidget(self.textEdit_console)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.frame_sagMenuParent = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_sagMenuParent.sizePolicy().hasHeightForWidth())
        self.frame_sagMenuParent.setSizePolicy(sizePolicy)
        self.frame_sagMenuParent.setMinimumSize(QtCore.QSize(325, 0))
        self.frame_sagMenuParent.setMaximumSize(QtCore.QSize(325, 16777215))
        self.frame_sagMenuParent.setStyleSheet("background-color: #cad7e0;\n"                                            "    border-radius: 8px 8px 8px 8px;")
        self.frame_sagMenuParent.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sagMenuParent.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sagMenuParent.setObjectName("frame_sagMenuParent")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_sagMenuParent)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_sagMenu = QtWidgets.QVBoxLayout()
        self.verticalLayout_sagMenu.setObjectName("verticalLayout_sagMenu")
        self.frame_sagMenu2 = QtWidgets.QFrame(self.frame_sagMenuParent)
        self.frame_sagMenu2.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_sagMenu2.setStyleSheet("background-color: #008efe;")
        self.frame_sagMenu2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sagMenu2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sagMenu2.setObjectName("frame_sagMenu2")
        self.label_robot = QtWidgets.QLabel(self.frame_sagMenu2)
        self.label_robot.setGeometry(QtCore.QRect(20, 0, 91, 71))
        self.label_robot.setStyleSheet("image: url(images/robot.png);\n"
                                       "background-color: transparent;")
        self.label_robot.setText("")
        self.label_robot.setObjectName("label_robot")
        self.verticalLayout_sagMenu.addWidget(self.frame_sagMenu2)
        self.textEdit_message = QtWidgets.QTextEdit(self.frame_sagMenuParent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_message.sizePolicy().hasHeightForWidth())
        self.textEdit_message.setSizePolicy(sizePolicy)
        self.textEdit_message.setMinimumSize(QtCore.QSize(300, 200))
        self.textEdit_message.setStyleSheet("font-family: \"Verdana\"; \n"
                                            "    font-size: 10pt; \n"
                                            "    font-weight: 475;\n"
                                            "    text-align: right;   \n"
                                            "    background-color: #cad7e0;\n"
                                            "    border:0;  /* kenarlık olmasın */\n"
                                            "")
        self.textEdit_message.setObjectName("textEdit_message")
        self.verticalLayout_sagMenu.addWidget(self.textEdit_message)
        self.frame_sagMenu3 = QtWidgets.QFrame(self.frame_sagMenuParent)
        self.frame_sagMenu3.setMinimumSize(QtCore.QSize(0, 75))
        self.frame_sagMenu3.setStyleSheet("    background-color: #cad7e0 ;\n")
        self.frame_sagMenu3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sagMenu3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sagMenu3.setObjectName("frame_sagMenu3")
        self.lineEdit_sendMessage = QtWidgets.QLineEdit(self.frame_sagMenu3)
        self.lineEdit_sendMessage.setGeometry(QtCore.QRect(0, 20, 307, 55))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_sendMessage.sizePolicy().hasHeightForWidth())
        self.lineEdit_sendMessage.setSizePolicy(sizePolicy)
        self.lineEdit_sendMessage.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_sendMessage.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_sendMessage.setStyleSheet("    font-family: \"Verdana\";\n"
                                                "    font-size: 10pt;\n"
                                                "    font-weight: 475; \n"
                                                "    text-align: left;\n"
                                                "    background-color: #ffffff;\n"
                                                "    border:0;  /* kenarlık olmasın */\n"
                                                "    height: 33px; /* metin kutusunun yüksekliği yazı boyutundan daha fazla olsun */\n"
                                                "    border-radius: 25px 25px 25px 25px;\n"
                                                "padding-left:70px;")
        self.lineEdit_sendMessage.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_sendMessage.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lineEdit_sendMessage.setObjectName("lineEdit_sendMessage")
        self.pushButton_smile = QtWidgets.QPushButton(self.frame_sagMenu3)
        self.pushButton_smile.setGeometry(QtCore.QRect(0, 18, 60, 60))
        self.pushButton_smile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_smile.setStyleSheet("background-color: transparent;")
        self.pushButton_smile.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/happy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_smile.setIcon(icon)
        self.pushButton_smile.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_smile.setObjectName("pushButton_smile")
        self.verticalLayout_sagMenu.addWidget(self.frame_sagMenu3)
        self.gridLayout_2.addLayout(self.verticalLayout_sagMenu, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_sagMenuParent, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_sagMenuParent)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 70))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit_searchEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit_searchEdit.setGeometry(QtCore.QRect(10, 10, 283, 45))
        self.textEdit_searchEdit.setStyleSheet("border: 1px solid;\n"
                                               "font: 16pt \"MS Shell Dlg 2\";\n"
                                               "border-color: rgb(156, 156, 156);\n"
                                               "border-radius: 8px 8px 8px 8px;\n"
                                               "background-color: palette(base);\n"
                                               "color: rgb(102, 102, 102)")
        self.textEdit_searchEdit.setObjectName("textEdit_searchEdit")
        self.pushButton_searchEdit = QtWidgets.QPushButton(self.frame)
        self.pushButton_searchEdit.setGeometry(QtCore.QRect(293, 10, 50, 45))
        self.pushButton_searchEdit.setStyleSheet("background-image:url(search.png);\n"
                                                 "background-repeat: no-repeat;\n")
        self.pushButton_searchEdit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_searchEdit.setIcon(icon)
        self.pushButton_searchEdit.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_searchEdit.setObjectName("pushButton_searchEdit")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(360, -11, 261, 91))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_add = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_add.setStyleSheet("QPushButton {\n"
                                          "    background-color: transparent;\n"
                                          "    background-repeat: no-repeat;\n"
                                          " }")
        self.pushButton_add.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/add_dark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_add.setIcon(icon1)
        self.pushButton_add.setIconSize(QtCore.QSize(64, 64))
        self.pushButton_add.setCheckable(True)
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout_2.addWidget(self.pushButton_add)
        self.pushButton_document = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_document.setStyleSheet("background-color: transparent;\n"
                                               "background-repeat: no-repeat;")
        self.pushButton_document.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/document_dark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_document.setIcon(icon2)
        self.pushButton_document.setIconSize(QtCore.QSize(64, 64))
        self.pushButton_document.setCheckable(True)
        self.pushButton_document.setObjectName("pushButton_document")
        self.horizontalLayout_2.addWidget(self.pushButton_document)
        self.pushButton_play = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_play.setStyleSheet("background-color: transparent;\n"
                                           "background-repeat: no-repeat;\n")
        self.pushButton_play.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/play_dark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_play.setIcon(icon3)
        self.pushButton_play.setIconSize(QtCore.QSize(64, 64))
        self.pushButton_play.setCheckable(True)
        self.pushButton_play.setObjectName("pushButton_play")
        self.horizontalLayout_2.addWidget(self.pushButton_play)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)
        self.frame_header = QtWidgets.QFrame(self.centralwidget)
        self.frame_header.setMinimumSize(QtCore.QSize(0, 115))
        self.frame_header.setStyleSheet("background-color:  #394b58;")
        self.frame_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_header.setObjectName("frame_header")
        self.label_baslik = QtWidgets.QLabel(self.frame_header)
        self.label_baslik.setGeometry(QtCore.QRect(-695, 30, 1721, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_baslik.sizePolicy().hasHeightForWidth())
        self.label_baslik.setSizePolicy(sizePolicy)
        self.label_baslik.setMaximumSize(QtCore.QSize(16777215, 111))
        self.label_baslik.setStyleSheet("image: url(images/pynar_yazi.png);\n")
        self.label_baslik.setText("")
        self.label_baslik.setObjectName("label_baslik")
        self.label_logo = QtWidgets.QLabel(self.frame_header)
        self.label_logo.setGeometry(QtCore.QRect(6, -10, 100, 131))
        self.label_logo.setStyleSheet("image: url(images/pynar_image.png);")
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.gridLayout.addWidget(self.frame_header, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.treeView.setWhatsThis(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" font-size:48pt; font-weight:600;\">asasas</span></p></body></html>"))
        self.textEdit_kodBlogu.setHtml(_translate("MainWindow",
                                                  "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                  "p, li { white-space: pre-wrap; }\n"
                                                  "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_console.setHtml(_translate("MainWindow",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&gt;&gt;&gt;</p></body></html>"))

ballon = """
<table border="0" cellpadding="0" cellspacing="0">
      <tr>
         <td><img src="images/sol_ust_beyaz.gif"></td>
         <td bgcolor="#ffffff"></td>
         <td><img src="images/sag_ust_beyaz.gif"></td>
		 <td width="40"><img src="images/transparent.gif"></td>
      </tr>
      <tr>
         <td background="images/sol_orta_beyaz.gif">&nbsp;</td>
         <td bgcolor="#ffffff" style="">{}<div align="right" style="font-size: 9px;color: #1BA44C;">{}</div></td>
         <td bgcolor="#ffffff">&nbsp;</td>
		 <td width="40"><img src="images/transparent.gif"></td>
      </tr>
      <tr>
         <td><img src="images/sol_alt_beyaz.gif"></td>
         <td bgcolor="#ffffff"><img src="images/transparent.gif"></td>
         <td><img src="images/sag_alt_beyaz.gif"></td>
		 <td width="40"><img src="images/transparent.gif"></td>
      </tr>
</table>
"""

ballon_Kullanici = """
<table border="0" cellpadding="0" cellspacing="0" align="right">
      <tr>
         <td width="40"><img src="images/transparent.gif"></td>
		 <td><img src="images/sol_ust_yesil.gif"></td>
         <td bgcolor="#e9fedd"><img src="images/transparent.gif"></td>
         <td><img src="images/sag_ust_yesil.gif"></td>
      </tr>
      <tr >
		 <td width="40"><img src="images/transparent.gif"></td>
         <td bgcolor="#e9fedd">&nbsp;</td>
         <td bgcolor="#e9fedd" style="">{}<div align="right" style="font-size: 9px;color: #1BA44C;">{}</div></td>
         </td>
         <td background="images/sag_orta_yesil.gif">&nbsp;</td>
      </tr>
      <tr>
		 <td width="40"><img src="images/transparent.gif"></td>
         <td><img src="images/sol_alt_yesil.gif"></td>
         <td bgcolor="#e9fedd"><img src="images/transparent.gif"></td>
         <td><img src="images/sag_alt_yesil.gif"></td>
      </tr>
</table>
"""
import icons_rc
# endregion


class SecondWindow(QtWidgets.QDialog):
    def __init__(self):
        super(SecondWindow, self).__init__()
        self.setUI()

    def setUI(self):
        centerPoint = QDesktopWidget().availableGeometry().center()
        self.setGeometry(centerPoint.x() - 180, centerPoint.y() + 96, 270, 157)
        self.setMinimumSize(QSize(270, 157))
        self.setMaximumSize(QSize(270, 157))
        self.setWindowTitle("Emojiler")
        self.setWindowIcon(QIcon('images/smile.png'))
        """
            Emojiye tıklanıldığında fonksiyon, emojinin karşılığını password adında görünmeyen bir label'a yazıyor. Dialog bittiğinde ise
            label'daki yazı userinput'a gönderiliyor. Farklı yollar denedik. Direkt olarak butona tıklandığında ana pencere sınıfına ulaşıp orada
            setText yapmayı denedik ama userinput değiştiği halde ekrana yazdırmıyordu. Userinputun değiştiğini ise konsola yazdırarak kontrol etmiştik.
            Signal kullanmayı da denedik. Emojiye tıklanıldığında direkt kapanmasından dolayı QDialog kullanmaya karar verdik.
        """

        self.password = QtWidgets.QLineEdit(self)
        self.password.setGeometry(200, 300, 50, 30)
        self.gulucuk = QPushButton(self)
        self.gulucuk.setStyleSheet(
            "background-image: url(images/smile.png);background-repeat: no-repeat;border: none;outline: none;")
        self.gulucuk.setGeometry(5, 5, 70, 60)
        self.gulucuk.clicked.connect(self.gulucukKoy)
        self.uzgun = QPushButton(self)
        self.uzgun.setStyleSheet(
            "background-image: url(images/uzgun.png);background-repeat: no-repeat;border: none;outline: none;")
        self.uzgun.setGeometry(95, 5, 70, 60)
        self.uzgun.clicked.connect(self.uzgunSuratKoy)
        self.gulme = QPushButton(self)
        self.gulme.setStyleSheet(
            "background-image: url(images/gulme.png);background-repeat: no-repeat;border: none;outline: none;")
        self.gulme.setGeometry(185, 5, 70, 60)
        self.gulme.clicked.connect(self.gul)

        self.gozKirpma = QPushButton(self)
        self.gozKirpma.setStyleSheet(
            "background-image: url(images/kırp.png);background-repeat: no-repeat;border: none;outline: none;")
        self.gozKirpma.setGeometry(5, 80, 70, 60)
        self.gozKirpma.clicked.connect(self.gozKirp)
        self.duzSurat = QPushButton(self)
        self.duzSurat.setStyleSheet(
            "background-image: url(images/duz.png);background-repeat: no-repeat;border: none;outline: none;")
        self.duzSurat.setGeometry(95, 80, 70, 60)
        self.duzSurat.clicked.connect(self.duzSuratKoy)
        self.sasirma = QPushButton(self)
        self.sasirma.setStyleSheet(
            "background-image: url(images/sasirma.png);background-repeat: no-repeat;border: none;outline: none;")
        self.sasirma.setGeometry(185, 80, 70, 60)
        self.sasirma.clicked.connect(self.sasirmaKoy)

    def gulucukKoy(self):
        self.password.setText(":) ")
        self.accept()

    def gul(self):
        self.password.setText(":D ")
        self.accept()

    def uzgunSuratKoy(self):
        self.password.setText(":( ")
        self.accept()

    def sasirmaKoy(self):
        self.password.setText(":O ")
        self.accept()

    def duzSuratKoy(self):
        self.password.setText(":| ")
        self.accept()

    def gozKirp(self):
        self.password.setText(";) ")
        self.accept()


class WebEngineViewWindow(QWidget):
    def __init__(self, data):
        super().__init__()
        layout = QVBoxLayout()
        view = QWebEngineView()
        view.load(QtCore.QUrl.fromLocalFile(os.getcwd() + '/HtmlDescriptions/' + data))
        self.setWindowTitle("Yardım")
        self.setWindowIcon(QIcon('images/help.png'))
        layout.addWidget(view)
        self.setLayout(layout)


class MenuButton(QtWidgets.QPushButton):
    moveSignal = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(MenuButton, self).__init__(*args, **kwargs)
        self.setFixedHeight(50)


class Project(QMainWindow):
    childNodes = []
    colors = ['#7fc97f', '#beaed4', '#fdc086', '#ffff99', '#386cb0', '#f0027f', '#bf5b17', '#666666']
    words = ["abs", "print", "while", "max", "for"]
    descriptions = []
    jsonFiles = []

    def __init__(self):
        super().__init__()
        self.activeMenu = 1
        self.toolButtons = {}
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        path = os.path.abspath('HtmlDescriptions')
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        self.descriptions = onlyfiles

        # self.ReadFromJsonApi()  #Eğer Json datayı bir web sayfasından almak isterse kullanılabilir.
        self.ReadFromFile('temelkomutlar.json')
        self.show()
        self.ui.treeView.setDragDropMode(QAbstractItemView.DragOnly)
        self.ui.treeView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.treeView.clicked.connect(self.expanded)
        self.ui.pushButton_play.pressed.connect(self.PlayButtonPressed)
        self.ui.pushButton_play.released.connect(self.PlayButtonReleased)
        self.ui.pushButton_add.pressed.connect(self.AddButtonPressed)
        self.ui.pushButton_add.released.connect(self.AddButtonReleased)
        self.ui.pushButton_smile.clicked.connect(self.emojiPage)
        self.ui.pushButton_document.pressed.connect(self.DocumentButtonPressed)
        self.ui.pushButton_document.released.connect(self.DocumentButtonReleased)
        self.ui.pushButton_play.clicked.connect(self.PlayButtonClick)
        self.ui.pushButton_add.clicked.connect(self.AddButtonClick)
        self.ui.pushButton_document.clicked.connect(self.DocumentButtonClick)
        self.ui.pushButton_searchEdit.clicked.connect(self.SearchButtonClick)
        self.setAcceptDrops(True)
        now = datetime.now()
        zaman = now.strftime("%H:%M")
        karsilama_metni = "Nasıl yardımcı olabilirim?"
        karsilama = ballon.format(karsilama_metni, zaman)
        self.ui.textEdit_message.append(karsilama)
        self.ui.textEdit_message.append("\n")
        self.ui.textEdit_message.setReadOnly(True)
        self.setWindowTitle("Python Kod Editörü")
        self.setWindowIcon(QIcon('images/logo.png'))
        self.ui.lineEdit_sendMessage.returnPressed.connect(self.AddToChatLogUser)
        self.ui.lineEdit_sendMessage.setEnabled(True)
        self.ui.lineEdit_sendMessage.setFocus()
        self.ui.treeView.setColumnWidth(0, 329)
        icon = QIcon('images/up.png')
        self.upBtn = MenuButton(icon=icon)
        self.upBtn.setIconSize(QSize(50, 50))
        self.upBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.upBtn.moveSignal.connect(self.moveUp)
        self.upBtn.setStyleSheet("QPushButton {background-color: rgb(0,170,255); border:none}"
                                 "QPushButton:hover {background-color: rgb(0,76,219); border:none}")
        icon = QIcon('images/down.png')
        self.downBtn = MenuButton(icon=icon)
        self.downBtn.setIconSize(QSize(50, 50))
        self.downBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.downBtn.moveSignal.connect(self.moveDown)
        self.downBtn.setStyleSheet("QPushButton {background-color: rgb(0,170,255); border:none}"
                                   "QPushButton:hover {background-color: rgb(0,76,219); border:none}")

        self.listWidget = QtWidgets.QListWidget()
        self.listWidget.setStyleSheet("background-color: #394b58; border:none; ")
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setFixedWidth(120)
        self.FillMenuCategories()
        self.listWidget.setCurrentRow(self.activeMenu)
        self.MenuActionClick(self.jsonFiles[self.activeMenu - 1], self.activeMenu)
        self.ui.leftMenuLayout.addWidget(self.upBtn)
        self.ui.leftMenuLayout.addWidget(self.listWidget)
        self.ui.leftMenuLayout.addWidget(self.downBtn)
        self.downBtn.clicked.connect(self.moveDown)
        self.upBtn.clicked.connect(self.moveUp)


    """Kategorilerin bulunduğu toolbarda yukarı ilerlemeyi sağlar"""
    @QtCore.pyqtSlot()
    def moveUp(self):
        ix = self.listWidget.moveCursor(QtWidgets.QAbstractItemView.MoveUp, QtCore.Qt.NoModifier)
        self.listWidget.setCurrentIndex(ix)
        if 1 < self.activeMenu:
            self.toolButtons[self.activeMenu].setStyleSheet(
                "background-color: #394b58; color: white; font: 14pt; padding-top:10px;")
            self.activeMenu = self.activeMenu - 1
            self.toolButtons[self.activeMenu].setStyleSheet(
                "background-color: #6b899f; color: white; font: 14pt; padding-top:10px;")
            self.MenuActionClick(self.jsonFiles[self.activeMenu - 1], self.activeMenu)

    """Kategorilerin bulunduğu toolbarda aşağı ilerlemeyi sağlar"""
    @QtCore.pyqtSlot()
    def moveDown(self):

        if self.menuItemCount > self.activeMenu:
            self.toolButtons[self.activeMenu].setStyleSheet(
                "background-color: #394b58; color: white; font: 14pt; padding-top:10px;")
            self.activeMenu = self.activeMenu + 1
            self.toolButtons[self.activeMenu].setStyleSheet(
                "background-color: #6b899f; color: white; font: 14pt; padding-top:10px;")
            self.listWidget.setCurrentRow(self.activeMenu - 1)
            self.MenuActionClick(self.jsonFiles[self.activeMenu - 1], self.activeMenu)

    def emojiPage(self):
        self.SW = SecondWindow()
        if self.SW.exec_():
            self.ui.lineEdit_sendMessage.setText(self.ui.lineEdit_sendMessage.text() + " " + self.SW.password.text())
        self.ui.lineEdit_sendMessage.setFocus()

    def UpdateCycle(self):
        """Retrieves a new bot message and appends to the chat log."""
        bmsg = self.v.getBotMessage()
        self.chatlog.setAlignment(Qt.AlignRight)
        [self.chatlog.append(m) for m in bmsg]
        self.userinput.setFocus()

    def ReplaceToEmoji(self, message):
        newMessage = message
        if ":)" in message:
            newMessage = newMessage.replace(':)', ' &#128522; ')
        if ":(" in message:
            newMessage = newMessage.replace(':(', ' &#128542; ')
        if ":D" in message:
            newMessage = newMessage.replace(':D', ' &#128516; ')
        if ":O" in message:
            newMessage = newMessage.replace(':O', ' &#128558; ')
        if ";)" in message:
            newMessage = newMessage.replace(';)', ' &#128521; ')
        if ":|" in message:
            newMessage = newMessage.replace(':|', ' &#128528; ')
        return newMessage

    def AddToChatLogUser(self):
        """Takes guest's entry and appends to the chatlog"""
        message = self.ui.lineEdit_sendMessage.text()
        if message != '':
            umsg = Chat(message, pairs, reflections)
            umsg.converse(message, quit='tamam')
            SqlSpeakModel.mesaj_ekle(message, umsg.__repr__())
            self.ui.textEdit_message.setAlignment(Qt.AlignLeft)
            now = datetime.now()
            zaman = now.strftime("%H:%M")
            ballonmesaj = ballon.format(umsg.__repr__(), zaman)
            splitting = self.ReplaceToEmoji(message)
            ballonKullanici = ballon_Kullanici.format(splitting, zaman)
            self.ui.textEdit_message.append(ballonKullanici)
            self.ui.textEdit_message.append("\n")
            self.ui.textEdit_message.setAlignment(Qt.AlignRight)
            self.ui.textEdit_message.append(ballonmesaj)
            self.ui.textEdit_message.append("\n")
            self.ui.textEdit_message.moveCursor(QtGui.QTextCursor.End)
            self.ui.lineEdit_sendMessage.setText("")

    # region TreeviewOperations
    def expanded(self, index):
        keyVal = index.data() + ".html"
        if keyVal in self.descriptions:
            self.pencere = WebEngineViewWindow(keyVal)
            self.pencere.show()

    def dragEnterEvent(self, event):
        event.accept()

    def dragMoveEvent(self, event):
        for ix in self.ui.treeView.selectedIndexes():
            text = ix.data(Qt.DisplayRole)
        if text in self.childNodes:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for ix in self.ui.treeView.selectedIndexes():
            text = ix.data(Qt.DisplayRole)  # or ix.data()
            self.colorTheText(text)

    def colorTheText(self, text):
        data = text.replace('<', "&lt;")
        data = data.replace("(", "<span style=\"color:#0000ff;\">(</span>")
        data = data.replace(")", "<span style=\" color:#0000ff;\">)</span>")
        data = data.replace("\n", "<br/>")

        for word in self.words:
            data = data.replace(word, "<span style=\" color:#aa007f;\">" + word + "</span>")
        data = data.replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;")
        self.ui.textEdit_kodBlogu.append(data)

    def ReadFromFile(self, dosya):
        with open(os.path.abspath('JsonFiles/' + dosya), encoding='utf-8') as f:
            data = json.load(f)
        model = QStandardItemModel(0, 1, self.ui.treeView)
        model.setHeaderData(0, Qt.Horizontal, None)
        self.ui.treeView.setModel(model)
        self.TreeViewFill(model, data)

    def FillMenuCategories(self):
        with open(os.path.abspath('JsonFiles/Menus.json'), encoding='utf-8') as f:
            leftMenuJson = json.load(f)
        i = 1
        self.menuItemCount = len(leftMenuJson.items())
        for root, children in leftMenuJson.items():
            item = QtWidgets.QListWidgetItem()
            widget = QWidget()
            jsonfile = children['jsonfile']
            self.jsonFiles.append(children['jsonfile'])
            self.toolButtons[i] = toolButton = QtWidgets.QToolButton()
            toolButton.setStyleSheet(
                "QToolButton {background-color: #394b58; color: white; font: 14pt; padding-top:10px;}\n"
                "QToolButton:hover {background-color: #6b899f; color: white; font: 14pt; padding-top:10px;}\n")
            toolButton.setFixedWidth(120)
            toolButton.setFixedHeight(134)
            self.toolButtons[1].setStyleSheet("background-color: #6b899f; color: white; font: 14pt; padding-top:10px;")
            self.activeMenu = 1
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(children['icon']), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            toolButton.setIconSize(QtCore.QSize(50, 50))
            toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
            toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            toolButton.setIcon(icon)
            toolButton.setText(root)
            self.toolButtons[i].clicked.connect(
                lambda checked, index=i, jsonfile=jsonfile: self.MenuActionClick(jsonfile, index))
            toolButton.setObjectName("toolButton")
            toolButton.raise_()

            widgetLayout = QHBoxLayout()
            widgetLayout.addWidget(toolButton)
            widgetLayout.addStretch()
            widgetLayout.setSizeConstraint(QLayout.SetFixedSize)
            widgetLayout.setContentsMargins(0, 0, 0, 0)
            widget.setLayout(widgetLayout)
            item.setSizeHint(widget.sizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, widget)
            i = i + 1

    def ReadFromJsonApi(self):
        payload = [{"__class__": "ServerRequest", "requestData": [], "requestClass": "TradeService",
                    "requestMethod": "getTradeOffers", "requestId": 83}]
        res = requests.request(method='GET', url='https://api.mocki.io/v1/ce5f60e2').text
        data = json.loads(res)
        model = QStandardItemModel(0, 1, self.ui.treeView)
        model.setHeaderData(0, Qt.Horizontal, None)
        self.ui.treeView.setModel(model)
        self.TreeViewFill(model, data)

    def TreeViewFill(self, model, data):
        i = 0
        for root, children in data.items():
            parent = QStandardItem(root)
            self.AddChild(children, parent)
            model.setItem(i, 0, parent)
            self.ui.treeView.setFirstColumnSpanned(i, self.ui.treeView.rootIndex(), True)
            i += 1

    def AddChild(self, children, parent):
        if isinstance(children, dict):
            for item, items in children.items():
                child = QStandardItem(item)
                parent.setIcon(QIcon('images/help.png'))
                child.setIcon(QIcon('images/help.png'))
                parent.appendRow(child)
                self.AddChild(items, child)
        elif children != None:  # if there is one node
            node = QStandardItem(children)
            node.setToolTip("Bu kodu editöre sürükle-bırak şeklinde taşıyabilirsiniz")
            self.childNodes.append(children)
            parent.appendRow(node)

    # endregion

    # region ButtonClick
    def PlayButtonClick(self):
        code = self.ui.textEdit_kodBlogu.toPlainText()
        if code:
            old_stdout = sys.stdout
            new_stdout = io.StringIO()
            sys.stdout = new_stdout
            exec(code)
            result = sys.stdout.getvalue().strip()
            sys.stdout = old_stdout
            self.ui.textEdit_console.setText(str(result))

        else:
            self.ui.textEdit_console.setText(">>> ")

    def AddButtonClick(self):
        b = 1

    def DocumentButtonClick(self):
        b = 1

    def SearchButtonClick(self):
        s=1

    def MenuActionClick(self, jsonFile, index):
        if (self.activeMenu != 0):
            self.toolButtons[self.activeMenu].setStyleSheet(
                "background-color: #394b58; color: white; font: 14pt; padding-top:10px;")
        self.toolButtons[index].setStyleSheet("background-color: #6b899f; color: white; font: 14pt; padding-top:10px;")
        self.ReadFromFile(jsonFile)
        self.activeMenu = index

    # endregion

    # region PressedReleasedCodes

    def AddButtonPressed(self):
        self.ui.addButton.setIcon(QIcon("images/add_light.png"))

    def AddButtonReleased(self):
        self.ui.addButton.setIcon(QIcon("images/add_dark.png"))

    def PlayButtonPressed(self):
        if self.ui.textEdit_kodBlogu.toPlainText():
            self.ui.pushButton_play.setIcon(QIcon("images/play_light.png"))

    def PlayButtonReleased(self):
        self.ui.pushButton_play.setIcon(QIcon("images/play_dark.png"))

    def DocumentButtonPressed(self):
        self.ui.pushButton_document.setIcon(QIcon("images/document_light.png"))

    def DocumentButtonReleased(self):
        self.ui.pushButton_document.setIcon(QIcon("images/document_dark.png"))
    # endregion


if __name__ == "__main__":
    application = QApplication([])
    veritabaniBaglan()
    SqlSpeakModel = SqlKonusmaModeli()
    window = Project()
    window.show()
    application.exec_()
