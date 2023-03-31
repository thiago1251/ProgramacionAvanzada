class Profesor:
    def __init__ (self, codigoNew, nombreNew, direccionNew, telefonoNew, programaNew ):
          #Atributos
          self. codigo = codigoNew
          self. nombre = nombreNew
          self. direccion = direccionNew
          self. telefono = telefonoNew
          self. programa = programaNew
          print('Objeto tipo Profesor creado...')
          
      #Analizadores
    def getCodigo(self):
          return self.codigo
      
    def getNombre(self):
          return self.nombre
      
    def getDireccion(self):
          return self.direccion
      
    def getTelefono(self):
        return self.telefono
    
    def getPrograma(self):
        return self.programa
      
      #Modificadores
    def setCodigo(self, codigoNew):
          self.codigo = codigoNew
          
    def setNombre(self, nombreNew):
          self.nombre = nombreNew
       
    def setDireccion(self, direccionNew):
          self.direccion = direccionNew
         
    def setTelefono(self, telefonoNew):
        self.telefono = telefonoNew
    
    def setPrograma(self, programaNew):
        self.programa = programaNew
       
    def toString (self):
          return ('Codigo =', self.codigo, 'Nombre =', self.nombre, 'Direccion =', 
                  self.direccion, 'Telefono =', self.telefono, 'Programa =', self.programa)
      
  