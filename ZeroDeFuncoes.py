#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import sys 								#não deixar de importar para usar graficos
from PyQt4 import QtGui, QtCore			#não deixar de importar para usar graficos

#classe da janela principal
class Window(QtGui.QMainWindow):
	#construtor
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(400,200,500,300)
		self.setWindowTitle("Metodos iterativos")
		self.setWindowIcon(QtGui.QIcon('ico.png'))
		
		#define o layout da janela principal
		self.home()

	def home(self):
		#botao Bissecção
		self.biBtn = QtGui.QPushButton("Bisseccao", self)
		self.biBtn.move(200,50)

		#botao Ponto fixo
		self.pontoFixoBtn = QtGui.QPushButton("Ponto fixo", self)
		self.pontoFixoBtn.move(200,100)

		#botao Newton
		self.pontoFixoBtn = QtGui.QPushButton("Newton", self)
		self.pontoFixoBtn.move(200,150)

		#botao sair
		self.quitBtn = QtGui.QPushButton("Sair", self)
		self.quitBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		self.quitBtn.move(200,200)

		self.show()

def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()