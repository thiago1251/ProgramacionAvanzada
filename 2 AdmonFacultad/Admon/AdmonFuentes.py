import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem



from Modelo.Fuente import Fuente
from Conex.Conexion import Conexion
from Diseno.DFuentes import Ui_MainWindow

class AdmonFuentes(QMainWindow):

    def __init__(self):
        super(AdmonFuentes, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.con = Conexion ()
        self.miConexion = self.con.conectar ()
        print('Objeto tipo AdmonFuentes creado y listo para usarse..!!')
        self.ui.PBTodas.clicked.connect(self.verTodas)
        self.ui.PBBuscar.clicked.connect(self.buscarFuente)
        self.ui.PBEliminar.clicked.connect(self.eliminaFuente)
        self.ui.PBSalir.clicked.connect(self.cerrarConexion)
        self.ui.PBBuscar.clicked.connect(self.buscarFuente)
        self.ui.PBModificar.clicked.connect(self.modifyFuente)
        self.ui.PBAgregar.clicked.connect(self.agregaFuente)
    def cerrarConexion(self):
        self.con.desconectar()
        self.close()
  


    def verTodas(self):
        cant = 0
        try :
            mycursor = self.miConexion.cursor ()
            mycursor.callproc ( 'allFuentes')
            #Limpiar la tabla
            a = self.ui.TWTabla.rowCount()
            for rep in range(a):
                self.ui.TWTabla.removeRow(0)
            #Llenar la tabla
            
                
            
            for result in mycursor.stored_results ():
                for (idFuente, nombre, contacto) in result :
                    self.ui.TWTabla.insertRow(cant)
                    
                    
                    celdaCodigo = QTableWidgetItem(str(idFuente))
                    celdaNombre = QTableWidgetItem(nombre)
                    celdaContacto = QTableWidgetItem(contacto)
                    
                    self.ui.TWTabla.setItem(cant,0, celdaCodigo)
                    self.ui.TWTabla.setItem(cant,1, celdaNombre)
                    self.ui.TWTabla.setItem(cant,2, celdaContacto)
                  
                    cant = cant + 1
            if cant == 0 :
                QMessageBox.information(self, 'Alerta en Consulta', 'No hay fuentes registradas..!!')
            mycursor.close()
        except Exception as ex :
            QMessageBox.information(self, 'Consulta Fallida', 'Fallo ejecutando el procedimiento de consulta de las fuentes..!!')
            print(ex)            

    def buscarFuente(self):
        cant =0
        idFuenteSearch = self.ui.SBCodigoBuscar.value()
        if self.existeIdFuente(idFuenteSearch) == False :
            QMessageBox.information(self, 'Alerta en Consulta', 'No hay fuentes registradas..!!')
        else :
            try:
                
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getFuente', [idFuenteSearch])
                #Limpiar la tabla
                a = self.ui.TWTabla.rowCount()
                for rep in range(a):
                    self.ui.TWTabla.removeRow(0)
                #Llenar la tabla
                
    
    
                for result in mycursor.stored_results():
                    for (idFuente, nombre, contacto) in result:
                        self.ui.TWTabla.insertRow(cant)
                        
                        
                        celdaCodigo = QTableWidgetItem(str(idFuente))
                        celdaNombre = QTableWidgetItem(nombre)
                        celdaContacto = QTableWidgetItem(contacto)
                        
                        self.ui.TWTabla.setItem(cant,0, celdaCodigo)
                        self.ui.TWTabla.setItem(cant,1, celdaNombre)
                        self.ui.TWTabla.setItem(cant,2, celdaContacto)
                        cant = cant + 1

                mycursor.close()
    
            except Exception as miError :
                QMessageBox.information(self,"Fallo", "Hay un fallo en la ejecucion")
                print(miError)



    def agregaFuente(self):
        idFuenteNew = self.ui.SBCodigoNuevo.value()
        if self.existeIdFuente(idFuenteNew) == True :
            QMessageBox.information (self,"Registro Fallido","La fuente ya existe no se puede repetir")
        else :
            
            nombreNew = self.ui.LEAgregarNombre.text()
            contactoNew = self.ui.LEAgregarContacto.text()
            
            try : 
                mycursor = self.miConexion.cursor ()
                mycursor.callproc ("newFuente",[idFuenteNew,nombreNew,contactoNew])
                self.miConexion.commit ()                
                QMessageBox.information(self,"Registro Exitoso",'La fuente ha sido creada..!!')
                mycursor.close ()
            except Exception as miError :
                QMessageBox.information(self,"Registro Fallido",'Fallo ejecutando el procedimiento')
                print(miError)
        

    def eliminaFuente(self):

        idFuenteDel = self.ui.SBCodigoEliminar.value()
        if self.existeIdFuente ( idFuenteDel ) == False :
            QMessageBox.information(self, 'Eliminacion Fallida', 'La fuente no existe, no se puede eliminar')
        else :
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delFuente' , [ idFuenteDel ] )
                self.miConexion.commit()
                
                QMessageBox.information(self, 'Eliminacion Exitosa', 'La fuente ha sido eliminada..!!')
                mycursor.close()
            except Exception as miError :
                QMessageBox.information(self, 'Eliminacion Fallida', 'Fallo ejecutando el proceso..!!')
                print(miError)


    def modifyFuente(self):

        idFuenteOld = self.ui.SBCodigoExistente.value()
        if self.existeIdFuente(idFuenteOld) == False :
            QMessageBox.information(self,"Modificación Fallida","La fuente no existe")
        else :
            idFuenteNew = self.ui.SBCodigoModificar.value()
            if idFuenteNew != idFuenteOld and self.existeIdFuente(idFuenteNew) == True:
                QMessageBox.information(self,"Modificación Fallida","Ya existe una fuente con ese ID, No se puede modificar")
            else:
                nombreNew = self.ui.LENombreModificar.text()
                contactoNew = self.ui.LEModificarContacto.text()

                try:
                    mycursor = self.miConexion.cursor()
                    mycursor.callproc('modFuente', [idFuenteNew, nombreNew, contactoNew, idFuenteOld])
                    self.miConexion.commit()
                    QMessageBox.information(self,"Modificacion Exitosa",'La fuente ha sido modificada..!!')
                    mycursor.close()
                except Exception as miError :
                    QMessageBox.information(self,"Modificacion Fallida",'Fallo ejecutando el procedimiento')
                    print(miError)



    def existeIdFuente (self,idFuente):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM FUENTES WHERE idFuente = %s"
            mycursor.execute(query, [idFuente])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)        
if __name__=='__main__':
    app=QApplication([])
    ventanaAdmonFuentes=AdmonFuentes()
    ventanaAdmonFuentes.show()
    sys.exit(app.exec())
