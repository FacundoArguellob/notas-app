from tools import clean_screen
from usuarios import acciones
import notas.asistente_notas as asistente_notas
from time import sleep

hazEl = acciones.Acciones()

sleep_time = 2
def menu():
    clean_screen()
    opcion = input("""
        Acciones disponibles:
        Elige una de las opciones con numeros
            -1 Registro
            -2 Login
            -3 Salida
        """)
    while opcion != "1" and opcion != "2" and opcion != "3":
            clean_screen()
            print("Introduce un numero correcto!")
            sleep(sleep_time)
    return opcion

def inicio_asistente():
    while True:
        opcion = menu()
        if opcion == "1":
            hazEl.registro()
            kill = any
        elif opcion == "2":
            login = hazEl.login()
            kill = any
            break
        elif opcion == "3":
            print("Hasta luego!")
            kill = True
            login = any
            break
    return login, kill

def main():
    login, kill = inicio_asistente()
    if kill:
        asistente_notas.inicio_asistente(login)
main()