class Profesor:

    #Constructor
    def __init__(self,idProfesorNew,nombreNew,direccionNew, telefonoNew, programaNew):
        self.idProfesor = idProfesorNew
        self.nombre = nombreNew
        self.direccion = direccionNew
        self.telefono = telefonoNew
        self.programa = programaNew

    #Modificadores
    def setIdProfesor(self,idProfesorNew):
        self.idProfesor=idProfesorNew

    def setNombre(self,nombreNew):
        self.nombre=nombreNew

    def setDireccion(self,direccionNew):
        self.direccion=direccionNew
        
    def setTelefono(self,telefonoNew):
        self.telefono=telefonoNew
    
    def setPrograma(self,programaNew):
        self.programa=programaNew
        

    #Analizadores
    def getIdProfesor(self):
        return self.idProfesor

    def getNombre(self):
        return self.nombre

    def getTelefono(self):
        return self.telefono
    
    def getPrograma(self):
        return self.programa

    
    #toString
    def toString(self):
        return "Profesor ID =", self.idProfesor, "Nombre = ", self.nombre,'Direccion =', self.direccion ,"Telefono =" , self.telefono,'Programa =', self.programa