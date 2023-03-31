class Financiacion:
    def __init__ (self, codigoNewProyecto, codigoNewFuente, montoNew ):
          #Atributos
          self. codigoProyecto = codigoNewProyecto
          self. codigoFuente = codigoNewFuente
          self. monto = montoNew
          self. codigo = [codigoNewProyecto,codigoNewFuente]
          print('Objeto tipo Financiacion creado...')
          
      #Analizadores
    def getCodigoProyecto(self):
          return self.codigoProyecto
      
    def getCodigoFuente(self):
          return self.codigoFuente
      
    def getCodigo(self):
        return self.codigo
      
    def getMonto(self):
          return self.monto
      

      #Modificadores
    def setCodigoProyecto(self, codigoNewProyecto):
          self.codigoProyecto = codigoNewProyecto
          
    def setCodigoFuente(self, codigoNewFuente):
          self.codigoFuente = codigoNewFuente
 
       
    def setMonto(self, montoNew):
          self.monto = montoNew
    
    def toString (self):
          return ('Codigo Financiacion Proyecto =', self.codigoProyecto , self.codigoFuente, 'Monto = $', self.monto)

