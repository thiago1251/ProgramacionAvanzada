import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem



from Modelo.Profesor import Profesor
from Conex.Conexion import Conexion
from Diseno.DProfesores import Ui_MainWindow

class AdmonProfesores(QMainWindow):

    def __init__(self):
        super(AdmonProfesores, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.con = Conexion ()
        self.miConexion = self.con.conectar ()
        print('Objeto tipo AdmonFuentes creado y listo para usarse..!!')
        self.ui.PBTodas.clicked.connect(self.verTodos)
        self.ui.PBBuscar.clicked.connect(self.buscarProfesor)
        self.ui.PBAgregar.clicked.connect(self.agregaProfesor)
        self.ui.PBEliminar.clicked.connect(self.eliminaProfesor)
        self.ui.PBModificar.clicked.connect(self.modifyProfesor)
        
        
        self.ui.PBSalir.clicked.connect(self.cerrarConexion)
        
    def cerrarConexion(self):
        self.con.desconectar()
        self.close()
  


    def verTodos(self):
        cant = 0
        try :
            mycursor = self.miConexion.cursor ()
            mycursor.callproc ( 'allProfesores')
            #Limpiar la tabla
            a = self.ui.TWTabla.rowCount()
            for rep in range(a):
                self.ui.TWTabla.removeRow(0)
            #Llenar la tabla
            
                
            
            for result in mycursor.stored_results ():
                for (idProfesor,nombre,direccion, telefono, programa) in result :
                    self.ui.TWTabla.insertRow(cant)
                    
                    
                    celdaCodigo = QTableWidgetItem(str(idProfesor))
                    celdaNombre = QTableWidgetItem(nombre)
                    celdaDireccion = QTableWidgetItem(direccion)
                    celdaTelefono = QTableWidgetItem(telefono)
                    celdaPrograma = QTableWidgetItem(str(programa)) 
                    
                    self.ui.TWTabla.setItem(cant,0, celdaCodigo)
                    self.ui.TWTabla.setItem(cant,1, celdaNombre)
                    self.ui.TWTabla.setItem(cant,2, celdaDireccion)
                    self.ui.TWTabla.setItem(cant,3, celdaTelefono)
                    self.ui.TWTabla.setItem(cant,4, celdaPrograma)
                  
                    cant = cant + 1
            if cant == 0 :
                QMessageBox.information(self, 'Alerta en Consulta', 'No hay Profesores registrados..!!')
            mycursor.close()
        except Exception as ex :
            QMessageBox.information(self, 'Consulta Fallida', 'Fallo ejecutando el procedimiento de consulta de los Profesores..!!')
            print(ex)  
            
    def buscarProfesor(self):
       cant =0
       idProfesorSearch = self.ui.SBCodigoBuscar.value()
       if self.existeIdProfesor(idProfesorSearch) == False :
           QMessageBox.information(self, 'Alerta en Consulta', 'No hay profesores registradas..!!')
       else :
           try:
               
               mycursor = self.miConexion.cursor()
               mycursor.callproc('getProfesor', [idProfesorSearch])
               a = self.ui.TWTabla.rowCount()
               for rep in range(a):
                   self.ui.TWTabla.removeRow(0)
               
   
   
               for result in mycursor.stored_results ():
                   for (idProfesor, nombre, direccion, telefono, programa) in result :
                       self.ui.TWTabla.insertRow(cant)
                      
                       celdaCodigo=QTableWidgetItem(str(idProfesor))
                       celdaNombre=QTableWidgetItem(nombre)
                       celdaDireccion=QTableWidgetItem(direccion)
                       celdaTelefono=QTableWidgetItem(telefono)
                       celdaPrograma=QTableWidgetItem(str(programa))
                      
                       self.ui.TWTabla.setItem(cant,0,celdaCodigo)
                       self.ui.TWTabla.setItem(cant,1,celdaNombre)
                       self.ui.TWTabla.setItem(cant,2,celdaDireccion)
                       self.ui.TWTabla.setItem(cant,3,celdaTelefono)
                       self.ui.TWTabla.setItem(cant,4,celdaPrograma)
                       cant = cant + 1

               mycursor.close()
   
           except Exception as miError :
               QMessageBox.information(self,"Fallo", "Hay un fallo en la ejecucion")
               print(miError)

                 
    def agregaProfesor(self):
        idProfesorNew = self.ui.SBCodigoNuevo.value()
        if self.existeIdProfesor(idProfesorNew) == True :
          QMessageBox.information (self,"Registro Fallido","El Profesor ya existe no se puede repetir")
        else :
          
          nombreNew = self.ui.LEAgregarNombre.text()
          direccionNew = self.ui.LEAgregarContacto.text()
          telefonoNew = self.ui.LETelefonoNuevo.text()
          programaNew = self.ui.SBProgramaNuevo.value()
          
          
          try : 
              mycursor = self.miConexion.cursor ()
              mycursor.callproc ("newProfesor",[idProfesorNew,nombreNew,direccionNew,telefonoNew,programaNew])
              self.miConexion.commit ()                
              QMessageBox.information(self,"Registro Exitoso",'El Profesor ha sido creado..!!')
              mycursor.close ()
          except Exception as miError :
              QMessageBox.information(self,"Registro Fallido",'Fallo ejecutando el procedimiento')
              print(miError)
              
    def eliminaProfesor(self):

        idProfesorDel = self.ui.SBCodigoEliminar.value()
        if self.existeIdProfesor ( idProfesorDel ) == False :
            QMessageBox.information(self, "Eliminacion fallida", "El Profesor no existe, no se puede eliminar")
        else :
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delProfesor' , [ idProfesorDel ] )
                self.miConexion.commit()
                
                QMessageBox.information(self, "Eliminacion exitosa", "El Profesor ha sido eliminado")
                mycursor.close()
            except Exception as miError :
                QMessageBox.information(self, "Eliminacion fallida", "Fallo ejecutando el procedimiento")
                print(miError)
                
    def modifyProfesor(self):
        idProfesorOld = self.ui.SBCodigoExistente.value()
        if self.existeIdProfesor(idProfesorOld) == False :
           QMessageBox.information(self,"Modificación Fallida","El Profesor no existe")
        else :
           idProfesorNew = self.ui.SBCodigoModificar.value()
           if idProfesorNew != idProfesorOld and self.existeIdProfesor(idProfesorNew) == True:
               QMessageBox.information(self,"Modificación Fallida","Ya existe un Profesor con ese ID, No se puede modificar")
           else:
               nombreNew = self.ui.LENombreModificar.text()
               direccionNew = self.ui.LEModificarDireccion.text()
               telefonoNew = self.ui.LEModificarTelefono.text()
               programaNew = self.ui.SBProgramaModificar.value()
               

               try:
                   mycursor = self.miConexion.cursor()
                   mycursor.callproc('modProfesor', [idProfesorNew, nombreNew, direccionNew, telefonoNew, programaNew, idProfesorOld])
                   self.miConexion.commit()
                   QMessageBox.information(self,"Modificacion Exitosa",'La fuente ha sido modificada')
                   mycursor.close()
               except Exception as miError :
                   QMessageBox.information(self,"Modificacion Fallida",'Fallo ejecutando el procedimiento')
                   print(miError)




    def existeIdProfesor(self,idProfesor):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM PROFESORES WHERE idProfesor = %s"
            mycursor.execute(query, [idProfesor])      
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
    ventanaAdmonProfesores=AdmonProfesores()
    ventanaAdmonProfesores.show()
    sys.exit(app.exec())
