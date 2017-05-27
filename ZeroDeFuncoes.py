#não deixar de importar para usar graficos
import sys
#não deixar de importar para usar graficos
from PyQt4 import QtGui, QtCore

#basico pra criar janelas
app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
#setta tamanho e posicao
window.setGeometry(50,50,500, 300)
#titulo
window.setWindowTitle("Primeira tela em python")
window.show()
########################