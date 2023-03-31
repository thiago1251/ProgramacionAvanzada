class Proyecto:
    def __init__ (self, codigoNew, nombreNew, presupuestoNew, fechaInicioNew, liderNew ):
          #Atributos
          self. codigo = codigoNew
          self. nombre = nombreNew
          self. presupuesto = presupuestoNew
          self. fechaInicio = fechaInicioNew
          self. lider = liderNew
          print('Objeto tipo Proyecto creado...')
          
      #Analizadores
    def getCodigo(self):
          return self.codigo
      
    def getNombre(self):
          return self.nombre
      
    def getPresupuesto(self):
          return self.presupuesto
      
    def getFechaInicio(self):
        return self.fechaInicio
    
    def getLider(self):
        return self.lider
      

      #Modificadores
    def setCodigo(self, codigoNew):
          self.codigo = codigoNew
          
    def setNombre(self, nombreNew):
          self.nombre = nombreNew
       
    def setPresupuesto(self, presupuestoNew):
          self.presupuesto = presupuestoNew
         
    def setFechaInicio(self, fechaInicioNew):
        self.fechaInicio = fechaInicioNew
    
    def setLider(self, liderNew):
        self.lider = liderNew
       
    def toString (self):
          return ('Codigo =', self.codigo, 'Nombre =', self.nombre, 'Presupuesto =', 
                  self.presupuesto, 'Fecha Inicio =', self.fechaInicio, 'Lider =', self.lider)