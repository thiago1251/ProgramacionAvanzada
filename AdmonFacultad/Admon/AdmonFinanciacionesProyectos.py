from Conex.Conexion import Conexion
from Modelo.FinanciacionProyecto import FinanciacionProyecto


class AdmonFinanciancianesProyectos:

        def __init__(self):
            self.con = Conexion()
            self.miConexion = self.con.conectar()
            
            print('Objeto tipo AdmonFinanciacionesProyectos creado y listo para usarse..!!')
           
            self.menu()

        def menu(self):
    
            opcion = -1
            while opcion != 0:
                print('===============')
                print(' FINANCIACIONES EN LOS PROYECTOS')
                print('===============')
                print('0. Regresar')            
                print('1. Ver todas')
                print('2. Buscar Financiacion de Proyecto')
                print('3. Agregar Financiacion de Proyecto')
                print('4. Modificar Financiacion de Proyecto')
                print('5. Eliminar Financiacion del Proyecto')

                opcion = int(input('Digite su opción:'))

                if opcion == 0:
                    self.con.desconectar()
                    print("Fin del menu de Administración de Financiacion de Proyectos")
                elif opcion == 1:
                    self.verTodas()
                elif opcion == 2:
                    self.buscarFinanciacion()
                elif opcion == 3:
                    self.agregaFinanciacion()
                elif opcion == 4:
                    self.modifyFinanciacion()
                elif opcion == 5:
                    self.eliminaFinanciacion()
                else:
                    print('Esa opción NO existe..!!!')
                input ()
                
        def verTodas(self):
            cant = 0
            try: 
                mycursor = self.miConexion.cursor()
                mycursor.callproc('allFinanciacion_Proyectos')
                for result in mycursor.stored_results():
                    for (idProyecto,idFuente, monto) in result:
                        laFinanciacion = FinanciacionProyecto(idProyecto,idFuente, monto)
             
                        print(laFinanciacion.toString())
                        cant = cant + 1
                if cant == 0 :
                        print ("No hay Financiaciones de Proyectos registrados")
                mycursor.close()   
            except Exception as miError:
                print('Fallo ejecutando el procedimiento..!!')
                print(miError)
                
        def buscarFinanciacion(self):
            idSearchFuente = int(input('Diga el codigo de la Fuente'))
            idSearchProyecto = int(input('Diga el codigo del Proyecto'))
            if self.existeCodigo( idSearchProyecto, idSearchFuente)== False:
                print('El codigo no existe!')
            else :
                
                try:
                    mycursor = self.miConexion.cursor()
                    mycursor.callproc('getFinanciacion_Proyecto', [ idSearchFuente,idSearchProyecto])
                    for result in mycursor.stored_results():
                        for ( idProyecto,idFuente, monto) in result:
                            laFinanciacion = FinanciacionProyecto(idProyecto,idFuente, monto)
                            print(laFinanciacion.toString())
                            
                    mycursor.close()
                except Exception as miError:
                    print('Fallo ejecutando el procedimiento')
                    print(miError)
                    
        def agregaFinanciacion(self):
            idNewProyecto = int(input('Diga el codigo nuevo del Proyecto'))
            idNewFuente = int(input('Diga el codigo nuevo de la Fuente'))
            
            if self.existeCodigo(idNewProyecto,idNewFuente) == True :
                print ("La Financiacion de Proyecto ya existe no se puede repetir")
                
            else :
                montoNew = input('Digite el monto de dinero dispuesto: ')
                try:
                    mycursor = self.miConexion.cursor()
                    mycursor.callproc('newFinanciacion_Proyecto', [idNewProyecto,idNewFuente,montoNew])
                    self.miConexion.commit()
                    print('La Financiacion del Proyecto ha sido creada...!!')
                    mycursor.close()
                except Exception as miError:
                    print('Fallo  ejecutando el procedimiento')
                    print(miError)
                    
        def eliminaFinanciacion(self):
            idFuenteDel = int(input('Diga el codigo actual del Proyecto'))
            idProyectoDel = int(input('Diga el codigo actual del Proyecto'))
            if self.existeCodigo(idFuenteDel,idProyectoDel) == False :
                print ("La Financiacion del Proyecto no existe, no se puede eliminar")
            else :
                try:
                    mycursor = self.miConexion.cursor()
                    mycursor.callproc('delFinanciacion_Proyecto', [idProyectoDel,idFuenteDel])
                    self.miConexion.commit()
                    print('La Financiacion del Proyecto ha sido eliminada..!!')
                    mycursor.close()
                except Exception as miError : 
                    print('Fallo ejecutanto el procedimiento')
                    print(miError)
                


        def modifyFinanciacion(self):

            idProyectoOld = int(input('Diga el codigo actual del Proyecto'))
            idFuenteOld = int(input('Diga el codigo actual de la Fuente'))
        
            if self.existeCodigo(idProyectoOld,idFuenteOld) == False :
                print ("La Financiacion del Proyecto no existe")
            else :
                idProyectoNew = int(input('Diga el codigo nuevo del Proyecto'))
                idFuenteNew = int(input('Diga el codigo nuevo de la fuente'))
                if idFuenteNew != idFuenteOld and idProyectoNew != idProyectoOld and self.existeCodigo(idFuenteNew,idProyectoNew) == True:
                    print("Ya existe una Financiacion con ese ID, No se puede modificar")
                else:
                    montoNew = input('Digite el nuevo monto de dinero dispuesto: ')
                    
                    
                    try:
                        mycursor = self.miConexion.cursor()
                        mycursor.callproc('modFinanciacion_Proyecto', [idProyectoNew,idFuenteNew, montoNew, idProyectoOld, idFuenteOld])
                        self.miConexion.commit()
                        print('La Financiacion de Proyecto ha sido modificada..!!')
                        mycursor.close()
                    except Exception as miError:
                        print('Fallo ejecutando el procedimiento')
                        print(miError)

                    
        def existeCodigo(self,idFuente,idProyecto):
            try:
                mycursor = self.miConexion.cursor()
                query = 'SELECT COUNT(*) FROM FINANCIACION_PROYECTOS WHERE idProyecto = %s AND idFuente = %s'      
                mycursor.execute(query,[idFuente,idProyecto])
                resultados = mycursor.fetchall()
                
                for registro in resultados:
                    if registro[0] == 1:
                        return True
                    return False
            except Exception as miError :
                print('Fallo ejecutando el procedimiento')
                print(miError)

