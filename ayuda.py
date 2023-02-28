##########################################
# Signos #
"""
Suma --> +
Resta --> -
División --> /
Multiplicacción --> *
Potencias --> **
Resto --> %
Cociente --> //
"""
# Tipos de Variables #
"""
String --> str
Integral --> int
Float --> flt
Bool --> bool
"""
var1 = "Hola" # string
var2 = 123 # integral |-/+|
var3 = 123.123 # float |-/+|
var4 = True # bool
##########################################
# Condicionales #
"""
Igualdad --> '=='
No igualdad --> '!='

Mayor que --> '>'
Menor que --> '<'

Mayor igual que --> '>='
Menor igual que --> '<='
"""
myvar1 = 20 # Definir var1
myvar2 = 20 # Definir var2

if myvar1 == myvar2: # false
    print("son iguales")
elif myvar1 > myvar2: # false
    print("myvar1 es mayor que myvar2")
else:
    print("las dos anteriores condiciones son falsas")

### Solo sucede una condicion. Si quieres mas...

if myvar1 >= myvar2:
    print("myvar1 es mayor que myvar2") # 1a condicion
    if myvar1 == myvar2:
        print("son iguales") # 2a condicion

# En este caso verifica si myvar1 es mayor o igual que myvar2, y ademas verifica si son iguales con la senguda condicion.
##########################################
# Bucles #

#while True: # bucle infinito /!\
    print("Hola")


### El bucle 'while' solo funcionara si es 'True', como:

# while 10 < 20: # bucle infinito /!\, siempre dara 'True'
    print("hola")

### Para que el bucle no sea infinito...
myvar3 = 0

while myvar3 > 10:
    myvar3 += 1

#importancia! esto lo debe tner un programa si o si para ue funcione
while True:
    event, values = windows.read()
    if event == sg.WIN_CLOSED:
        break

windows.close()