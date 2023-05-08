import notas.nota as modelo
from tools import clean_screen
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
        
        listas = modelo.Nota.mostrar_notas(any, usuario)
        print("---NOTAS---")
        for lista in listas:
            print(f"""
            Titulo: {lista[2]}
            Nr: {lista[0]}\n
            Contenido: {lista[3]}
            \n
            """)
        siguiente = input("enter para continuar")

    def borrar_nota(self, usuario):
        listas = modelo.Nota.mostrar_notas(any, usuario)
        clean_screen()
        print("Elige el id de la nota que quieres borrar")
        lista_id = []
        print("---NOTAS---")
        contador = 0
        for lista in listas:
            print(f"""
            Titulo: {lista[2]}
            ID: {contador}\n
            """)
            contador += 1
            lista_id.append(lista)
        while True:
            try:
                id_borrar = int(input("ID: "))
                if id_borrar in lista_id:
                    modelo.Nota.eliminar_nota(id_borrar)
                    break
                else:
                    print("ese id esta fuera de rango o no existe, intenta nuevamente")
                    
            except ValueError:
                print("ingresa un numero por favor ")