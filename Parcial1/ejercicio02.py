
import string

# Importar random para usar el metodo choice, que elije un elemento al azar de un iterable
import random

minusculas_ascii = string.ascii_lowercase
#print(minusculas_ascii)

mayusculas_ascii = string.ascii_uppercase
#print(mayusculas_ascii)

numeros = string.digits
#print(numeros)


def generarPassword(n):
    # Escribe una funcion que genere un password aleatorio de n caracteres
    # el password debe contener letras mayusculas minusculas y numeros

    # Definir una lista con todos los símbolos posibles
    simbolos = minusculas_ascii + mayusculas_ascii + numeros

    password = ''
    for _ in range(n):
        # Elegir con el método choice un elemento aleatorio de la lista de simbolos
        # y concatenar con la variable contraseña hasta la cantidad de caracteres indicada
        password += random.choice(simbolos)
    return password

for i in range(10, 20):
    print(generarPassword(i))