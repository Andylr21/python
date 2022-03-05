#Pedir la edad


edad = float(input("Escribe el año actual: "))
#Entrada de datoe
 
if (edad >=18 and edad <= 120): #(18 - # si se cumple o es verdadera
    print("Mayor de edad")
elif (edad >= 1 and edad < 18): #(1-17)
    print("Menor de edad")
else:
    print("Edad no EXISTE")