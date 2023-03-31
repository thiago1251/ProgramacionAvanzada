from Proyecto import Proyecto
class AdmonProyecto :
    def __init__(self):
        self.misProyectos = []
        print('Objeto tipo admon Proyectos creado ...!')
        self.menu()
    def menu (self):
        opcion =-1
        while opcion != 0:
            print('==============OPCIONES============')
            print('0. Salir')
            print('1. Nuevo Proyecto')
            print('2. Ver Proyectos')
            print('3. Buscar Proyecto')
            print('4. Eliminar Proyecto')
            print('5. Modificar Proyecto')
            opcion = int ( input('Diga su opcion :'))
            if opcion == 0:
                print('Adios .....')
            elif opcion == 1:
                self.nuevoProyecto()
            elif opcion == 2:
                self.verTodos()
            elif opcion==3:
                self.buscarProyecto()
            elif opcion == 4:
                self.eliminarProyecto()
            elif opcion == 5:
                self.modificarProyecto()
           
                
    def nuevoProyecto(self):
        #pedir la informacion
        codigoNew = int(input('Diga el codigo del proyecto'))
        if self.existeCodigo(codigoNew) == True:
            print('El codigo del proyecto ya esxiste!')
        else :
           liderNew = input('Diga el profesor Lider')
           if self.existeLider(liderNew)== True:
               print('El profesor ya es lider')
           else: 
               nombreNew = input('Diga el nombre del proyecto')
               if self.existeNombre(nombreNew)==True:
                   print('El nombre del proyecto ya existe')
               else:
                   presupuestoNew = input('Diga el presupuesto del proyecto')
                   fechaInicioNew = input('Diga la fecha de inicio del proyecto')
                   
                       #Crear el objeto Profesor
                   proyect = Proyecto(codigoNew, nombreNew, presupuestoNew, fechaInicioNew, liderNew)
                    
                       #Guardar esta instancia en la lista
                   self.misProyectos.append(proyect)
                   print('El Proyecto ha sido creado con exito')
#______________________________________________________________________________  
    def verTodos(self):
        for proy in self.misProyectos:
            print(proy.toString())
#______________________________________________________________________________     
    def buscarProyecto(self):
        codigoSearch = int(input('Diga el codigo del Proyecto'))
        if self.existeCodigo(codigoSearch)== False:
            print('El codigo del proyecto no existe!')
        else:
            for proy in self.misProyectos:
                if codigoSearch==proy.getCodigo():
                    print(proy.toString())
#______________________________________________________________________________     
    def eliminarProyecto(self):
        codigoDel = int(input('Diga el codigo del Proyecto'))
        if self.existeCodigo(codigoDel)== False:
            print('El codigo no existe')
        else:
            for proy in self.misProyectos:
                if codigoDel==proy.getCodigo():
                    self.misProyectos.remove(proy)
                    print('El proyecto se ha eliminado')
#______________________________________________________________________________ 
    def modificarProyecto(self):
        codigoMod = int(input('Diga el codigo del Proyecto'))
        if self.existeCodigo(codigoMod)== False:
            print('El codigo no existe')
        else:
                for proy in self.misProyectos:
                    if codigoMod==proy.getCodigo():
                        codigoNew = int( input('Diga codigo:'))
                        if self.existeCodigo(codigoNew)== True:
                            print('El codigo del proyecto ya existe!')
                        else: 
                            liderNew = input('Diga el profesor lider')
                            if self.existeLider(liderNew) == True:
                                print('El profesor ya tiene un proyecto asignado')
                            else:
                                nombreNew = input('Diga el nombre del proyecto')
                                if self.existeNombre(nombreNew)==True:
                                    print('El nombre del proyecto ya existe')
                                else:
                                    presupuestoNew = input('Diga el presupuesto del proyecto')
                                    fechaInicioNew = input('Diga la fecha de inicio del proyecto')
                                  
                                    proy.setPresupuesto(presupuestoNew)
                                    proy.setNombre(nombreNew)
                                    proy.setCodigo(codigoNew)
                                    proy.setFechaInicio(fechaInicioNew)
                                    proy.setLider(liderNew)
                                    print('el profesor fue modificado')
#______________________________________________________________________________ 
    def existeCodigo (self,codigo):
        for proy in self.misProyectos:
            if codigo == proy.getCodigo():
                return True
            return False
#______________________________________________________________________________ 
    def existeLider (self,lider):
        for proy in self.misProyectos:
            if lider == proy.getLider():
                return True
            return False
#______________________________________________________________________________ 
    def existeNombre (self,nombre):
        for proy in self.misProyectos:
            if nombre == proy.getNombre():
                return True
            return False