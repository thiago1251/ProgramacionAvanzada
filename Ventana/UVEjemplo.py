import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

from Ejemplo import Ui_MainWindow

class UVEjemplo (QMainWindow):
    def __init__(self):
        super(UVEjemplo, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.PBTerminar.setEnabled(False)
        self.ui.PBTerminar.clicked.connect(self.boton_salir)
        self.ui.PBAceptar.clicked.connect(self.boton_aceptar)
        
        
        
        
        
        
    def boton_salir(self):
        QMessageBox.information(self, 'Adios', 'Esto se acabo!!')
        self.close()
        
    def boton_aceptar(self):
        
        if self.ui.LENombre.text() == '':
            QMessageBox.warning(self, 'Error', 'Y el nombre???')
        else:
            
            
            self.ui.PBTerminar.setEnabled(True)
            self.ui.LTitulo.setText('Bienvenido  '+self.ui.LENombre.text() + ' con '+ str(self.ui.SBEdad.value())+' años')
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__=='__main__':
    app = QApplication([])
    ventana = UVEjemplo()
    ventana.show()
    sys.exit(app.exec())    