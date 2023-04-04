from Admon.AdmonFuentes import AdmonFuentes
from Admon.AdmonProfesores import AdmonProfesores
from Admon.AdmonDepartamentos import AdmonDepartamentos
from Admon.AdmonParticipaProyectos import AdmonParticipaProyectos
from Admon.AdmonProyectos import AdmonProyectos
from Admon.AdmonFinanciacionesProyectos import AdmonFinanciancianesProyectos

class Entrada:

    #Constuctor
    def __init__(self):
        print('Objeto tipo Entrada creado y listo para usarse..!!')
        self.menu()

    # métodos
    def menu(self):
        opcion = -1
        while opcion != 0:
            print('==================================')
            print('............OPCIONES..............')
            print('==================================')
            print('0. Salir')          
            print('1. FUENTES DE FINANCIACION')
            print('2. PROFESORES')
            print('3. DEPARTAMENTOS')
            print('4. PROYECTOS')
            print('5. PROGRAMAS')
            print('6. PARTICIPACION PROYECTOS')
            print('7. FINANCIACION PROYECTOS')
            opcion = int(input('Digite su opción:'))

            if opcion == 0:
                print("Adios ..!!")

            elif opcion == 1:
                AdmonFuentes()
            elif opcion == 2:
                AdmonProfesores()
            elif opcion == 3:
                AdmonDepartamentos()
            elif opcion == 4:
                AdmonProyectos()
            elif opcion == 5:
                print('Proceso no realizado')
            elif opcion == 6:
               AdmonParticipaProyectos()
            elif opcion == 7:
                AdmonFinanciancianesProyectos()

            else:
                print('Esa opción NO existe..!!!')


Entrada()
