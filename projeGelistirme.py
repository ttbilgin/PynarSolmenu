import os,io
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QColor,QIcon,QBrush
from PyQt5.QtCore import Qt,QModelIndex
import json, requests
from design_python import Ui_MainWindow

#region interfaceCodes

#endregion

class proje(QMainWindow):
    childNodes = []
    roots = []
    colors = ['#7fc97f', '#beaed4', '#fdc086', '#ffff99', '#386cb0', '#f0027f', '#bf5b17', '#666666']
    words = ["abs", "print", "while", "max", "for"]

    acikNodes =[]
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ReadFromJsonApi()
        self.ReadFromFile()

        self.show()
        self.ui.treeView.setDragDropMode(QAbstractItemView.DragOnly)
        self.ui.treeView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.treeView.clicked.connect(self.expanded)
        self.ui.treeView.doubleClicked.connect(self.collapsed)
        self.ui.playButton.pressed.connect(self.PlayButtonPressed)
        self.ui.playButton.released.connect(self.PlayButtonReleased)
        self.ui.addButton.pressed.connect(self.AddButtonPressed)
        self.ui.addButton.released.connect(self.AddButtonReleased)
        self.ui.documentButton.pressed.connect(self.DocumentButtonPressed)
        self.ui.documentButton.released.connect(self.DocumentButtonReleased)
        self.ui.playButton.clicked.connect(self.PlayButtonClick)
        self.ui.addButton.clicked.connect(self.AddButtonClick)
        self.ui.documentButton.clicked.connect(self.DocumentButtonClick)
        self.ui.pushButton.clicked.connect(self.SearchButtonClick)
        self.setAcceptDrops(True)


    # region TreeviewOperations
    def expanded(self, index):
         if not self.ui.treeView.isExpanded(index):
             if self.roots.__contains__(index.data()):
                 if len(self.acikNodes) > 0:
                     for item in self.acikNodes:
                         if item.data != index.data:
                             self.ui.treeView.collapse(item)
                             if self.acikNodes.__contains__(item.data()):
                                self.acikNodes.remove(item)
                 self.ui.treeView.expand(index)
                 self.acikNodes.append(index)
             else:
                 self.ui.treeView.expand(index)
                 self.acikNodes.append(index)
         else:
            self.ui.treeView.collapse(index)
            if self.acikNodes.__contains__(index):
                self.acikNodes.remove(index)


    def collapsed(self, item):
        i=1
        #self.ui.treeView.collapse(item)

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
        self.ui.textEdit_kodBlogu.setText(data)

    def ReadFromFile(self):
        with open(os.path.abspath('solmenu.json'), encoding='utf-8') as f:
            data = json.load(f)
        model = QStandardItemModel(0, 1, self.ui.treeView)
        model.setHeaderData(0, Qt.Horizontal, None)
        self.ui.treeView.setModel(model)
        self.TreeViewFill(model, data)

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

            self.roots.append(root)
            i += 1

    def AddChild(self, children, parent):
        if isinstance(children, dict):
            for item, items in children.items():
                child = QStandardItem(item)
                parent.appendRow(child)
                self.AddChild(items, child)
        elif children is not None:  # if there is one node
            node = QStandardItem(children)
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
        #TODO: content will be added

    def DocumentButtonClick(self):
        b=1
        # TODO: content will be added

    def SearchButtonClick(self):
        # aranan = self.ui.searchEdit.toPlainText()


        a = self.ui.treeView.keyboardSearch('a')

        #obj_type = type('Döngüler')
        #idx = self.sourceModel().index(sourceRow, 0, sourceParent)
        #a = self.ui.treeView.findChildren(str, 'a')
        print(str(a))


    # endregion

    # region PressedReleasedCodes
    def AddButtonPressed(self):
        self.ui.addButton.setIcon(QIcon(":/add/images/add_light.png"))
    def AddButtonReleased(self):
        self.ui.addButton.setIcon(QIcon(":/add/images/add_dark.png"))
    def PlayButtonPressed(self):
        if self.ui.textEdit_kodBlogu.toPlainText():
            self.ui.playButton.setIcon(QIcon(":/play/images/play_light.png"))
    def PlayButtonReleased(self):
        self.ui.playButton.setIcon(QIcon(":/play/images/play_dark.png"))
    def DocumentButtonPressed(self):
        self.ui.documentButton.setIcon(QIcon(":/document/images/document_light.png"))
    def DocumentButtonReleased(self):
        self.ui.documentButton.setIcon(QIcon(":/document/images/document_dark.png"))
    #endregion

    # region Functions


    # endregion



if __name__ == "__main__":
    uygulama = QApplication([])
    pencere = proje()
    pencere.show()
    uygulama.exec_()






