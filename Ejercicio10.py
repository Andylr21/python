
suma = 0 
contador = 0


numero = int(input("Ingresar numero"))
while(numero > 0):   
    if(numero > 0):
        suma = suma + numero
        contador = contador + 1
    numero = int(input("Ingresar numero"))
promedio = suma / contador 

print("El promedio es",(promedio))
