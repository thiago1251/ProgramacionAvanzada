from Proyecto import Proyecto

p1 = Proyecto(1111, 'Pepito Perez', '4783783', '15/09/2023', 1)
p2 = Proyecto(2222, 'Juan Alvarez', '7468436', '12/09/2022', 2)

print('Nombre 1:', p1.getNombre())
print('lider 2:', p2.getLider())

cod = int ( input('Diga el codigo:'))
nom = input('Diga el Nombre:')
presupues = input('Diga el presupuesto:')
date = input('Diga la fecha de Inicio:')
boss = int ( input('Diga el profesor lider:'))

p3 = Proyecto(cod, nom, presupues, date, boss)
print(p3.toString())

p2.setLider(3)
print(p2.toString())

