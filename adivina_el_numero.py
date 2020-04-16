import random

def adivina_el_numero():
    numero_a_adivinar = random.randint(1, 11)
    while True:
        numero_ingresado_por_usuario = int(input("Ingresa un numero entre 1 y 10: "))
        if numero_a_adivinar == numero_ingresado_por_usuario:
            print("Adivinaste el numero")
            break
        elif numero_a_adivinar > numero_ingresado_por_usuario:
            print("El numero que ingresaste es menor que el número a adivinar")
            continue
        elif numero_a_adivinar < numero_ingresado_por_usuario:
            print("El numero que ingresaste es mayor que el número a adivinar")
            continue

if __name__ == '__main__':
    adivina_el_numero()