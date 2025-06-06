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

    print(".....Operadores lógicos.....")
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
    print(".....Operadores de comparación.....")

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

print(".....Variables.....")

