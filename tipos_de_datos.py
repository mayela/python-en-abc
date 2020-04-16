#Varibles

entero = 3
flotante = 4.5
cadena = "Hola a todos"

# Constantes

PI = 3.1416

mi_conjunto = {1, 2, 3, 4}
mi_lista = [1, 2, "hola", "azul", 6]
mi_tupla = (1, "Adios", 4, 6)
mi_diccionario = {
    "nombre": "Maricela",
    "apellido": "Sanchez",
    "color_favorito": "negro"
}


class Bicicleta:
    def __init__(self, rodada, velocidad):
        # Atributos
        self.rodada = rodada
        self.velocidad = velocidad

    #Comportamiento

    def cambiar_velocidad(self, nueva_velocidad):
        self.velocidad = nueva_velocidad

    def frenar(self):
        self.velocidad = 0


