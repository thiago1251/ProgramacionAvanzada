from Conex.Conexion import Conexion
from Modelo.Profesor import Profesor

class AdmonProfesores:

    def __init__(self):
        self.con = Conexion()
        self.miConexion = self.con.conectar()
        
        print('Objeto tipo AdmonProfesores creado y listo para usarse..!!')
       
        self.menu()

    def menu(self):
        opcion = -1
        while opcion != 0:
            print('===============')
            print('     PROFESORES')
            print('===============')
            print('0. Regresar')            
            print('1. Ver todos')
            print('2. Buscar Profesor')
            print('3. Agregar Profesor')
            print('4. Modificar Profesor')
            print('5. Eliminar Profesor')

            opcion = int(input('Digite su opción:'))

            if opcion == 0:
                self.con.desconectar()
                print("Fin del menu de Administración de Profesores")
            elif opcion == 1:
                self.verTodos()
            elif opcion == 2:
                self.buscarProfesor()
            elif opcion == 3:
                self.agregaProfesor()
            elif opcion == 4:
                self.modifyProfesor()
            elif opcion == 5:
                self.eliminarProfesor()
            else:
                print('Esa opción NO existe..!!!')
            input ()

    def verTodos(self):
        cant = 0
        try: 
            mycursor = self.miConexion.cursor()
            mycursor.callproc('allProfesores')
            for result in mycursor.stored_results():
                for (idProfesor,nombre,direccion,telefono,programa) in result:
                    elProfesor = Profesor(idProfesor, nombre, direccion,telefono,programa)
         
                    print(elProfesor.toString())
                    cant = cant + 1
            if cant == 0 :
                    print ("No hay profesores registrados")
            mycursor.close()   
        except Exception as miError:
            print('Fallo ejecutando el procedimiento..!!')
            print(miError)

    def buscarProfesor(self):
        idProfesorSearch = int(input('Digite el codigo del profesor'))
        if self.existeIdProfesor(idProfesorSearch) == False:
            print('El profesor no existe')
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getProfesor', [idProfesorSearch])
                for result in mycursor.stored_results():
                    for (idProfesor, nombre, direccion, telefono, programa) in result:
                        elProfesor = Profesor(idProfesor, nombre, direccion, telefono, programa)
                        print(elProfesor.toString())
                mycursor.close()
            except Exception as miError:
                print('Fallo ejecutando el procedimiento')
                print(miError)
        
         


    def agregaProfesor(self):
        idProfesorNew = int(input('Digite el código del profesor: '))
        if self.existeIdProfesor(idProfesorNew) == True :
            print ("El profesor ya existe no se puede repetir")
        else :
            telefonoNew = (input('Digite el telefono: '))
            if self.existeTelefono(telefonoNew) == True :
                print ("El numero de telefono ya existe no se puede repetir")
            else:
                
                nombreNew = input('Digite el nombre del profesor: ')
                direccionNew = input('Digite la direccion del profesor: ')
                programaNew = int(input('Dijite el programa al que pertenece el profesor'))
                try:
                    mycursor = self.miConexion.cursor()
                    mycursor.callproc('newProfesor', [idProfesorNew, nombreNew, direccionNew, telefonoNew, programaNew])
                    self.miConexion.commit()
                    print('El profesor ha sido creado...!!')
                    mycursor.close()
                except Exception as miError:
                    print('Fallo  ejecutando el procedimiento')
                    print(miError)

         

    def eliminarProfesor(self):

        idProfesorDel = int(input('Digite el código del profesor a eliminar: '))
        if self.existeIdProfesor(idProfesorDel) == False :
            print ("El profesor no existe, no se puede eliminar")
        else :
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delProfesor', [idProfesorDel])
                self.miConexion.commit()
                print('El profesor ha sido eliminado..!!')
                mycursor.close()
            except Exception as miError : 
                print('Fallo ejecutanto el procedimiento')
                print(miError)
            


    def modifyProfesor(self):

        idProfesorOld = int(input('Digite código actual: '))
        if self.existeIdProfesor(idProfesorOld) == False :
            print ("El profesor no existe")
        else :
            idProfesorNew = int(input('Digite nuevo código del profesor: '))
            if idProfesorNew != idProfesorOld and self.existeIdProfesor(idProfesorNew) == True:
                print("Ya existe un profesor con ese ID, No se puede modificar")
            else:
                telefonoNew = input('Digite el telefono nuevo: ')
                if self.existeTelefono(telefonoNew) == True :
                    print ("El numero de telefono ya existe no se puede repetir")
                else:
                    nombreNew = input('Digite el nuevo nombre del profesor: ')
                    direccionNew = input('Digite la nueva direccion del profesor: ')
                    programaNew = int(input('Dijite el nuevo programa al que pertenece el profesor'))
                    
                    try:
                        mycursor = self.miConexion.cursor()
                        mycursor.callproc('modProfesor', [idProfesorNew, nombreNew, direccionNew,telefonoNew,programaNew, idProfesorOld])
                        self.miConexion.commit()
                        print('El profesor ha sido modificado..!!')
                        mycursor.close()
                    except Exception as miError:
                        print('Fallo ejecutando el procedimiento')
                        print(miError)

    def existeIdProfesor(self,idProfesor):
        try:
            mycursor = self.miConexion.cursor()
            query = 'SELECT count(*) FROM PROFESORES WHERE idProfesor = %s ;'
            mycursor.execute(query,[idProfesor])
            resultados = mycursor.fetchall()
            for registro in resultados:
                if registro[0]==1:
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)

    def existeTelefono (self,telefono):
        try:
            mycursor = self.miConexion.cursor()
            query = 'SELECT count(*) FROM PROFESORES WHERE telefono = %s ;'
            mycursor.execute(query,[telefono])
            resultados = mycursor.fetchall()
            
            for registro in resultados:
                if registro[0] == 1:
                    return True
                return False
        except Exception as miError :
            print('Fallo ejecutando el procedimiento')
            print(miError)


