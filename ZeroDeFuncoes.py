#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import sys 								#não deixar de importar para usar graficos
from PyQt4 import QtGui, QtCore			#não deixar de importar para usar graficos






################################################################
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
		self.biBtn.clicked.connect(self.criaJanelaDoMetodoBis)

		#botao Ponto fixo
		self.pontoFixoBtn = QtGui.QPushButton("Ponto fixo", self)
		self.pontoFixoBtn.move(200,100)
		self.pontoFixoBtn.clicked.connect(self.criaJanelaDoMetodoPontFix)

		#botao Newton
		self.newtonBtn = QtGui.QPushButton("Newton", self)
		self.newtonBtn.move(200,150)
		self.newtonBtn.clicked.connect(self.criaJanelaDoMetodoNewt)

		#botao sair
		self.quitBtn = QtGui.QPushButton("Sair", self)
		self.quitBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		self.quitBtn.move(200,200)

		self.show()

	def criaJanelaDoMetodoBis(self):
		self.janelaBisseccao = BisseccaoWindow()

	def criaJanelaDoMetodoPontFix(self):
		self.janelaPontoFixo = PontoWindow()

	def criaJanelaDoMetodoNewt(self):
		self.janelaNewton = NewtonWindow()
######################################################################################






#QMdiSubWindow
#QMainWindow
class BisseccaoWindow(QtGui.QMdiSubWindow):
	#construtor
	
	def __init__(self):
		super(BisseccaoWindow, self).__init__()
		self.setGeometry(400,200,500,300)
		self.setWindowTitle("Metodos da Bisseccao")
		self.setWindowIcon(QtGui.QIcon('ico.png'))
		
		#define o layout da janela do método da bissecao
		self.define_layout()

	def define_layout(self):
		#	etiqueta 'F(x)'
		self.fDeX = QtGui.QLabel("f(x) = ",self)
		self.fDeX.move(50,20)

		#	campo para entrar com a função
		self.funcao = QtGui.QLineEdit(self)
		self.funcao.move(80,22)
		self.funcao.resize(150,25)

		#	etiqueta 'Erro'
		self.erroLabel = QtGui.QLabel("Erro <= ",self)
		self.erroLabel.move(300,20)
		self.erroLabel.resize(150,25)

		#	campo para entrar com o erro
		self.campoErro = QtGui.QLineEdit(self)
		self.campoErro.move(345,22)
		self.campoErro.resize(50,25)

		#	etiqueta 'iteracoes'
		self.iteracoesLabel = QtGui.QLabel("Numero de Iteracoes (k) = ?",self)
		self.iteracoesLabel.move(300,70)
		self.iteracoesLabel.resize(155,25)

		#	etiqueta ' intervalo'
		self.intervaloLabel = QtGui.QLabel("Intervalo: (                   ,                  )",self)
		self.intervaloLabel.move(50,70)
		self.intervaloLabel.resize(200,25)

		#campos a e b do intervalo
		self.campoA = QtGui.QLineEdit(self)
		self.campoA.move(115,75)
		self.campoA.resize(45,20)
		self.campoB = QtGui.QLineEdit(self)
		self.campoB.move(180,75)
		self.campoB.resize(45,20)


		#botao 'go!'
		self.goBtn = QtGui.QPushButton("Go!", self)
		self.goBtn.move(50,110)
		self.goBtn.resize(410,25)
		self.goBtn.clicked.connect(self.rodaMetodoBisseccao)

		self.show()

	def rodaMetodoBisseccao(self):
		funcao = self.funcao.text()
		print(funcao)

	def calculaK(self):
		pass

	def verificaSinais(self):
		pass











def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()