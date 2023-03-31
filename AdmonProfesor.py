from Profesor import Profesor
class AdmonProfesor :
    def __init__(self):
        self.misProfesores = []
        print('Objeto tipo admon Profesores creado ...!')
        self.menu()
    def menu (self):
        opcion = -1
        while opcion != 0:
            print('==============OPCIONES============')
            print('0. Salir')
            print('1. Nuevo Profesor')
            print('2. Ver Profesores')
            print('3. Buscar Profesor')
            print('4. Eliminar Profesor')
            print('5. Modificar Profesor')
            opcion = int ( input('Diga su opcion :'))
            if opcion == 0:
                print('Adios .....')
            elif opcion == 1:
                self.nuevoProfesor()
            elif opcion == 2:
                self.verTodos()
            elif opcion==3:
                self.buscarProfesor()
            elif opcion == 4:
                self.eliminarProfesor()
            elif opcion == 5:
                self.modificarProfesor()
           
                
    def nuevoProfesor(self):
        #pedir la informacion
        codigoNew = int(input('Diga el codigo del profesor'))
        if self.existeCodigo(codigoNew) == True:
            print('El codigo del profesor ya esxiste!')
        else :
           telefonoNew = input('Diga el telefono del profesor')
           if self.existeTelefono(telefonoNew) == True:
               print('El numero de telefono ya existe')
           else: 
               nombreNew = input('Diga el nombre del profesor')
               direccionNew = input('Diga la direccion del profesor')
               programaNew = int(input('Diga el programa'))
           
                   #Crear el objeto Profesor
               teacher = Profesor(codigoNew, nombreNew, direccionNew, telefonoNew, programaNew)
                
                   #Guardar esta instancia en la lista
               self.misProfesores.append(teacher)
               print('El Profesor ha sido creado con exito')
#______________________________________________________________________________  
    def verTodos(self):
        for teacher in self.misProfesores:
            print(teacher.toString())
#______________________________________________________________________________     
    def buscarProfesor(self):
        codigoSearch = int(input('Diga el codigo del Profesor'))
        if self.existeCodigo(codigoSearch)== False:
            print('El codigo del Profesor no esxiste!')
        else:
            for teacher in self.misProfesores:
                if codigoSearch==teacher.getCodigo():
                    print(teacher.toString())
#______________________________________________________________________________     
    def eliminarProfesor(self):
        codigoDel = int(input('Diga el codigo del Profesor'))
        if self.existeCodigo(codigoDel)== False:
            print('El codigo no existe')
        else:
            for teacher in self.misProfesores:
                if codigoDel==teacher.getCodigo():
                    self.misProfesores.remove(teacher)
                    print('El profesor se ha eliminado')
#______________________________________________________________________________ 
    def modificarProfesor(self):
        codigoMod = int(input('Diga el codigo del Profesor'))
        if self.existeCodigo(codigoMod)== False:
            print('El codigo no existe')
        else:
                for teacher in self.misProfesores:
                    if codigoMod==teacher.getCodigo():
                        codigoNew = int( input('Diga codigo:'))
                        if self.existeCodigo(codigoNew)== True:
                            print('El codigo del profesor ya esxiste!')
                        else: 
                            telefonoNew = input('Diga el telefono del profesor')
                            if self.existeTelefono(telefonoNew) == True:
                                print('El numero de telefono ya existe')
                            else:
                                nombreNew = input('Diga el Nombre')
                                direccionNew = input('Diga la direccion del profesor')
                                programaNew = int(input('Diga el programa'))
                                
                                teacher.setDireccion(direccionNew)
                                teacher.setNombre(nombreNew)
                                teacher.setCodigo(codigoNew)
                                teacher.setPrograma(programaNew)
                                print('el profesor fue modificado')
#______________________________________________________________________________ 
    def existeCodigo (self,codigo):
        for teacher in self.misProfesores:
            if codigo == teacher.getCodigo():
                return True
        return False
#______________________________________________________________________________ 
    def existeTelefono (self,telefono):
        for teacher in self.misProfesores:
            if telefono == teacher.getTelefono():
                return True
        return False
