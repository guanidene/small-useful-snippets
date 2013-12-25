# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pushpak/Desktop/pdf-to-latex-table-gui/main_ui.ui'
#
# Created: Sat Nov 30 13:21:54 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(652, 396)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 0, 1, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.textbox_output = QtGui.QTextBrowser(self.centralwidget)
        self.textbox_output.setObjectName(_fromUtf8("textbox_output"))
        self.verticalLayout_2.addWidget(self.textbox_output)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.textbox_input = QtGui.QTextEdit(self.centralwidget)
        self.textbox_input.setObjectName(_fromUtf8("textbox_input"))
        self.verticalLayout.addWidget(self.textbox_input)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.button_sort = QtGui.QPushButton(self.centralwidget)
        self.button_sort.setObjectName(_fromUtf8("button_sort"))
        self.horizontalLayout.addWidget(self.button_sort)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 652, 26))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menu_About = QtGui.QMenu(self.menuBar)
        self.menu_About.setObjectName(_fromUtf8("menu_About"))
        MainWindow.setMenuBar(self.menuBar)
        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName(_fromUtf8("action_About"))
        self.menu_About.addAction(self.action_About)
        self.menuBar.addAction(self.menu_About.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "DHD Project", None))
        self.label_2.setText(_translate("MainWindow", "Latex Output", None))
        self.label.setText(_translate("MainWindow", "Pdf table copy paste here - ", None))
        self.button_sort.setText(_translate("MainWindow", "&Generate", None))
        self.menu_About.setTitle(_translate("MainWindow", "&Help", None))
        self.action_About.setText(_translate("MainWindow", "&About", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

