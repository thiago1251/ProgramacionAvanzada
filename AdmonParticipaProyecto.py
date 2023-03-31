from ParticipaProyecto import ParticipaProyecto
class AdmonParticipaProyecto :
    def __init__(self):
        self.misParticipaciones = []
        print('Objeto tipo admon Participacion Proyectos creado ...!')
        self.menu()
    def menu (self):
        opcion =-1
        while opcion != 0:
            print('==============OPCIONES============')
            print('0. Salir')
            print('1. Nueva Participacion de proyecto')
            print('2. Ver Participaciones de los proyectos')
            print('3. Buscar Participacion de Proyecto')
            print('4. Eliminar participacion de Proyecto')
            print('5. Modificar participacion de Proyecto')
            opcion = int ( input('Diga su opcion :'))
            if opcion == 0:
                print('Adios .....')
            elif opcion == 1:
                self.nuevaParticipacion()
            elif opcion == 2:
                self.verTodos()
            elif opcion==3:
                self.buscarParticipacion()
            elif opcion == 4:
                self.eliminarParticipacion()
            elif opcion == 5:
                self.modificarParticipacion()
           
                
    def nuevaParticipacion(self):
        
        #pedir la informacion
        codigoNewProfe = int(input('Diga el codigo del Profesor participante'))
        codigoNewProyecto = int(input('Diga el codigo del Proyecto'))
        
        if self.existeCodigo(codigoNewProfe, codigoNewProfe) == True:
               print('El codigo ya existe!')
        else:
               horasNew = int(input('Diga las horas de la participacion en el proyecto'))
               participacionPro = ParticipaProyecto(codigoNewProfe, codigoNewProyecto, horasNew)
                    
                       #Guardar esta instancia en la lista
               self.misParticipaciones.append(participacionPro)
               print('La participacion de Proyecto ha sido creado con exito')
#______________________________________________________________________________  
    def verTodos(self):
        for proy in self.misParticipaciones:
            print(proy.toString())
#______________________________________________________________________________     
    def buscarParticipacion(self):
        codigoSearchProfe = int(input('Diga el codigo del Profesor'))
        codigoSearchProy = int(input('Diga el codigo del Proyecto'))
        if self.existeCodigo(codigoSearchProfe, codigoSearchProy)== False:
            print('El codigo no existe!')
        else:
                for proy in self.misParticipaciones:
                    if codigoSearchProfe == proy.getCodigoProfe() and codigoSearchProy == proy.getCodigoProyecto():
                        print(proy.toString())
#______________________________________________________________________________     
    def eliminarParticipacion(self):
        codigoDelProfe = int(input('Diga el codigo del Profesor'))
        codigoDelProy = int(input('Diga el codigo del Proyecto'))
        if self.existeCodigo(codigoDelProfe, codigoDelProy)== False:
            print('El codigo no existe!')
        else:
            for proy in self.misParticipaciones:
                if codigoDelProfe==proy.getCodigoProfe() and codigoDelProy == proy.getCodigoProyecto():
                    self.misParticipaciones.remove(proy)
                    print('El proyecto se ha eliminado')
#______________________________________________________________________________ 
    def modificarParticipacion(self):
        codigoModProfe = int(input('Diga el codigo del Profesor'))
        codigoModProy = int(input('Diga el codigo del Proyecto'))
        if self.existeCodigo(codigoModProfe, codigoModProy)== False:
            print('El codigo no existe!')
        else:
            for proy in self.misParticipaciones:
                if codigoModProfe==proy.getCodigoProfe() and codigoModProy == proy.getCodigoProyecto():
                    codigoNewProfe = int(input('Diga el codigo nuevo del Profesor'))
                    codigoNewProy = int(input('Diga el codigo nuevo del Proyecto'))
                    if self.existeCodigo(codigoNewProfe, codigoNewProy)== True :
                        print('El codigo ya existe')
                    else:
                        horasNew = int(input('Diga las horas de la participacion'))
                        proy.setCodigoProfe(codigoNewProfe)
                        proy.setCodigoProyecto(codigoNewProy)
                        proy.setHoras(horasNew)
                        print('La participacion fue modificada')       
          
#______________________________________________________________________________ 
    def existeCodigo (self,codigoProfe, codigoProyecto):
        for participacion in self.misParticipaciones:
            if codigoProfe == participacion.getCodigoProfe() and codigoProyecto == participacion.getCodigoProyecto():
                return True
        return False
#______________________________________________________________________________ 
