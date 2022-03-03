# Ejemplo 2. Operaciones Matemáticas

#Importar una Libreria de Funciones Matemáticas
import math 


#Entrada de datos
# DEFINICION DE LAS VARIABLES (Declarar/Creación)
número1 = float(input("Escribe el 1er número: ")) # Ingresando texto
número2 = float(input("Escribe el 2do número: "))

# PROCESOS (Cálculos u Operaciones Matemáticas y lógicas
suma = número1 + número2
resta = número1 - número2
mutiplicación = número1 * número2
división = número1 / número2
potencia1 = número1 ** número2
potencia2 = pow(número1,número2)
cuadrado = número1 ** 2
cubo = pow(número2,3)
raíz_cuadrada1 = pow(número1, 1/2)
raíz_cuadrada2 = math.sqrt(número1)
raiz_cubica = pow(número2, 1/3)
módulo = número1 % número2

# Saida de datos
print("La suma =", suma) #1ra Forma
print("La suma = " + str(suma)) #2da Forma Concatenación/u
print(f"Lasuma = {suma}") # 3ra Forma interpolacion de cadena

print("La resta =", resta) 
print("La resta = " + str(resta)) 
print(f"La resta = {resta}") 

print("La multiplicación =", mutiplicación) #1ra Forma
print("La multiplicación = " + str(mutiplicación)) 
print(f"La multiplicación = {mutiplicación}")

print("La división =", división) 
print("La división = " + str(división)) 
print(f"La división = {división}") 

print("La pontencia1 =", potencia1)
print("La pontencia1 = " + str(potencia1)) 
print(f"La pontencia1 = {potencia1}")

print("La pontencia2 =", potencia2)
print("La pontencia2 = " + str(potencia2)) 
print(f"La pontencia2 = {potencia2}")

print("cuadrado =", cuadrado)
print("cuadrado = " + str(cuadrado)) 
print(f"cuadrado = {cuadrado}")

print("cubo =", cubo)
print("cubo = " + str(cubo)) 
print(f"cubo = {cubo}")

print("La raíz cuadrada 1 =", raíz_cuadrada1)
print("La raíz cuadrada 1 = " + str(raíz_cuadrada1)) 
print(f"La raíz cuadrada 1 = {raíz_cuadrada1}")

print("La raíz cuadrada 2=", raíz_cuadrada2)
print("La raíz cuadrada 2 = " + str(raíz_cuadrada2)) 
print(f"La raíz cuadrada 2 = {raíz_cuadrada2}")

print("La raíz cubica =", raiz_cubica)
print("La raíz cubica  = " + str(raiz_cubica)) 
print(f"La raíz cubica = {raiz_cubica}")

print("Módulo=", módulo)
print("Módulo = " + str(módulo)) 
print(f"Módulo = {módulo}")