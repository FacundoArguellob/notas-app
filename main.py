from tools import clean_screen
from usuarios import acciones


hazEl = acciones.Acciones()


def eleccion_user():
    opcion = input("""
        Acciones disponibles:
        Elige una de las opciones con numeros
            -1 Registro
            -2 Login
        """)
    return opcion


def inicio_asistente():
    clean_screen()
    opcion = eleccion_user()
    while opcion != "1" and opcion != "2":
        clean_screen()
        opcion = eleccion_user()

    if opcion == "1":
        hazEl.registro()
    elif opcion == "2":
        hazEl.login()


def main():
    inicio_asistente()
main()


#facuarg49@gmail.com
#valeagus111