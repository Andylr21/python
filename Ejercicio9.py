# Definición de las variables

días_laborales = float(input("Escribe los días laborales : "))
pagoxdía = float(input("Escribe el pago por día: "))



# Proceso 

pago_base = días_laborales * pagoxdía
iva_trasladado = pago_base * .16
subtotal = pago_base + iva_trasladado
iva_retenido = iva_trasladado * 2/3
isr_retenido = pago_base * .10
pago_neto = subtotal - isr_retenido - iva_retenido

# Salida de datos

print(" pago base =",(pago_base))
print(" iva trasaladado =",(iva_trasladado))
print(" subtotal =",(subtotal))
print(" iva retenido =",(iva_retenido))
print(" isr retenido =",(isr_retenido))
print(" pago neto =", round(pago_neto,2))