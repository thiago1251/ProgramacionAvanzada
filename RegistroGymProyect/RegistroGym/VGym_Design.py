import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

from Gyb_Design import Ui_MainWindow

class VGym_Design (QMainWindow):
    def __init__(self):
        super(VGym_Design, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.hobbies = []
      
        self.ui.PBRegistrar.clicked.connect(self.boton_Registrar)
       
   
    def boton_Registrar(self):
        if self.ui.LENombre.text() == '':
        
            QMessageBox.warning(self, 'Error', 'Ingrese su Nombre, Por favor!')
            
        elif self.ui.LEApellido.text() =='':
           
            QMessageBox.warning(self, 'Error', 'Ingrese su Apellido, Por favor!')
      
        else:
            self.ui.PBRegistrar.setEnabled(True)
            for checkbox in[self.ui.CBEntrenaCircuito, self.ui.CBLevantaPesa, 
                            self.ui.CBPracticaDeportes, self.ui.CBYoga, self.ui.CBEntrenamientoCardio]:
                if checkbox.isChecked():
                    self.hobbies.append(checkbox.text())
                    
            QMessageBox.information(self, 'Registro exitoso  ','Nombre: ' +self.ui.LENombre.text()+'-    Apellido: '+self.ui.LEApellido.text()
                                +'-   Fecha de Nacimiento: ' + self.ui.DENacimiento.date().toString('dd/MM/yyyy')
                                + '-   Peso: '+ str(self.ui.DEBPeso.value())+ '-   Altura: '+ str(self.ui.SBAltura.value())
                                + '-   Genero: '+ self.ui.CBGenero.currentText()+'-   Hobbie(s): '+ str(self.hobbies) ) 
            self.close()
                  

        
if __name__=='__main__':
    app = QApplication([])
    ventana = VGym_Design()
    ventana.show()
    sys.exit(app.exec())    

        
