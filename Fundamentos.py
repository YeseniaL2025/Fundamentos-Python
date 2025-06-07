def nuevoTema(tema):
    print("\n-----", tema, "-----\n")


if __name__ == "__main__":
    
    nuevoTema("Operadores Ariméticos")
# Suma
    print("Operador suma, 5 + 6 =", 5 + 6)
# Resta
    print("Operador resta, 6 - 10 =", 6 - 10) 
# Multiplicación
    print("Operador multiplicación, 24 * 20 =", 24 * 20)
# División
    print("Operador división, 20 / 4 =", 20 / 4)
# División entera
    print("Operador división entera, 20 // 3 =", 20 // 3)
# Módulo (residuo de una división)
    print("Operador módulo, 20 % 3 =", 20 % 3)
# Exponente
    print("Operador exponente, 2 ** 3 =", 2 ** 3)

    nuevoTema(".....Operadores lógicos.....")
# Variables de ejemplo
    a = True
    b = False
# Operador AND (y)
    print("Operador AND: True and False =", a and b)
# Operador OR (o)
    print("Operador OR: True or False =", a or b)
# Operador NOT (no)
    print("Operador NOT: not True =", not a)
    print("Operador NOT: not False =", not b)

    #TAREA 1. Hacer las tablas de verdad
        # Tabla de verdad para AND
    nuevoTema(".....Tablas de Verdad.....")
    print("Tabla de verdad: AND")
    print("A\tB\tA and B")
    print("True\tTrue\t", True and True)
    print("True\tFalse\t", True and False)
    print("False\tTrue\t", False and True)
    print("False\tFalse\t", False and False)
    print()

        # Tabla de verdad para OR
    print("Tabla de verdad: OR")
    print("A\tB\tA or B")
    print("True\tTrue\t", True or True)
    print("True\tFalse\t", True or False)
    print("False\tTrue\t", False or True)
    print("False\tFalse\t", False or False)
    print()

        # Tabla de verdad para NOT
    print("Tabla de verdad: NOT")
    print("A\tnot A")
    print("True\t", not True)
    print("False\t", not False)

    #2 TAREA 1. ejemplo de cada operador de comparación.
    nuevoTema(".....Operadores de comparación.....")

# Igual a
    print("5 == 5 →", 5 == 5)  # True

# Distinto de
    print("3 != 4 →", 3 != 4)  # True

# Mayor que
    print("10 > 7 →", 10 > 7)  # True

# Menor que
    print("2 < 5 →", 2 < 5)  # True

# Mayor o igual que
    print("6 >= 6 →", 6 >= 6)  # True

# Menor o igual que
    print("4 <= 9 →", 4 <= 9)  # True

nuevoTema(".....Variables.....")
variable1=10
_variable2=6.2547
variable3="Pepe"
nombreVariable=8
nombre_variable=34.2
print(variable1, _variable2, variable3, nombreVariable, nombre_variable)

a, b, c = 5, 10, 8
print(a)
print(b)
print(c)

nombre_variable = "Adios"
print(nombre_variable)

nuevoTema("Enteros")
w=103
x=32322
y=-58
z=0b01011100
h=0xFF

print(w, type(w))
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(h, type(h))

nuevoTema("Flotantes")
x=12134.56
print(x, type(x))
y=-0.43423
print(y, type(y))

nuevoTema("Números complejos")
          
x=-123j
y=12+54j
z=3j
c=y+z

print(x, type(x))
print(y, type(y))
print(z, type(y)) 
print(c, type(c)) 

nuevoTema("Booleanos")
x=True
print(x, type(x))

nuevoTema("Listas")
lista=[10,20,5, "Listas de Python"]
print(lista)
print(lista[1])
lista[0]="Hola"
lista.append(34)
print(lista)
lista.insert(0,1.1)
print(lista)
lista.append([3,4,5,6,7,8])
print(lista)
print(lista[6])
print(lista[6][4])

nuevoTema("Tuplas")
tupla=(25, "Tupla", 1+10)
print(tupla)
print(tupla[1])

nuevoTema("Conjunto")
conjunto={1, 20, 30, 40, 50}
print(conjunto)
print (50 in conjunto)

nuevoTema("Diccionarios")
diccionario={"Nombre":"Luna", "Teléfono": 2344343432,90:4+3}
print(diccionario)
print(diccionario["Teléfono"])
print(diccionario[90])

nuevoTema("Cadenas")
cadena1="Esto es una cadena"
cadena2='Esto es una cadena'
cadena_multilinea='''esto es una cadena 
de varias
lineas con tabuladores
saltos de 
línea'''
print(cadena1, type(cadena1))
print(cadena2, type(cadena2))
print(cadena_multilinea, type(cadena_multilinea))

cadena3= "Hola"*5
print(cadena3)
print(cadena1[2])
print(cadena1[2:10])
print(cadena1[:5])
print(cadena1[5:])
print(cadena1[::-1])