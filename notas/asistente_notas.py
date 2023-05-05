from tools import clean_screen
from time import sleep


def menu():
    while True:
        try:
            clean_screen()
            opcion = int(input("""
            Acciones disponibles:
            1- crear nota
            2- mostrar tus notas
            3- eliminar nota
            4- salir 

            """))
            if opcion >= 1 and opcion <= 4:
                break
            else:
                print("escribe un numero entre 1 y 4")
                sleep(1)
        except ValueError:
            print("introduce un numero por favor")
            sleep(2)
    return opcion


def inicio_asistente():
    opcion = menu()
