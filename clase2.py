# Vamos a ver tipos y comparaciones de variables
#PODEMOS USAR COMPARACIONES PARA COMPROBAR SI UN NUMERO ES MENOR O A
#MAYOR QUE OTRO, O SI SON IGUALES

print(1<90)
print(54>90)
print(70>=70)

#PODEMOS USAR COMPARACIONES PARA COMPROBAR SI UNA CADENA ES IGUAL A OTRA
pin_correcto = 1234
pin_usuario = 1234
print("El PIN que digitó es:", pin_correcto == pin_usuario, "El PIN es correcto")

#PODEMOS USAR COMPARACIONES PARA COMPROBAR SI UNA CADENA ES DIFERENTE A OTRA
print("Hay diferencia entre pines?",pin_correcto != pin_usuario)

#PODEMOS USAR COMPARACIONES PARA COMPROBAR SI UNA CADENA ES IGUAL A OTRA
#O SI UNA CADENA ES MAYOR O MENOR QUE OTRA
print("El PIN es mayor que el PIN del usuario?",pin_correcto > pin_usuario)
print("El PIN es menor que el PIN del usuario?",pin_correcto < pin_usuario)


#CONDICIONALES
#LOS CONDICIONALES NOS PERMITEN EJECUTAR UNA SERIE DE INSTRUCCIONES
#CUANDO SE CUMPLE UNA CONDICION
#SI LA CONDICION SE CUMPLE, EJECUTA EL BLOQUE DE CODIGO
#SI LA CONDICION NO SE CUMPLE, NO EJECUTA EL BLOQUE DE CODIGO

#CONDICIONAL IF

if True:
    print("La condicion se cumple")

if 54 > 90:
    print("La condicion se cumple, efectivamente 54 es menor que 90")
else:
    print("La condicion no se cumple, 54 no es mayor que 90")

print("-------------------")
print("Vamos a trabajar con el condicional if")

nota = int(input("Digite la nota del alumno: "))
if nota >= 70 and nota <= 100:
    print("El alumno aprobó")
elif nota >= 60 and nota < 70:
    print("El alumno está en recuperación")
elif nota >= 0 and nota < 60:
    print("El alumno reprobó")
else:
    print("La nota no es válida, no sea caballo")

