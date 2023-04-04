from Conex.Conexion import Conexion
from Modelo.ParticipaProyecto import ParticipaProyecto


class AdmonParticipaProyectos:

        def __init__(self):
            self.con = Conexion()
            self.miConexion = self.con.conectar()
            
            print('Objeto tipo AdmonParticipaProyectos creado y listo para usarse..!!')
           
            self.menu()

        def menu(self):
    
            opcion = -1
            while opcion != 0:
                print('===============')
                print(' PARTICIPACIONES EN LOS PROYECTOS')
                print('===============')
                print('0. Regresar')            
                print('1. Ver todas')
                print('2. Buscar Participacion en Proyecto')
                print('3. Agregar Participacion en Proyecto')
                print('4. Modificar Participacion en Proyecto')
                print('5. Eliminar Participacion en Proyecto')

                opcion = int(input('Digite su opción:'))

                if opcion == 0:
                    self.con.desconectar()
                    print("Fin del menu de Administración de Participaciones en Proyectos")
                elif opcion == 1:
                    self.verTodas()
                elif opcion == 2:
                    self.buscarParticipacion()
                elif opcion == 3:
                    self.agregaParticipacion()
                elif opcion == 4:
                    self.modifyParticipacion()
                elif opcion == 5:
                    self.eliminaParticipacion()
                else:
                    print('Esa opción NO existe..!!!')
                input ()
                
        def verTodas(self):
            cant = 0
            try: 
                mycursor = self.miConexion.cursor()
                mycursor.callproc('allParticipacion_Proyectos')
                for result in mycursor.stored_results():
                    for (idProfesor, idProyecto, horas) in result:
                        laParticipacion = ParticipaProyecto(idProfesor, idProyecto, horas)
             
                        print(laParticipacion.toString())
                        cant = cant + 1
                if cant == 0 :
                        print ("No hay Participaciones en Proyectos registradas")
                mycursor.close()   
            except Exception as miError:
                print('Fallo ejecutando el procedimiento..!!')
                print(miError)
                
        def buscarParticipacion(self):
            idSearchProfesor = int(input('Diga el codigo del Profesor'))
            idSearchProyecto = int(input('Diga el codigo del Proyecto'))
            if self.existeCodigo(idSearchProfesor, idSearchProyecto)== False:
                print('El codigo no existe!')
            else :
                
                try:
                    mycursor = self.miConexion.cursor()
                    mycursor.callproc('getParticipacion_Proyecto', [idSearchProfesor, idSearchProyecto])
                    for result in mycursor.stored_results():
                        for ( idProfesor, idProyecto, horas) in result:
                            laParticipacion = ParticipaProyecto(idProfesor, idProyecto, horas)
                            print(laParticipacion.toString())
                            
                    mycursor.close()
                except Exception as miError:
                    print('Fallo ejecutando el procedimiento')
                    print(miError)
                    
        def agregaParticipacion(self):
            idNewProfesor = int(input('Diga el codigo nuevo del Profesor'))
            idNewProyecto = int(input('Diga el codigo nuevo del Proyecto'))
            
            if self.existeCodigo(idNewProfesor, idNewProyecto) == True :
                print ("La Participacion de Proyecto ya existe no se puede repetir")
                
            else :
                horasNew = input('Digite las Horas empleadas de la Participacion: ')
                try:
                    mycursor = self.miConexion.cursor()
                    mycursor.callproc('newParticipacion_Proyecto', [idNewProfesor,idNewProyecto,horasNew])
                    self.miConexion.commit()
                    print('La Participacion de Proyecto ha sido creada...!!')
                    mycursor.close()
                except Exception as miError:
                    print('Fallo  ejecutando el procedimiento')
                    print(miError)
                    
        def eliminaParticipacion(self):
            idProfesorDel = int(input('Diga el codigo actual del Profesor'))
            idProyectoDel = int(input('Diga el codigo actual del Proyecto'))
            if self.existeCodigo(idProfesorDel,idProyectoDel) == False :
                print ("La participacion del Proyecto no existe, no se puede eliminar")
            else :
                try:
                    mycursor = self.miConexion.cursor()
                    mycursor.callproc('delParticipacion_Proyecto', [idProfesorDel,idProyectoDel])
                    self.miConexion.commit()
                    print('La Participacion de Proyecto ha sido eliminada..!!')
                    mycursor.close()
                except Exception as miError : 
                    print('Fallo ejecutanto el procedimiento')
                    print(miError)
                


        def modifyParticipacion(self):

            idProfesorOld = int(input('Diga el codigo actual del Profesor'))
            idProyectoOld = int(input('Diga el codigo actual del Proyecto'))
            if self.existeCodigo(idProfesorOld,idProyectoOld) == False :
                print ("La Participacion de Proyecto no existe")
            else :
                idProfesorNew = int(input('Diga el codigo nuevo del Profesor'))
                idProyectoNew = int(input('Diga el codigo nuevo del Proyecto'))
                if idProfesorNew != idProfesorOld and idProyectoNew != idProyectoOld and self.existeCodigo(idProfesorNew, idProyectoNew) == True:
                    print("Ya existe una Participacion de Proyecto con ese ID, No se puede modificar")
                else:
                    horasNew = input('Digite la cantidad de horas empleadas en la Participacion De Proyecto: ')
                    
                    
                    try:
                        mycursor = self.miConexion.cursor()
                        mycursor.callproc('modParticipacion_Proyecto', [idProfesorNew, idProyectoNew, horasNew, idProfesorOld,idProyectoOld])
                        self.miConexion.commit()
                        print('La Participacion de Proyecto ha sido modificada..!!')
                        mycursor.close()
                    except Exception as miError:
                        print('Fallo ejecutando el procedimiento')
                        print(miError)

                    
        def existeCodigo(self,idProfesor,idProyecto):
            try:
                mycursor = self.miConexion.cursor()
                query = 'SELECT COUNT(*) FROM PARTICIPACION_PROYECTOS WHERE idProfesor = %s AND idProyecto = %s'      
                mycursor.execute(query,[idProfesor,idProyecto])
                resultados = mycursor.fetchall()
                
                for registro in resultados:
                    if registro[0] == 1:
                        return True
                    return False
            except Exception as miError :
                print('Fallo ejecutando el procedimiento')
                print(miError)

