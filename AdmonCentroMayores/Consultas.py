from Conex.Conexion import Conexion
class Consultas:

    def __init__(self):
        self.con = Conexion()
        self.miConexion = self.con.conectar()
        
        print('Objeto tipo Consultas creado y listo para usarse..!!')
       
        self.menu()

    def menu(self):
        opcion = -1
        while opcion != 0:
            print('===============')
            print('   CONSULTAS')
            print('===============')
            print('0. Regresar')            
            print('1. Listado de Adultos Mayores por Centro')
            print('2. Listado de Actividades')
            print('3. Calificación de Actividades')
            print('4. Listado de Inscritos en Actividad')
            print('5. Actividades realizadas')

            opcion = int(input('Digite su opción:'))

            if opcion == 0:
                self.con.desconectar()
                print("Fin del menu de Administración de Consultas")
            elif opcion == 1:
                self.verAlgo1()
            elif opcion == 2:
                self.verAlgo2()
            elif opcion == 3:
                self.verAlgo3()
            elif opcion == 4:
                 self.verAlgo4()
            elif opcion == 5:
                self.verAlgo5()
            else:
                print('Esa opción NO existe..!!!')
            input ()
            
    def verAlgo1 (self):
        try:
            mycursor=self.miConexion.cursor()
            query = 'SELECT centros.nombre AS Centro, adultos.Nombre, adultos.Apellido FROM centros INNER JOIN adultos ORDER BY centros.nombre, adultos.Apellido;'
            mycursor.execute(query)
            resultados = mycursor.fetchall()
            for registro in resultados:
                print('Centro: ',registro[0], ' ¬Nombre:', registro[1], '¬Apellido: ', registro[2] )
            mycursor.close()
        except Exception as miError:
            print('Fallo Ejecutando el Procedimiento')
            print(miError)
            
    def verAlgo2 (self):
         try:
             mycursor=self.miConexion.cursor()
             query = 'SELECT categorias.nombre , actividades.nombre, actividades.fecha  , actividades.Descripcion, centros.Direccion  FROM (categorias INNER JOIN actividades ON categorias.idCategoria = actividades.iDCategoria) INNER JOIN centros ON centros.nombre = actividades.Centro;'
             mycursor.execute(query)
             resultados = mycursor.fetchall()
             for registro in resultados:
                 print('Categoria: ',registro[0], ' ¬Fecha:', registro[2], '¬Nombre: ', registro[1], '¬Decripcion: ' , registro[3], '¬Direccion: ', registro[4])
             mycursor.close()
         except Exception as miError:
             print('Fallo Ejecutando el Procedimiento')
             print(miError)
             
    def verAlgo3 (self):
             try:
                 mycursor=self.miConexion.cursor()
                 query = 'SELECT actividades.nombre , adultos.nombre  , inscripcion.Calificacion  FROM (adultos INNER JOIN inscripcion ON adultos.idAdulto = inscripcion.idAdulto) INNER JOIN actividades ON actividades.idActividad = inscripcion.idActividad ORDER BY calificacion desc;'
                 mycursor.execute(query)
                 resultados = mycursor.fetchall()
                 for registro in resultados:
                     print('Actividad: ',registro[0], ' ¬Adulto:', registro[1], '¬Calificacion: ', registro[2])
                 mycursor.close()
             except Exception as miError:
                 print('Fallo Ejecutando el Procedimiento')
                 print(miError)
                 
    def verAlgo4 (self):
             try:
                 mycursor=self.miConexion.cursor()
                 query = 'SELECT actividades.idActividad, adultos.Nombre, adultos.Apellido FROM  adultos INNER JOIN inscripcion ON adultos.idAdulto = inscripcion.idAdulto INNER JOIN actividades ON actividades.idActividad= 2 = inscripcion.idActividad;'
                 mycursor.execute(query)
                 resultados = mycursor.fetchall()
                 for registro in resultados:
                     print('Actividad: ',registro[0], ' ¬Nombre:', registro[1], '¬Apellido: ', registro[2])
                 mycursor.close()
             except Exception as miError:
                 print('Fallo Ejecutando el Procedimiento')
                 print(miError)
                 
    def verAlgo5 (self):
             try:
                 mycursor=self.miConexion.cursor()
                 query = 'SELECT actividades.Fecha,actividades.Nombre as Actividad,inscripcion.Calificacion FROM actividades INNER JOIN inscripcion on actividades.idActividad=inscripcion.IdActividad WHERE IdAdulto=4444;'
                 mycursor.execute(query)
                 resultados = mycursor.fetchall()
                 for registro in resultados:
                     print('Fecha: ',registro[0], ' ¬Actividad:', registro[1], '¬Calificacion: ', registro[2])
                 mycursor.close()
             except Exception as miError:
                 print('Fallo Ejecutando el Procedimiento')
                 print(miError)