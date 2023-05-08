import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Nota:

    def __init__(self, usuario_id, titulo, descripcion):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"
        nota = (self.usuario_id, self.titulo, self.descripcion)
        cursor.execute(sql, nota)
        database.commit()

        return cursor.rowcount, self
    
    def mostrar_notas(self, usuario):
        sql = f"SELECT * FROM notas WHERE usuario_id = {usuario[0]}"
        cursor.execute(sql)
        listas = cursor.fetchall()
        return listas
    
    def eliminar_nota(id_borrar):
        sql = "DELETE FROM notas WHERE id = %s"
        cursor.execute(sql, (id_borrar,))
        database.commit()