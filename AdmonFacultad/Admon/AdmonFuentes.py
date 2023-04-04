from Conex.Conexion import Conexion
from Modelo.Fuente import Fuente

class AdmonFuentes:

    def __init__(self):
        self.con = Conexion()
        self.miConexion = self.con.conectar()
        
        print('Objeto tipo AdmonFuentes creado y listo para usarse..!!')
       
        self.menu()

    def menu(self):
        opcion = -1
        while opcion != 0:
            print('===============')
            print('   FUENTES')
            print('===============')
            print('0. Regresar')            
            print('1. Ver todas')
            print('2. Buscar Fuente')
            print('3. Agregar Fuente')
            print('4. Modificar Fuente')
            print('5. Eliminar Fuente')

            opcion = int(input('Digite su opción:'))

            if opcion == 0:
                self.con.desconectar()
                print("Fin del menu de Administración de Fuentes")
            elif opcion == 1:
                self.verTodas()
            elif opcion == 2:
                self.buscarFuente()
            elif opcion == 3:
                self.agregaFuente()
            elif opcion == 4:
                self.modifyFuente()
            elif opcion == 5:
                self.eliminaFuente()
            else:
                print('Esa opción NO existe..!!!')
            input ()

    def verTodas(self):
        cant = 0
        try: 
            mycursor = self.miConexion.cursor()
            mycursor.callproc('allFuentes')
            for result in mycursor.stored_results():
                for (idFuente,nombre,contacto) in result:
                    laFuente = Fuente(idFuente, nombre, contacto)
         
                    print(laFuente.toString())
                    cant = cant + 1
            if cant == 0 :
                    print ("No hay fuentes registradas")
            mycursor.close()   
        except Exception as miError:
            print('Fallo ejecutando el procedimiento..!!')
            print(miError)

    def buscarFuente(self):
        idFuenteSearch = int(input('Digite el código de la fuente: '))
        if self.existeIdFuente(idFuenteSearch) == False :
            print ("La fuente no existe")
        else :
            
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getFuente',[idFuenteSearch])
                for result in mycursor.stored_results():
                    for ( idFuente, nombre, contacto) in result:
                        laFuente = Fuente(idFuente, nombre, contacto)
                        print(laFuente.toString())
                        
                mycursor.close()
            except Exception as miError:
                print('Fallo ejecutando el procedimiento')
                print(miError)
            
         


    def agregaFuente(self):
        idFuenteNew = int(input('Digite el código de la nueva fuente: '))
        if self.existeIdFuente(idFuenteNew) == True :
            print ("La fuente ya existe no se puede repetir")
        else :
            nombreNew = input('Digite el nombre de la fuente: ')
            contactoNew = input('Digite el contacto de la fuente: ')
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('newFuente', [idFuenteNew,nombreNew,contactoNew])
                self.miConexion.commit()
                print('La fuente ha sido creada...!!')
                mycursor.close()
            except Exception as miError:
                print('Fallo  ejecutando el procedimiento')
                print(miError)

         

    def eliminaFuente(self):

        idFuenteDel = int(input('Digite el código de la fuente a eliminar: '))
        if self.existeIdFuente(idFuenteDel) == False :
            print ("La fuente no existe, no se puede eliminar")
        else :
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delFuente', [idFuenteDel])
                self.miConexion.commit()
                print('La fuente ha sido eliminada..!!')
                mycursor.close()
            except Exception as miError : 
                print('Fallo ejecutanto el procedimiento')
                print(miError)
            


    def modifyFuente(self):

        idFuenteOld = int(input('Digite código actual: '))
        if self.existeIdFuente(idFuenteOld) == False :
            print ("La fuente no existe")
        else :
            idFuenteNew = int(input('Digite nuevo código de la fuente: '))
            if idFuenteNew != idFuenteOld and self.existeIdFuente(idFuenteNew) == True:
                print("Ya existe una fuente con ese ID, No se puede modificar")
            else:
                nombreNew = input('Digite el nuevo nombre de la fuente: ')
                contactoNew = input('Digite el nueva contacto de la fuente: ')
                
                try:
                    mycursor = self.miConexion.cursor()
                    mycursor.callproc('modFuente', [idFuenteNew, nombreNew, contactoNew, idFuenteOld])
                    self.miConexion.commit()
                    print('La fuente ha sido modificada..!!')
                    mycursor.close()
                except Exception as miError:
                    print('Fallo ejecutando el procedimiento')
                    print(miError)

    def existeIdFuente (self,idFuente):
        try:
            mycursor = self.miConexion.cursor()
            query = 'SELECT count(*) FROM FUENTES WHERE idFuente = %s ;'
            mycursor.execute(query,[idFuente])
            resultados = mycursor.fetchall()
            
            for registro in resultados:
                if registro[0] == 1:
                    return True
                return False
        except Exception as miError :
            print('Fallo ejecutando el procedimiento')
            print(miError)

