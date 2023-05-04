import mysql.connector
from datetime import date

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="proyect_python",
    port=3306,
)

cursor = database.cursor(buffered=True)

class Usuario:

    fecha = date.today()
    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password

    def registro(self):
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellido, self.email, self.password, self.fecha)
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount,self]
        except:
            result = [0, self]
            
        return result
    
    def login(self):
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        cursor.execute(sql,(self.email, self.password))
        resultado = cursor.fetchall()
        return resultado