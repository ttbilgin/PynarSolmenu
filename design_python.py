# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/aysegul_projeler/project/design.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 754)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 750))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setMinimumSize(QtCore.QSize(300, 500))
        self.treeView.setMaximumSize(QtCore.QSize(350, 16777215))
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
        self.frame_sagMenu = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_sagMenu.sizePolicy().hasHeightForWidth())
        self.frame_sagMenu.setSizePolicy(sizePolicy)
        self.frame_sagMenu.setMinimumSize(QtCore.QSize(300, 500))
        self.frame_sagMenu.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_sagMenu.setStyleSheet("\n"
"    border-radius: 8px 8px 8px 8px;\n"
"    padding: 10px;\n"
"    outline: 0px;\n"
"    font:   rgb(255, 255, 255);\n"
"    font:  20pt \"MS Shell Dlg 2\";\n"
"   background-color: rgb(222, 222, 222);\n"
"")
        self.frame_sagMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sagMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sagMenu.setObjectName("frame_sagMenu")
        self.label_imageboy = QtWidgets.QLabel(self.frame_sagMenu)
        self.label_imageboy.setGeometry(QtCore.QRect(0, 0, 301, 101))
        self.label_imageboy.setStyleSheet("image: url(:/icon/images/boys.png);")
        self.label_imageboy.setText("")
        self.label_imageboy.setObjectName("label_imageboy")
        self.label = QtWidgets.QLabel(self.frame_sagMenu)
        self.label.setGeometry(QtCore.QRect(0, 110, 301, 51))
        self.label.setStyleSheet("background-color:#4c649d;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_sagMenu)
        self.label_2.setGeometry(QtCore.QRect(90, 80, 121, 41))
        self.label_2.setStyleSheet("background-color:transparent;\n"
"font: 14pt \"Bahnschrift\";\n"
"color: rgb(122, 122, 122);")
        self.label_2.setObjectName("label_2")
        self.label_bubble = QtWidgets.QLabel(self.frame_sagMenu)
        self.label_bubble.setGeometry(QtCore.QRect(-10, 120, 101, 81))
        self.label_bubble.setStyleSheet("background-color:transparent;\n"
"image: url(:/icon/images/bubble.png);")
        self.label_bubble.setText("")
        self.label_bubble.setObjectName("label_bubble")
        self.horizontalLayout.addWidget(self.frame_sagMenu)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 70))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.searchEdit = QtWidgets.QTextEdit(self.frame)
        self.searchEdit.setGeometry(QtCore.QRect(0, 10, 250, 45))
        self.searchEdit.setStyleSheet("border: 1px solid;\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(156, 156, 156);\n"
"border-radius: 8px 8px 8px 8px;\n"
"background-color: palette(base);\n"
"color: rgb(102, 102, 102)")
        self.searchEdit.setObjectName("searchEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(250, 10, 50, 45))
        self.pushButton.setStyleSheet("background-image:url(:/newPrefix/search.png);\n"
"background-repeat: no-repeat;\n"
"background-image: url(:/search/search.png);\n"
"")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/search/images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(360, -11, 261, 91))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.addButton.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    background-repeat: no-repeat;\n"
" }")
        self.addButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/add/images/add_dark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon1)
        self.addButton.setIconSize(QtCore.QSize(64, 64))
        self.addButton.setCheckable(True)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout_2.addWidget(self.addButton)
        self.documentButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.documentButton.setStyleSheet("background-image: url(:/document/document.png);\n"
"background-color: transparent;\n"
"background-repeat: no-repeat;")
        self.documentButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/document/images/document_dark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.documentButton.setIcon(icon2)
        self.documentButton.setIconSize(QtCore.QSize(64, 64))
        self.documentButton.setCheckable(True)
        self.documentButton.setObjectName("documentButton")
        self.horizontalLayout_2.addWidget(self.documentButton)
        self.playButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.playButton.setStyleSheet("background-color: transparent;\n"
"background-repeat: no-repeat;\n"
"background-image: url(:/play/play.png);")
        self.playButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/play/images/play_dark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon3)
        self.playButton.setIconSize(QtCore.QSize(64, 64))
        self.playButton.setCheckable(True)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout_2.addWidget(self.playButton)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)
        self.frame_header = QtWidgets.QFrame(self.centralwidget)
        self.frame_header.setMinimumSize(QtCore.QSize(0, 125))
        self.frame_header.setStyleSheet("background-color:  #b9e6fb;")
        self.frame_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_header.setObjectName("frame_header")
        self.label_baslik = QtWidgets.QLabel(self.frame_header)
        self.label_baslik.setGeometry(QtCore.QRect(-450, 30, 1721, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_baslik.sizePolicy().hasHeightForWidth())
        self.label_baslik.setSizePolicy(sizePolicy)
        self.label_baslik.setMaximumSize(QtCore.QSize(16777215, 111))
        self.label_baslik.setStyleSheet("\n"
"image: url(:/logo/images/logoyazi.png);\n"
"")
        self.label_baslik.setText("")
        self.label_baslik.setObjectName("label_baslik")
        self.label_logo = QtWidgets.QLabel(self.frame_header)
        self.label_logo.setGeometry(QtCore.QRect(6, 0, 141, 131))
        self.label_logo.setStyleSheet("image: url(:/logo/images/logo.png);")
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "JSON VERİ"))
        self.treeView.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt; font-weight:600;\">asasas</span></p></body></html>"))
        self.textEdit_kodBlogu.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_console.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&gt;&gt;&gt;</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "ÖĞRETBOT"))

import icons_rc
