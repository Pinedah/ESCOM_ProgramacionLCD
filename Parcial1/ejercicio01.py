
import string

caracteres_ascii = string.ascii_letters
print(caracteres_ascii)

def verificar(cadena):
    # Escribe el codigo que verifique que todos los caracteres de una
    # cadena son letras ASCII
    # Devuelve: True en caso de que todos los caracteres sean letras ascii
    #           False en caso contrario

    # Reemplazar los espacios con un caracter vacio
    cadena = cadena.replace(' ', '')
    for caracter in cadena: 
        # Iterar sobre cada caracter y verificar si está en la lista que contiene a los ASCII
        if caracter not in caracteres_ascii:
            # Devolver False si es que alguno ya no es ASCII
            return False
    # Devolver True si es que el se termino el ciclo
    return True 
    
cadena1 = "Esto es un a cadena$"
print(f"{cadena1}\t-> {verificar(cadena1)}")

cadena2 = "Esto es un a cadena"
print(f"{cadena2}\t-> {verificar(cadena2)}")