from datetime import date
import hashlib 
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]


class Usuario:

    fecha = date.today()
    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password

    def registro(self):

        #cifrado contrasenia
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellido, self.email, cifrado.hexdigest(), self.fecha)
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount,self]
        except:
            result = [0, self]

        return result
    
    def login(self):
        #consulta
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        
        #cifrado contrasenia
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        cursor.execute(sql,(self.email, cifrado.hexdigest()))
        resultado = cursor.fetchone()
        return resultado