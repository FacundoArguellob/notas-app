from  os import system
from time import sleep
from notas import acciones
from usuarios import acciones as usuario
#import usuarios.clases_usuario as usuario

def menu():
    while True:
        try:
            system("clear")
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


def eleccion(opcion, login):
    if opcion == 1:
        acciones.Acciones.crear(any, login)
        sleep(1)
        inicio_asistente()
    if opcion == 2:
        print("2")
        sleep(1)
        inicio_asistente()
    if opcion == 3:
        print("3")
        sleep(1)
        inicio_asistente()
    if opcion == 4:
        print("4")

def inicio_asistente(login):
    opcion = menu()
    eleccion(opcion, login)
