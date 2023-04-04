from Conex.Conexion import Conexion
from Modelo.Proyecto import Proyecto
from datetime import datetime

class AdmonProyectos:

    def __init__(self):
        self.con = Conexion()
        self.miConexion = self.con.conectar()
        
        print('Objeto tipo AdmonProyectos creado y listo para usarse..!!')
       
        self.menu()

    def menu(self):
        opcion = -1
        while opcion != 0:
            print('===============')
            print('   PROYECTOS')
            print('===============')
            print('0. Regresar')            
            print('1. Ver todos')
            print('2. Buscar Proyecto')
            print('3. Agregar Proyecto')
            print('4. Modificar Proyecto')
            print('5. Eliminar Proyecto')

            opcion = int(input('Digite su opción:'))

            if opcion == 0:
                self.con.desconectar()
                print("Fin del menu de Administración de Proyectos")
            elif opcion == 1:
                self.verTodos()
            elif opcion == 2:
                self.buscarProyecto()
            elif opcion == 3:
                self.agregaProyecto()
            elif opcion == 4:
                self.modifyProyecto()
            elif opcion == 5:
                self.eliminaProyecto()
            else:
                print('Esa opción NO existe..!!!')
            input ()

    def verTodos(self):
        cant = 0
        try: 
            mycursor = self.miConexion.cursor()
            mycursor.callproc('allProyectos')
            for result in mycursor.stored_results():
                for (idProyecto,nombre,presupuesto,fechaInicio,lider) in result:
                    elProyecto = Proyecto(idProyecto, nombre, presupuesto,fechaInicio,lider)
         
                    print(elProyecto.toString())
                    cant = cant + 1
            if cant == 0 :
                    print ("No hay Profesores registradas")
            mycursor.close()   
        except Exception as miError:
            print('Fallo ejecutando el procedimiento..!!')
            print(miError)

    def buscarProyecto(self):
        idProyectoSearch = int(input('Digite el código del Proyecto: '))
        if self.existeIdProyecto(idProyectoSearch) == False :
            print ("El Proyecto no existe")
        else :
            
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getProyecto',[idProyectoSearch])
                for result in mycursor.stored_results():
                    for ( idProyecto,nombre,presupuesto,fechaInicio,lider) in result:
                        elProyecto = Proyecto(idProyecto,nombre,presupuesto,fechaInicio,lider)
                        print(elProyecto.toString())
                        
                mycursor.close()
            except Exception as miError:
                print('Fallo ejecutando el procedimiento')
                print(miError)
            
         


    def agregaProyecto(self):
        idProyectoNew = int(input('Digite el código del nuevo Proyecto: '))
        if self.existeIdProyecto(idProyectoNew) == True :
            print ("El profesor ya existe no se puede repetir")
        else :
             nombreNew = input('Diga el nombre del proyecto')
             if self.existeNombre(nombreNew)==True:
                 print('El nombre del proyecto ya existe')
             else:
                  liderNew = input('Diga el profesor Lider')
                  if self.existeLider(liderNew)== True:
                      print('El profesor ya es lider')
                  else:
                      presupuestoNew = input('Diga el presupuesto del proyecto')
                      fechaInicioNew = datetime.strptime(input('Diga la fecha de inicio del proyecto (YYYY-MM-DD): '), '%Y-%m-%d')
                
                  try:
                      mycursor = self.miConexion.cursor()
                      mycursor.callproc('newProyect', [idProyectoNew, nombreNew, presupuestoNew, fechaInicioNew, liderNew])
                      self.miConexion.commit()
                      print('El Proyecto ha sido creado...!!')
                      mycursor.close()
                  except Exception as miError:
                      print('Fallo ejecutando el procedimiento')
                      print(miError)

         

    def eliminaProyecto(self):

        idProyectoDel = int(input('Digite el código del Proyecto a eliminar: '))
        if self.existeIdProyecto(idProyectoDel) == False :
            print ("El Proyecto no existe, no se puede eliminar")
        else :
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delProyecto', [idProyectoDel])
                self.miConexion.commit()
                print('El Proyecto ha sido eliminado..!!')
                mycursor.close()
            except Exception as miError : 
                print('Fallo ejecutanto el procedimiento')
                print(miError)
            


    def modifyProyecto(self):

        idProyectoOld = int(input('Digite código actual: '))
        if self.existeIdProyecto(idProyectoOld) == False :
            print ("El Proyecto no existe")
        else :
            idProyectoNew = int(input('Digite nuevo código del Proyecto: '))
            if idProyectoNew != idProyectoOld and self.existeIdProyecto(idProyectoNew) == True:
                print("Ya existe un Proyecto con ese ID, No se puede modificar")
            else:
                nombreNew = input('Digite el nuevo nombre del proyecto: ')
                if self.existeNombre(nombreNew)==True:
                    print('El nombre del proyecto ya existe')
                else:
                     liderNew = input('Diga el nuevo profesor Lider')
                     if self.existeLider(liderNew)== True:
                         print('El profesor ya es lider en otro Proyecto')
                     else:
                         presupuestoNew = input('Diga el nuevo presupuesto del proyecto')
                         fechaInicioNew = datetime.strptime(input('Diga la nueva fecha de inicio del proyecto (YYYY-MM-DD): '), '%Y-%m-%d')
                
                     try:
                            mycursor = self.miConexion.cursor()
                            mycursor.callproc('modProyecto', [idProyectoNew,nombreNew, presupuestoNew, fechaInicioNew, liderNew, idProyectoOld])
                            self.miConexion.commit()
                            print('El Proyecto ha sido modificado..!!')
                            mycursor.close()
                     except Exception as miError:
                            print('Fallo ejecutando el procedimiento')
                            print(miError)

    def existeIdProyecto(self,idProyecto):
        try:
            mycursor = self.miConexion.cursor()
            query = 'SELECT count(*) FROM PROYECTOS WHERE idProyecto = %s ;'
            mycursor.execute(query,[idProyecto])
            resultados = mycursor.fetchall()
            
            for registro in resultados:
                if registro[0] == 1:
                    return True
                return False
        except Exception as miError :
            print('Fallo ejecutando el procedimiento')
            print(miError)
    
    def existeNombre(self,nombre):
        try:
            mycursor = self.miConexion.cursor()
            query = 'SELECT count(*) FROM PROYECTOS WHERE nombre = %s ;'
            mycursor.execute(query,[nombre])
            resultados = mycursor.fetchall()
            
            for registro in resultados:
                if registro[0] == 1:
                    return True
                return False
        except Exception as miError :
            print('Fallo ejecutando el procedimiento')
            print(miError)
            
    
    def existeLider(self,lider):
        try:
            mycursor = self.miConexion.cursor()
            query = 'SELECT count(*) FROM PROYECTOS WHERE lider = %s ;'
            mycursor.execute(query,[lider])
            resultados = mycursor.fetchall()
            
            for registro in resultados:
                if registro[0] == 1:
                    return True
                return False
        except Exception as miError :
            print('Fallo ejecutando el procedimiento')
            print(miError)



