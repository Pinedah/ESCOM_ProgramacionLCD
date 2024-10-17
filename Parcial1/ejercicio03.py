# Crear un programa que genere 100 numeros aleatorios entre 1 y 1000
# inserte en una lista los pares y en otra los impares
# Imprimir ambas listas y el tamaño de las mismas

# Importar random para generar aleatorios
import random 

def main():

    # Creación de la lista de aleatorios con List Comprehension
    aleatorios = [random.randint(1, 1001) for _ in range(100)]
    
    # Funciones lambda para filtrar
    esPar = lambda x: x % 2 == 0
    esImpar = lambda x: x % 2 == 1

    # Creación de las listas pares e impares con Filter
    pares = list(filter(esPar, aleatorios))
    impares = list(filter(esImpar, aleatorios))

    # Impresiones de las listas
    print(f"\nLista original: \n{aleatorios}\n")
    print(f"Pares: \n{pares}\n")
    print(f"Imares: \n{impares}")

if __name__ == "__main__":
    main()