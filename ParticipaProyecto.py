class ParticipaProyecto:
    def __init__ (self, codigoNewProfe, codigoNewProyecto, horasNew ):
          #Atributos
          self. codigoProfe = codigoNewProfe
          self. codigoProyecto = codigoNewProyecto
          self. horas = horasNew
          self. codigo = [codigoNewProfe,codigoNewProyecto]
          print('Objeto tipo Participa Proyecto creado...')
          
      #Analizadores
    def getCodigoProfe(self):
          return self.codigoProfe
      
    def getCodigoProyecto(self):
          return self.codigoProyecto
      
    def getCodigo(self):
        return self.codigo
      
    def getHoras(self):
          return self.horas 
      

      #Modificadores
    def setCodigoProfe(self, codigoNewProfe):
          self.codigoProfe = codigoNewProfe
          
    def setCodigoProyecto(self, codigoNewProyecto):
          self.codigoProyecto = codigoNewProyecto
 
       
    def setHoras(self, horasNew):
          self.horas = horasNew
    
    def toString (self):
          return ('Codigo Partcipacion Proyecto =', self.codigoProfe , self.codigoProyecto, 'Horas =', self.horas)