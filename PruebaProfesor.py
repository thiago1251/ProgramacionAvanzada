from Profesor import Profesor

p1 = Profesor(1111, 'Pepito Perez', 'Casanare', '3134532', 1 )
p2 = Profesor(2222, 'Juan Alvarez', 'Funza', '847923', 2)

print('Nombre 1:', p1.getNombre())
print('Direccion 2:', p2.getDireccion())

cod = int ( input('Diga el codigo:'))
nom = input('Diga el Nombre:')
dire = input('Diga la direccion:')
tele = input('Diga el telefeno:')
prog = int ( input('Diga el programa:'))

p3 = Profesor(cod, nom, dire, tele, prog)
print(p3.toString())

p2.setDireccion('Chia')
print(p2.toString())

