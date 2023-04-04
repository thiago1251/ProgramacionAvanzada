class Departamento:
    #Constructor
    def __init__(self,idDeptoNew,nombreNew,extencionNew, jefeNew):
        self.idDepto=idDeptoNew
        self.nombre=nombreNew
        self.extencion=extencionNew
        self.jefe = jefeNew

    #Modificadores
    def setIdDepto(self,idDeptoNew):
        self.idDepto=idDeptoNew

    def setNombre(self,nombreNew):
        self.nombre=nombreNew

    def setExtencion(self,extencionNew):
        self.extencion=extencionNew
        
    def setJefe(self, jefeNew):
        self.jefe=jefeNew

    #Analizadores
    def getIdDepto(self):
        return self.idDepto

    def getNombre(self):
        return self.nombre

    def getExtencion(self):
        return self.extencion
    
    def getJefe(self):
        return self.jefe
    
    #toString
    def toString(self):
        return "Departamento ID =", self.idDepto, "Nombre = ", self.nombre,"Extencion =" , self.extencion, 'Jefe =', self.jefe