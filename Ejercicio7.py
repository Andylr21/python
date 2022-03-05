#Pedir la edad
agua_metros =  float(input("Escribe el nivel del agua en metros de una cisterna: "))

# Proceso 

if (agua_metros > 6):
    print("Desbordamiento de agua en cisterna")
elif(agua_metros == 6):
    print("Apagar Bomba")
elif(agua_metros>=4 and agua_metros<6):
    print("Desacelerar Bomba")
elif(agua_metros>=2 and agua_metros<=4):
    print("Bomba trabajando")
elif(agua_metros>0 and agua_metros<=2):
    print("Acelerar bomba de agua")
elif(agua_metros == 0):
    print("Encender Bomba de agua")
elif (agua_metros < 0):
    print("Fuga en cisterna")
else:
    print("El nivel de metros no es ACEPTADO")
