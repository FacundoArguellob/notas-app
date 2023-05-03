from tools import clean_screen

class Acciones:

    def registro(self):
        clean_screen()
        nombre = input("Introduce tu nombre: ")
        apellido = input("Introduce tu apellido: ")
        email = input("Introduce tu email: ")
        password = input("Crea una password: ")

    def login(self):
        clean_screen()
        email = input("Email: ")
        password = input("Password: ")
