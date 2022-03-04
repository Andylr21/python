# Definición de las variables

grados_c = float(input("Escribe los grados °C: "))
grados_f = float(input("Escribe los grados °F: "))
grados_k = float(input("Escribe los grados K:"))

# Proceso 

gradosc = grados_k - 273.15
gradosf = (9 * (grados_k - 273.15) / 5) + 32
gradosk = grados_c + 273.15
grados_k_2= (5 * (grados_f - 32) / 9) +273.15



# Salida de datos 
print(" Los grados C =",(gradosc))
print(" Los grados F =",(gradosf))
print(" Los grados K =",(gradosk))
print(" Los grados K2 =",(grados_k_2))