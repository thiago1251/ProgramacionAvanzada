from Financiacion import Financiacion
class AdmonFinanciacion :
    def __init__(self):
        self.misFinanciaciones = []
        print('Objeto tipo admon Financiacion de Proyectos creado ...!')
        self.menu()
    def menu (self):
        opcion =-1
        while opcion != 0:
            print('==============OPCIONES============')
            print('0. Salir')
            print('1. Nueva Financiacion de proyecto')
            print('2. Ver financiaciones de los proyectos')
            print('3. Buscar financiacion de Proyecto')
            print('4. Eliminar financiacion de Proyecto')
            print('5. Modificar financiacion de Proyecto')
            opcion = int ( input('Diga su opcion :'))
            if opcion == 0:
                print('Adios .....')
            elif opcion == 1:
                self.nuevaFinanciacion()
            elif opcion == 2:
                self.verTodos()
            elif opcion==3:
                self.buscarFinanciacion()
            elif opcion == 4:
                self.eliminarFinanciacion()
            elif opcion == 5:
                self.modificarFinanciacion()
           
                
    def nuevaFinanciacion(self):
        
        #pedir la informacion
        codigoNewProyecto = int(input('Diga el codigo del proyecto '))
        codigoNewFuente = int(input('Diga el codigo de la fuente'))
        
        if self.existeCodigo(codigoNewProyecto, codigoNewFuente) == True:
               print('El codigo ya existe!')
        else:
               montoNew = int(input('Diga el monto dispuesto para el proyecto'))
               financiacion = Financiacion(codigoNewProyecto, codigoNewFuente, montoNew)
                    
                       #Guardar esta instancia en la lista
               self.misFinanciaciones.append(financiacion)
               print('La financiacion del Proyecto ha sido creada con exito')
#______________________________________________________________________________  
    def verTodos(self):
        for proy in self.misFinanciaciones:
            print(proy.toString())
#______________________________________________________________________________     
    def buscarFinanciacion(self):
        codigoSearchProy = int(input('Diga el codigo del Proyecto'))
        codigoSearchFuente = int(input('Diga el codigo de la fuente'))
        if self.existeCodigo(codigoSearchProy, codigoSearchFuente)== False:
            print('El codigo no existe!')
        else:
                for proy in self.misFinanciaciones:
                    if codigoSearchProy == proy.getCodigoProyecto() and codigoSearchFuente == proy.getCodigoFuente():
                        print(proy.toString())
#______________________________________________________________________________     
    def eliminarFinanciacion(self):
        codigoDelProy = int(input('Diga el codigo del Proyecto'))
        codigoDelFuente = int(input('Diga el codigo de la fuente'))
        if self.existeCodigo(codigoDelProy, codigoDelFuente)== False:
            print('El codigo no existe!')
        else:
            for proy in self.misFinanciaciones:
                if codigoDelProy==proy.getCodigoProyecto() and codigoDelFuente == proy.getCodigoFuente():
                    self.misFinanciaciones.remove(proy)
                    print('La financiacion se ha eliminado')
#______________________________________________________________________________ 
    def modificarFinanciacion(self):
        codigoModProy = int(input('Diga el codigo del proyecto'))
        codigoModFuente = int(input('Diga el codigo de la fuente'))
        if self.existeCodigo(codigoModProy, codigoModFuente)== False:
            print('El codigo no existe!')
        else:
            for proy in self.misFinanciaciones:
                if codigoModProy==proy.getCodigoProyecto() and codigoModFuente == proy.getCodigoFuente():
                    codigoNewProy = int(input('Diga el codigo nuevo del Proyecto'))
                    codigoNewFuente = int(input('Diga el codigo nuevo de la fuente'))
                    if self.existeCodigo(codigoNewProy, codigoNewFuente)== True :
                        print('El codigo ya existe')
                    else:
                        montoNew = int(input('Diga el monto a disposicion por la fuente'))
                        proy.setCodigoProyecto(codigoNewProy)
                        proy.setCodigoFuente(codigoNewFuente)
                        proy.setMonto(montoNew)
                        print('La Financiacion fue modificada')       
          
#______________________________________________________________________________ 
    def existeCodigo (self,codigoProyecto, codigoFuente):
        for money in self.misFinanciaciones:
            if codigoProyecto == money.getCodigoProyecto() and codigoFuente == money.getCodigoFuente():
                return True
        return False
#______________________________________________________________________________ 
