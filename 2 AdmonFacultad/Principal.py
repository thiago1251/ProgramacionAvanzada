import sys
from PyQt6.QtWidgets import QMainWindow,QApplication

from Admon.AdmonFuentes import AdmonFuentes
from Diseno.DPrincipal import Ui_MainWindow

class Principal (QMainWindow):
	def __init__(self):
		super(Principal,self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.ui.BFuente.clicked.connect(self.fuente)
		self.ui.BTerminar.clicked.connect(self.terminar)

	def fuente(self):
		print("Se llama a Fuente")
		self.ventanaFuente = AdmonFuentes ()
		self.ventanaFuente.show ()

	def terminar(self):
		self.close()



if __name__ == '__main__':
	app =QApplication([])
	ventanaPrincipal = Principal()
	ventanaPrincipal.show()
	sys.exit(app.exec())
