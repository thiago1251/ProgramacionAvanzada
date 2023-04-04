from Conex.Conexion import Conexion
from Modelo.Departamento import Departamento

class AdmonDepartamentos:

    def __init__(self):
        self.con = Conexion()
        self.miConexion = self.con.conectar()
        
        print('Objeto tipo AdmonDepartamento creado y listo para usarse..!!')
       
        self.menu()

    def menu(self):
        opcion = -1
        while opcion != 0:
            print('===============')
            print('   DEPARTAMENTOS')
            print('===============')
            print('0. Regresar')            
            print('1. Ver todos')
            print('2. Buscar Departamento')
            print('3. Agregar Departamento')
            print('4. Modificar Departamento')
            print('5. Eliminar Departamento')

            opcion = int(input('Digite su opción:'))

            if opcion == 0:
                self.con.desconectar()
                print("Fin del menu de Administración de Departamentos")
            elif opcion == 1:
                self.verTodos()
            elif opcion == 2:
                self.buscarDepto()
            elif opcion == 3:
                self.agregaDepto()
            elif opcion == 4:
                self.modifyDepto()
            elif opcion == 5:
                self.eliminaDepto()
            else:
                print('Esa opción NO existe..!!!')
            input ()

    def verTodos(self):
        cant = 0
        try: 
            mycursor = self.miConexion.cursor()
            mycursor.callproc('allDepartamentos')
            for result in mycursor.stored_results():
                for (idDepto,nombre,extencion,jefe) in result:
                    elDepto = Departamento(idDepto, nombre, extencion, jefe)
         
                    print(elDepto.toString())
                    cant = cant + 1
            if cant == 0 :
                    print ("No hay profesores registrados")
            mycursor.close()   
        except Exception as miError:
            print('Fallo ejecutando el procedimiento..!!')
            print(miError)

    def buscarDepto(self):
        idDeptoSearch = int(input('Digite el código del Departamento: '))
        if self.existeIdDepto(idDeptoSearch) == False :
            print ("El Departamento no existe")
        else :
            
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getDepartamento',[idDeptoSearch])
                for result in mycursor.stored_results():
                    for (idDepto,nombre,extencion,jefe) in result:
                        elDepto = Departamento(idDepto,nombre,extencion,jefe)
                        print(elDepto.toString())
                        
                mycursor.close()
            except Exception as miError:
                print('Fallo ejecutando el procedimiento')
                print(miError)
            
         


    def agregaDepto(self):
        idDeptoNew = int(input('Digite el código del nuevo Departamento: '))
        if self.existeIdDepto(idDeptoNew) == True :
            print ("El Departamento ya existe no se puede repetir")
        else:
            nombreNew = input('Digite el nombre del Departamento: ')
            if self.existeNombre(nombreNew) == True:
                print('El Departamento ya existe no se puede repetir')
            else :
                extencionNew = input('Digite el contacto de la fuente: ')
                jefeNew = int(input('Digite el jefe del Departamento '))
                try:
                    mycursor = self.miConexion.cursor()
                    mycursor.callproc('newDepartamento', [idDeptoNew,nombreNew,extencionNew,jefeNew])
                    self.miConexion.commit()
                    print('El Departamento ha sido creado...!!')
                    mycursor.close()
                except Exception as miError:
                    print('Fallo  ejecutando el procedimiento')
                    print(miError)

         

    def eliminaDepto(self):

        idDeptoDel = int(input('Digite el código del Departamento a eliminar: '))
        if self.existeIdDepto(idDeptoDel) == False :
            print ("El Departamento no existe, no se puede eliminar")
        else :
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delDepartamento', [idDeptoDel])
                self.miConexion.commit()
                print('El Departamento ha sido eliminado..!!')
                mycursor.close()
            except Exception as miError : 
                print('Fallo ejecutanto el procedimiento')
                print(miError)
            


    def modifyDepto(self):

        idDeptoOld = int(input('Digite código actual: '))
        if self.existeIdDepto(idDeptoOld) == False :
            print ("El Departamento no existe")
        else :
            idDeptoNew = int(input('Digite nuevo código del Departamento: '))
            if idDeptoNew != idDeptoOld and self.existeIdDepto(idDeptoNew) == True:
                print("Ya existe un Departamento con ese ID, No se puede modificar")
                
            else:
                    nombreNew = input('Digite el nuevo nombre del Departamento: ')
                    if self.existeNombre(nombreNew) == True:
                        print('El Departamento ya existe no se puede repetir')
                    
                    else:
                        extencionNew = input('Digite la nueva extencion del Departamento: ')
                        jefeNew = input('Digite el nuevo jefe del Departamento: ')
                        
                        try:
                            mycursor = self.miConexion.cursor()
                            mycursor.callproc('modDepartamento', [idDeptoNew, nombreNew, extencionNew,jefeNew, idDeptoOld])
                            self.miConexion.commit()
                            print('El Departamento ha sido modificado..!!')
                            mycursor.close()
                        except Exception as miError:
                            print('Fallo ejecutando el procedimiento')
                            print(miError)

    def existeIdDepto (self,idDepto):
        try:
            mycursor = self.miConexion.cursor()
            query = 'SELECT count(*) FROM DEPARTAMENTOS WHERE idDepartamento = %s ;'
            mycursor.execute(query,[idDepto])
            resultados = mycursor.fetchall()
            
            for registro in resultados:
                if registro[0] == 1:
                    return True
                return False
        except Exception as miError :
            print('Fallo ejecutando el procedimiento')
            print(miError)
            
    def existeNombre (self,nombre):
        try:
            mycursor = self.miConexion.cursor()
            query = 'SELECT count(*) FROM DEPARTAMENTOS WHERE nombre = %s ;'
            mycursor.execute(query,[nombre])
            resultados = mycursor.fetchall()
            
            for registro in resultados:
                if registro[0] == 1:
                    return True
                return False
        except Exception as miError :
            print('Fallo ejecutando el procedimiento')
            print(miError)


