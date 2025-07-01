file =open("EjemploArchivo.txt","w")
file.write("Este es el contenido del archivo.")
file.close()

lista=["Fresa", "Kiwi", "Sandia"]

with open("EjemploArchivo.txt", "a") as file:
    for e in lista:
        file.write(e +"\n")

print("Lista escrita en el archivo")

lista2=["Honda", "Suzuki","BMW"]

with open("EjemploArchivo.txt", "a") as file:
    for e in lista2:
        file.write(e +"\n")

print("Imprimir todo el contenido del archivo")
with open("EjemploArchivo.txt", "r") as file:
    print(file.read())

print("Leer dos líneas y posteriormente 5 caracteres")
with open ("EjemploArchivo.txt", "r") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline(5))

print("Alamacenar el contenido en una lista y mostrar el contenido")
with open("EjemploArchivo.txt", "r") as file:
    contenido=file.readlines()
    print(contenido[-1])

