import notas.nota as modelo
class Acciones:

    def crear(self, usuario):
        print(f"Ok {usuario[1]}")
        titulo = input("Titulo de la nota: ")
        descripcion = input("Contenido de la nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar

        if guardar[0] >= 1:
            print(f"\nLa nota {titulo} se a guardado")
        else:
            print(f"\nNo se ha guardado la nota {titulo}")