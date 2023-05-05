from tools import clean_screen
import usuarios.clases_usuario as modelo
from time import sleep 


def check_login():
    clean_screen()
    email = input("Email: ")
    password = input("Password: ")
    #email = "facuarg49@gmail.com"
    #password = "valeagus111"
    check_login = modelo.Usuario(any, any, email, password)
    login = check_login.login()

    return login

class Acciones:

    def registro(self):
        clean_screen()
        nombre = input("Introduce tu nombre: ")
        apellido = input("Introduce tu apellido: ")
        email = input("Introduce tu email: ")
        password = input("Crea una password: ")

        usuario = modelo.Usuario(nombre, apellido, email, password)
        registro = usuario.registro()

        if registro[0] >= 1:
            print(f"Te haz registrado exitosamente {registro[1].nombre}")
        else:
            print("ERROR")

    def login(self):
        clean_screen()

        intentos = 0
        login = check_login()

        while not login and intentos != 3:
            intentos += 1
            print(f"Usuario incorrecto, Intenta nuevamente (intentos: {intentos})")
            sleep(2)
            login = check_login()  

        if login:
            print(f"Bienvenido/a {login[1]}")
            sleep(2)
        else:
            print("cantidad de intentos maxima")

        return login