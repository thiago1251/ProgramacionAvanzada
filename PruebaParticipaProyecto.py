from ParticipaProyecto import ParticipaProyecto

p1 = ParticipaProyecto(1111, 2, 5)
p2 = ParticipaProyecto(2222, 3, 6)

print('Participacion Proyecto 1:', p1.getCodigo())
print('Horas paticipacion Proyecto 2:', p2.getHoras())

cod = int ( input('Diga el codigo del Profesor:'))
cod2 = int(input('Diga el codigo del Proyecto:'))
horas= int(input('Diga las horas de la participacion:'))


p3 = ParticipaProyecto(cod, cod2,horas)
print(p3.toString())

p2.setHoras(3)
print(p2.toString())

