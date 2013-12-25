#!/usr/bin/python -u
# -*- coding: utf-8 -*-


from PyQt4 import QtGui, QtCore
from mainui import Ui_MainWindow
from pdftolatextablemain import get_latex_table

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)
        self.setupUi(self)
        self.button_sort.clicked.connect(self.sort)

    def sort(self):
        self.textbox_output.setText(get_latex_table(str(self.textbox_input.toPlainText())))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())


