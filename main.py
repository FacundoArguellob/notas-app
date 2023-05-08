from tools import clean_screen
from usuarios import acciones
import notas.asistente_notas as asistente_notas

hazEl = acciones.Acciones()


def eleccion_user():
    clean_screen()
    opcion = input("""
        Acciones disponibles:
        Elige una de las opciones con numeros
            -1 Registro
            -2 Login
        """)
    return opcion


def inicio_asistente():
    loginOk = false
    while !loginOk:
        opcion = eleccion_user()
        while opcion != "1" or opcion != "2":
            opcion = eleccion_user()
        if opcion == "1":
            hazEl.registro()
        else:
            login = hazEl.login()
            loginOk = true
    return login

def main():
    login = inicio_asistente()
    asistente_notas.inicio_asistente(login)
main()


#facuarg49@gmail.com
#valeagus111
