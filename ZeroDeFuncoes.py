#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import math
import parser
import sys 								#não deixar de importar para usar graficos
from PyQt4 import QtGui, QtCore			#não deixar de importar para usar graficos

############
import sympy
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
init_printing()
############




#classe da janela principal
################################################################
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
		self.biBtn = QtGui.QPushButton("Bissecao", self)
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






# classe que cria a janela do metodo da bisseccao
######################################################################################
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

		#etiqueta da resposta
		self.resposta = QtGui.QLabel("Resposta ---> ?",self)
		self.resposta.move(50, 195)
		self.resposta.resize(600, 50)
		self.resposta.setFont(QtGui.QFont("Ubuntu", 12, QtGui.QFont.Bold))

		#	campo para entrar com a função
		self.campoFuncao = QtGui.QLineEdit(self)
		self.campoFuncao.move(80,22)
		self.campoFuncao.resize(150,25)

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
		self.iteracoesLabel.resize(165,25)

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
		self.goBtn.clicked.connect(self.Starter)

		#botao 'plot!'
		self.plotBtn = QtGui.QPushButton("Plot!", self)
		self.plotBtn.move(50,145)
		self.plotBtn.resize(410,25)
		self.plotBtn.clicked.connect(self.Plotter)

		self.show()

	def Starter(self):
		#pega funcao digitada pelo usuario
		self.funcao = self.campoFuncao.text()

		#pega a e b do intervalo digitado
		self.a = float(self.campoA.text())
		self.b = float(self.campoB.text())

		#pega o erro desejado
		self.error = float(eval(str(self.campoErro.text())))
		#calcula o numero de iterações necessária para aquele erro
		self.k = self.CalculaK(self.a, self.b, self.error)
		#atualiza a etiqueta na tela
		self.iteracoesLabel.setText("Numero de Iteracoes (k) = %d" %self.k)

		#executa o metodo
		self.bissecao(self.a, self.b)

	
	def CalculaK(self, a, b, erro):
		#pega sempre o valo positivo do intervalo
		if(b-a >= 0):
			h = b-a
		if(b-a < 0):
			h = (b-a)*-1
		#retorna o valor de K arredondado pra cima
		return math.ceil((np.log10(h/erro))/(np.log10(2)))

	#calcula f(x)
	def CalculaF(self, x):
		return float(eval(str(self.funcao)))
	
	#verifica sinais
	def VerificaSinais(self, a, b):
		if(self.CalculaF(a)*self.CalculaF(b) < 0):
			return 1
		else:
			return 0

	def Plotter(self):
		def f(x):
			return eval(str(self.funcao))

		plt.axis([self.aOrginal-1,self.bOrginal+1,-100,100])
		plt.plot(self.pMs,self.YpMs, 'bo', self.xs, f(self.xs),'k')
		plt.grid()
		plt.show()

	def bissecao(self, a, b):
		self.aOrginal = a
		self.bOrginal = b

		
		#lista dos pontos medios para plotar
		self.pMs = []
		#essa lista é apenas pra plotagem
		self.YpMs = []

		#lista tambem para plotagem
		self.xs = np.arange(float(self.aOrginal), float(self.bOrginal), 0.02)

		#para plotagem
		self.pMs.append(self.aOrginal)
		self.pMs.append(self.bOrginal)
		self.YpMs.append(0)
		self.YpMs.append(0)


		#se os sinais de f(a) e f(b) nao forem opostos, pede um novo intervalo
		condicao = self.VerificaSinais(a,b)
		if(condicao == 0):
			msg = QtGui.QMessageBox()
			msg.setIcon(QtGui.QMessageBox.Information)
			msg.setWindowTitle("Escolha de intervalo")
			msg.setText("f(a) . f(b) > 0!")
			msg.setInformativeText("Retorne e escolha outro intervalo de forma que f(a) . f(b) < 0")
			msg.setDetailedText("Nao ha como garantir convergencia nesse intervalo!\nf(a) = %f\nf(b) = %f\nf(a).f(b) = %f" %(self.CalculaF(a), self.CalculaF(b), self.CalculaF(a)*self.CalculaF(b)))
			msg.setStandardButtons(QtGui.QMessageBox.Ok)
			msg.exec_()
		else:
			for i in range(1, int(self.k)):
				y0 = self.CalculaF(a)
				y1 = self.CalculaF(b)
				pMedio = (a+b)/2
				
				#para plotagem
				self.pMs.append(pMedio)
				#para plotagem
				self.YpMs.append(0)

				yMedio = self.CalculaF(pMedio)
				if(y0 * yMedio < 0):
					b = pMedio
				if(y1 * yMedio < 0):
					a = pMedio
			self.resposta.setText("Resposta ---> %.20f" %pMedio)

			



	
		







def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()