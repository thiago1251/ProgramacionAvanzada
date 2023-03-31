from Fuente import Fuente

p1 = Fuente(1111, 'Pepito Perez', 'Casanare', '3134532' )
p2 = Fuente(2222, 'Juan Alvarez', 'Funza', '847923')

print('Nombre 1:', p1.getNombre())
print('Direccion 2:', p2.getDireccion())

cod = int ( input('Diga el codigo:'))
nom = input('Diga el Nombre:')
dire = input('Diga la direccion:')
tele = input('Diga el telefeno:')

p3 = Fuente(cod, nom, dire, tele)
print(p3.toString())

p2.setDireccion('Chia')
print(p2.toString())

