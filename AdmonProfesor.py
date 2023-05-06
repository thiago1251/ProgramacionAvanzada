import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from Modelo.Profesores import Profesor
from Conex.Conexion import Conexion
from Diseno.DProfesores import Ui_MainWindow
  

class AdmonProfesores(QMainWindow):
    def _init_ (self):
        super(AdmonProfesores, self)._init_()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.con = Conexion ()
        self.miConexion = self.con.conectar ()
        print('Objeto tipo AdmonProfesores creado y listo para usarse..!!')
        self.ui.PBTodas.clicked.connect(self.verTodas)
        self.ui.PBEliminar.clicked.connect(self.eliminaProfesor)
        self.ui.PBSalir.clicked.connect(self.cerrarConexion)
        self.ui.PBBuscar.clicked.connect(self.buscarProfesor)
        self.ui.PBAgregar.clicked.connect(self.agregaProfesor)
        self.ui.PBModificar.clicked.connect(self.modifyProfesor)
    
    def cerrarConexion(self):
         self.con.desconectar()
         self.close()
        

    def verTodas(self):
        cant = 0
        try :
            mycursor = self.miConexion.cursor ()
            mycursor.callproc ( 'allProfesores')
            
            
            a=self.ui.TWTabla.rowCount()
            for rep in range (a):
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
            if cant == 0 :
                
                QMessageBox.information(self,"Alerta en consulta","No hay profesores registradas")
            mycursor.close()
        except Exception as ex :
            QMessageBox.information(self,"Consulta Fallida"," Fallo ejecutando el procedimiento de Consulta de las Funetes")
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
        idProfesorNew = self.ui.SBCodigoAgregar.value()
        if self.existeIdProfesor(idProfesorNew) == True :
          QMessageBox.information (self,"Registro Fallido","La fuente ya existe no se puede repetir")
        else :
          
          nombreNew = self.ui.LEAgregarNombre.text()
          direccionNew = self.ui.LEAgregarDireccion.text()
          telefonoNew = self.ui.LEAgregarTelefono.text()
          programaNew = self.ui.LEAgregarNombre_3.text()
          
          
          try : 
              mycursor = self.miConexion.cursor ()
              mycursor.callproc ("newProfesor",[idProfesorNew,nombreNew,direccionNew,telefonoNew,programaNew])
              self.miConexion.commit ()                
              QMessageBox.information(self,"Registro Exitoso",'La fuente ha sido creada..!!')
              mycursor.close ()
          except Exception as miError :
              QMessageBox.information(self,"Registro Fallido",'Fallo ejecutando el procedimiento')
              print(miError)

    def eliminaProfesor(self):

        idProfesorDel = self.ui.SBCodigoEliminar.value()
        if self.existeIdProfesor ( idProfesorDel ) == False :
            QMessageBox.information(self, "Eliminacion fallida", "La fuente no existe, no se elimina")
        else :
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delProfesor' , [ idProfesorDel ] )
                self.miConexion.commit()
                
                QMessageBox.information(self, "Eliminacion exitosa", "La fuente ha sido eliminada")
                mycursor.close()
            except Exception as miError :
                QMessageBox.information(self, "Eliminacion fallida", "Fallo ejecutando el procedimiento")
                print(miError)


    def modifyProfesor(self):
        idProfesorOld = self.ui.SBCodigoExistene.value()
        if self.existeIdProfesor(idProfesorOld) == False :
           QMessageBox.information(self,"Modificación Fallida","La fuente no existe")
        else :
           idProfesorNew = self.ui.SBCodigoModificar.value()
           if idProfesorNew != idProfesorOld and self.existeIdProfesor(idProfesorNew) == True:
               QMessageBox.information(self,"Modificación Fallida","Ya existe una fuente con ese ID, No se puede modificar")
           else:
               nombreNew = self.ui.LENombreModificar.text()
               direccionNew = self.ui.LEDireccionModificar.text()
               telefonoNew = self.ui.LETelefonoModificar.text()
               programaNew = self.ui.LEProgramaModificar.text()
               

               try:
                   mycursor = self.miConexion.cursor()
                   mycursor.callproc('modProfesor', [idProfesorNew, nombreNew, direccionNew, telefonoNew, programaNew, idProfesorOld])
                   self.miConexion.commit()
                   QMessageBox.information(self,"Modificacion Exitosa",'La fuente ha sido modificada')
                   mycursor.close()
               except Exception as miError :
                   QMessageBox.information(self,"Modificacion Fallida",'Fallo ejecutando el procedimiento')
                   print(miError)


    def existeIdProfesor (self,idProfesor):
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

if _name_ =='_main_':
    app=QApplication ([])
    ventana = AdmonProfesores()
    ventana.show()
    sys.exit(app.exec())
