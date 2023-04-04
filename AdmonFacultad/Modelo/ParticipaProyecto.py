class ParticipaProyecto:
    def __init__ (self, idNewProfesor, idNewProyecto, horasNew ):
          #Atributos
          self. idProfesor = idNewProfesor
          self. idProyecto = idNewProyecto
          self. horas = horasNew
          self. codigo = [idNewProfesor,idNewProyecto]
          print('Objeto tipo Participa Proyecto creado...')
          
      #Analizadores
    def getIdProfe(self):
          return self.idProfesor
      
    def getIdProyecto(self):
          return self.idProyecto
      
    def getCodigo(self):
        return self.codigo
      
    def getHoras(self):
          return self.horas 
      

      #Modificadores
    def setIdProfe(self, idNewProfesor):
          self.idProfesor = idNewProfesor
          
    def setIdProyecto(self, idNewProyecto):
          self.idProyecto = idNewProyecto
 
       
    def setHoras(self, horasNew):
          self.horas = horasNew
    
    def toString (self):
          return ('Codigo Partcipacion Proyecto =', self.idProfesor , self.idProyecto, 'Horas =', self.horas)