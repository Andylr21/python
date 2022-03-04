# Definición de las variables

a = float(input("Escribe el valor de a: "))
b= float(input("Escribe el valor de b: "))
c= float(input("Escribe el vaor de c:"))

# Proceso 

x1 = (- b - (pow(b ** 2 - 4 * a * c, 1/2))) / (2 * a)
x2 = (- b + (pow(b ** 2 - 4 * a * c, 1/2))) / (2 * a)

# Salida de datos 
print(" X1 es =",round(x1,2))
print(" X2 es =",round(x2,2))