from Fuente import Fuente
class AdmonFuente :
    def __init__(self):
        self.misFuentes = []
        print('Objeto tipo fuente creado ...!')
        self.menu()
    def menu (self):
        opcion = -1
        while opcion != 0:
            print('==============OPCIONES============')
            print('0. Salir')
            print('1. Nueva Fuente')
            print('2. Ver Fuentes')
            print('3. Buscar Fuente')
            print('4. Eliminar Fuente')
            print('5. Modificar Fuente')
            opcion = int ( input('Diga su opcion :'))
            if opcion == 0:
                print('Adios .....')
            elif opcion == 1:
                self.nuevaFuente()
            elif opcion == 2:
                self.verTodos()
            elif opcion==3:
                self.buscarFuente()
            elif opcion == 4:
                self.eliminarFuente()
            elif opcion == 5:
                self.modificarFuente ()
           
                
    def nuevaFuente(self):
        #pedir la informacion
        codigoNew = int(input('Diga el codigo de la fuente'))
        if self.existeCodigo(codigoNew) == True:
            
            print('El codigo de la fuente ya existe!')
            
        else: 
               telefonoNew = input('Diga el telefono de la fuente')
               nombreNew = input('Diga el nombre de la fuente')
               direccionNew = input('Diga la direccion de la fuente')

                   #Crear el objeto Profesor
               source = Fuente(codigoNew, nombreNew, direccionNew, telefonoNew)
                   #Guardar esta instancia en la lista
               self.misFuentes.append(source)
               print('la fuente ha sido creada con exito')
#______________________________________________________________________________  
    def verTodos(self):
        for source in self.misFuentes:
            print(source.toString())
#______________________________________________________________________________     
    def buscarFuente(self):
        codigoSearch = int(input('Diga el codigo de la Fuente'))
        if self.existeCodigo(codigoSearch)== False:
            print('El codigo de la fuente no esxiste!')
        else:
            for source in self.misFuentes:
                if codigoSearch==source.getCodigo():
                    print(source.toString())
#______________________________________________________________________________     
    def eliminarFuente(self):
        codigoDel = int(input('Diga el codigo de la Fuente'))
        if self.existeCodigo(codigoDel)== False:
            print('El codigo no existe')
        else:
            for source in self.misFuentes:
                if codigoDel == source.getCodigo():
                    self.misFuentes.remove(source)
                    print('la Fuente se ha eliminado')
#______________________________________________________________________________ 
    def modificarFuente(self):
        codigoMod = int(input('Diga el codigo de la Fuente'))
        if self.existeCodigo(codigoMod)== False:
            print('El codigo no existe')
        else:
                for source in self.misFuentes:
                    if codigoMod==source.getCodigo():
                        codigoNew = int( input('Diga codigo:'))
                        if self.existeCodigo(codigoNew)== True:
                            print('El codigo de la fuente ya esxiste!')
                        else: 
                           
                                telefonoNew = input('Diga el telefono de la fuente')
                                nombreNew = input('Diga el Nombre de la fuente')
                                direccionNew = input('Diga la direccion de la fuente')
                             
                                source.setTelefono(telefonoNew)
                                source.setDireccion(direccionNew)
                                source.setNombre(nombreNew)
                                source.setCodigo(codigoNew)
                               
                                print('la fuente fue modificada')
#______________________________________________________________________________ 
    def existeCodigo (self,codigo):
        for source in self.misFuentes:
            if codigo == source.getCodigo():
                return True
        return False

