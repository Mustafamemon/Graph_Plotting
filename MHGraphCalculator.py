# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 20:57:32 2018

@author: Hassan
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic, Qt
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication, QFileDialog) 	
from PyQt5.QtGui import QPalette


import prims ,kruskal ,dijkstra,FloydWarshall,bellmanford,parser_1,plotting, LocalCluster, all_bulk
from functools import partial

result = () 
node_x_y = [] # list of ['node_number', x-axis position,y-axis position]
from_to_cost = 0
no_of_nodes = 0
source = 0



qtCreatorFile = "base1.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

def buttonpress(function, *args):
    result = (node_x_y,)
    result = result + function(*args)
    result = result[ : 2 ] + (no_of_nodes ,) + (source,)+ result[2 : ]
    # print(result)
    plotting.PLOTTING(result)

def PLOTTING():
    # print(result)
    plotting.PLOTTING(result)


globalobj = 0
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def benchmark_input(self):
        file_path, files = QFileDialog.getOpenFileName(self)
        global result 
        global node_x_y 
        global from_to_cost 
        global no_of_nodes 
        global source 

        try:
            result = parser_1.PARSER(file_path)
        except FileNotFoundError as fe:
            print(fe)
            er = QtWidgets.QErrorMessage(self)
            er.showMessage('Invalid File')
            return 
        except ValueError as fe:
            print(fe)
            er = QtWidgets.QErrorMessage(self)
            er.showMessage('Invalid File')
            return 

        result = result + (0.0,) + ('Simple Graph',)
        node_x_y = result[0]
        from_to_cost = result [1]
        no_of_nodes = result[2]
        source = result[3]

        self.pushButton_plot.show()
        self.pushButton_plot.show()
        self.pushButton_kruskal.show()
        self.pushButton_prims.show()
        self.pushButton_dijkstra.show()
        self.pushButton_bellman.show()
        self.pushButton_floyd.show()
        self.pushButton_local.show() 
        self.pushButton_all.show()
        self.tableWidget.show()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        self.pushButton_plot.hide()
        self.pushButton_kruskal.hide()
        self.pushButton_prims.hide()
        self.pushButton_dijkstra.hide()
        self.pushButton_bellman.hide()
        self.pushButton_floyd.hide()
        self.pushButton_local.hide()
        self.pushButton_all.hide()
        self.tableWidget.hide()

        self.pushButton_plot.clicked.connect(lambda: PLOTTING())
        self.pushButton_kruskal.clicked.connect(lambda: buttonpress(kruskal.kruskal,from_to_cost,no_of_nodes))
        self.pushButton_prims.clicked.connect(lambda: buttonpress( prims.PRIMS,from_to_cost,no_of_nodes,source ))
        self.pushButton_dijkstra.clicked.connect(lambda :buttonpress(dijkstra.DIJKSTRA,from_to_cost,no_of_nodes,source))
        self.pushButton_bellman.clicked.connect(lambda: buttonpress(bellmanford.BELLMANFORD,from_to_cost,no_of_nodes,source))
        self.pushButton_floyd.clicked.connect(lambda: buttonpress(FloydWarshall.FLOYDWARSHALL,from_to_cost,no_of_nodes,source,node_x_y))
        self.pushButton_local.clicked.connect(lambda: LocalCluster.LocalCluster(result, self))
        self.pushButton_all.clicked.connect(lambda: all_bulk.get_all_results(from_to_cost,no_of_nodes,source,node_x_y, result, self))
        self.pushButton_get_input.clicked.connect(self.benchmark_input)


        
if __name__ == "__main__":
   
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53,53,53))
    palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15,15,15))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53,53,53))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53,53,53))
    palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142,45,197).lighter())
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(palette)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    