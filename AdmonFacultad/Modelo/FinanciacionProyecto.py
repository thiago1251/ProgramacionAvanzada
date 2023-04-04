
class FinanciacionProyecto:
    def __init__ (self, idProyectoNew, idFuenteNew, montoNew ):
          #Atributos
          self. idProyecto = idProyectoNew
          self. idFuente = idFuenteNew
          self. monto = montoNew
          print('Objeto tipo Financiacion creado...')
          
      #Analizadores
    def getIdProyecto(self):
          return self.idProyecto
      
    def getIdFuente(self):
          return self.idFuente
      
    def getMonto(self):
          return self.monto
      

      #Modificadores
    def setIdProyecto(self, idProyectoNew):
          self.idProyecto= idProyectoNew
          
    def setCodigoFuente(self, idFuenteNew):
          self.idFuente = idFuenteNew
 
       
    def setMonto(self, montoNew):
          self.monto = montoNew
    
    def toString (self):
          return ('Codigo Financiacion Proyecto =',  self.idProyecto, self.idFuente ,'Monto = $', self.monto)
