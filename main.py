from tools import clean_screen
from usuarios import acciones


hazEl = acciones.Acciones()

def inicio_asistente():
    clean_screen()
    opcion = input("""
        Acciones disponibles:
        Elige una de las opciones con numeros
            -1 Registro
            -2 Login
        """)
    while opcion != "1" and opcion != "2":
        clean_screen()
        opcion = input("""
        Acciones disponibles:
        Elige una de las opciones con numeros
            -1 Registro
            -2 Login
        """)

    if opcion == "1":
        hazEl.registro()
    elif opcion == "2":
        hazEl.login()












def main():
    inicio_asistente()
main()