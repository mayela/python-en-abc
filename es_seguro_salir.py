import datetime
from random import choice

hoy = datetime.datetime.now()
fin_jornada_distanciamiento = datetime.datetime(2020, 5, 30)
aprobacion_autoridades = choice([True, False])

def es_seguro_salir():
    if hoy > fin_jornada_distanciamiento and aprobacion_autoridades:
        print("Es seguro salir tomando tus precacuiones de distacia y "
              "lavandote las manos"
              )
    elif hoy > fin_jornada_distanciamiento and aprobacion_autoridades == False:
        print("Quédate en casa , si tu situación lo permite, hasta que las "
              "autoridades notifiquen que es seguro salir"
              )
    elif hoy < fin_jornada_distanciamiento and aprobacion_autoridades:
        print("Es seguro salir tomando tus precauciones")
    else:
        print("Quédate en casa si tu sitaución lo permite")

if __name__ == '__main__':
    es_seguro_salir()
