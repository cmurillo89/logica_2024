#APRENDAMOS UN NUEVO CONCEPTO QUE EXPLICA COMO LAS VARIABLES SE COMPORTAN O REALIZAN UN SEGUIMIENTO DE COSAS COMO AGREGAR O QUITAR VALORES
#PARA ESTO UTILIZAMOS COMUNMENTE LOS BUCLES
#LOS BUCLES NOS PERMITEN EJECUTAR UNA SERIE DE INSTRUCCIONES VARIAS VECES

wallet = 1000

#Vamos a hacer un bucle que le agregue 100 a la billetera 5 veces
#Bucle FOR
#El bucle for nos permite ejecutar un bloque de codigo varias veces

for i in range(15):
    wallet = wallet + 100
    print("El saldo de su billetera es:", wallet)
    print("El valor de i es:", i)

#AHORA VAMOS A VER EL BUCLE WHILE
#El bucle while nos permite ejecutar un bloque de codigo mientras una condicion sea verdadera
    
print("Vamos a trabajar con el bucle while")
wallet = 1000
while True:
    print("El saldo de su billetera es:", wallet)
    wallet = wallet + 100
    if wallet == 2500:
        break
print("El saldo de su billetera es:", wallet)
print("El bucle while ha terminado")
print("-------------------")

#Vamos a agregar condiciones a los bucles
wallet = 1000
while wallet < 2500 and wallet > 0:
    wallet = wallet + 100
    print("El saldo de su billetera es:", wallet)
    
#PODEMOS USAR CONTADORES CON EL BUCLE WHILE

print("Vamos a trabajar con contadores")
dias = 0
kilometros = 0

while kilometros < 50000 or dias < 10:
    dias = dias + 1
    kilometros = int(input("Digite los kilometros recorridos por el auto: "))
    if kilometros >= 50000:
        print("El auto ha recorrido más de 50000 kilómetros, ya no tiene garantía")
        break

    print("El auto está en garantía desde hace", dias, "días")