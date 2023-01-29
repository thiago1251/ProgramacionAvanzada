#Elaborarun programa que diga cuántos
# y cuales números primos hay en un intervalo (a, b).

a=int(input('Digite el primer numero del intervalo'))
b=int(input('Digite el segundo numero del intervalo'))
#contador=0
primos = []
rango=[]
contador=0 #se sabe que un numero primo es divisible entre uno y el mismo, este cuenta esos dos cocientes
count=0 # cuenta cuantos primos hay

for num in range(a, b+1):
    rango.append(num)#rango dado a una lista

for i in rango:
    for x in range(1,i+1):
        if i%x==0:# si el modulo es cero es divisible
            contador=contador+1# si es divisible dos veces es primo
        if contador==2:# si hay dos diviciones exactas
          count=count+1# Este contador cuenta cuantos primos hay
          primos.append(i)# los añado

#pero solo funciona con el primer numero primo y ya lo intente como 3 horas y nada, ayudaaa
print(primos)
print(count)
print(rango)
