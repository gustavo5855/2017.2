# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Janela_2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    criterio = []
    def setupUi(self, MainWindow, crit):
        global criterio
        criterio = crit
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(681, 360)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 661, 251))
        self.tableWidget.setRowCount(len(criterio))
        self.tableWidget.setColumnCount(len(criterio))

        for i in range(len(criterio)):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)

            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)

        self.tableWidget.setObjectName("tableWidget")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 681, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        for i in range(len(criterio)):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("MainWindow", criterio[i]))#critério 1

            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", criterio[i]))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        # for i in range(len(criterio)):
        #     print(i)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "1"))

        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(_translate("MainWindow", "Matriz de Critérios"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

