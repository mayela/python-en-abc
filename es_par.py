def es_par(numero):
    if numero % 2 == 0:
        print("El numero que ingresaste es par")
    else:
        print("El numero que ingresaste es impar")

if __name__ == '__main__':
    numero = int(input("Ingresa un numero entero: "))
    es_par(numero)