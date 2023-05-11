import notas.nota as modelo
from tools import clean_screen
from time import sleep

test = 1
class Acciones:


    def crear(self, usuario):
        print(f"Ok {usuario[1]}, vamos a crear una nota")
        titulo = input("Titulo de la nota: ")
        descripcion = input("Contenido de la nota: ")
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()
        if guardar[0] >= 1:
            print(f"\nLa nota {titulo} se a guardado")
        else:
            print(f"\nNo se ha guardado la nota {titulo}")


    def mostrar(self, usuario):
        notas = modelo.Nota.mostrar_notas(any, usuario)
        if len(notas) == 0:
            print("No tienes notas")
            sleep(test)
        else:
            print("---NOTAS---")
            contador = 0
            for nota in notas:
                print(f"""
                Titulo: {nota[2]}
                Nr: {contador}\n
                Contenido: {nota[3]}
                \n
                """)
                contador += 1
            siguiente = input("enter para continuar")


    def borrar_eleccion(self, usuario, nota_id):
        #clean_screen()
        while True:
            try:
                resultado = int(input("""
                Funciones:
                    1- Borrar todas las notas
                    2- Borrar una nota
                    3- Volver al menu
                """))
            except ValueError:
                #clean_screen()
                print("Escribe un numero valido")
                sleep(test)
            if resultado == 1:
                modelo.Nota.eliminar_todo(usuario)
                #clean_screen()
                print("Se han eliminado todas las notas...")
                sleep(test)
                break
            elif resultado == 2:
                while True:
                    try:
                        id_borrar = int(input("ID: "))
                        if id_borrar >= 0 and id_borrar <= len(nota_id)-1:
                            id_nota = (nota_id[id_borrar])
                            modelo.Nota.eliminar_nota(id_nota[0])
                            print(f"La nota {id_nota[2]} se a eliminado correctamente")
                            break
                        else:
                            print("ese id esta fuera de rango o no existe, intenta nuevamente")    
                    except ValueError:
                            print("ingresa un numero por favor ")
            elif resultado == 3:
                break
            else:
                print("Numero incorrecto")


    def borrar_nota(self, usuario):
        notas = modelo.Nota.mostrar_notas(any, usuario)
        if len(notas) == 0:
            print("No tienes notas")
            sleep(test)
        else:
            #clean_screen()
            nota_id = []
            print("---NOTAS---")
            contador = 0
            for nota in notas:
                print(f"""
                Titulo: {nota[2]}
                ID: {contador}\n
                """)
                contador += 1
                nota_id.append(nota)
            Acciones.borrar_eleccion(any, usuario, nota_id)

