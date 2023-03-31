from Financiacion import Financiacion

p1 = Financiacion(1111, 2, 5)
p2 = Financiacion(2222, 3, 6)

print('Participacion Proyecto 1:', p1.getCodigo())
print('Monto Proyecto 2:', p2.getMonto())

cod = int ( input('Diga el codigo del Proyecto:'))
cod2 = int(input('Diga el codigo de la fuente:'))
monto= int(input('Diga el monto dispuesto por la fuente:'))


p3 = Financiacion(cod, cod2,monto)
print(p3.toString())

p2.setMonto(3)
print(p2.toString())

