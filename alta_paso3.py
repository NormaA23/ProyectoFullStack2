
import mysql.connector 
class Catalogo: 
    def __init__(self, host, user, password, database): 

        self.conn = mysql.connector.connect(
            host=host, 
            user=user, 
            password=password, 
            database=database
        )

        self.cursor = self.conn.cursor(dictionary=True) 

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS recetas ( 
        id INT AUTO_INCREMENT PRIMARY KEY, 
        nombre VARCHAR(255)NOT NULL,
        imagen_url VARCHAR(255),
        descripcion VARCHAR(255) NOT NULL, 
        ingredientes VARCHAR(700) NOT NULL, 
        procedimiento VARCHAR(900) NOT NULL,
        )''')

        self.conn.commit()

    def agregar_receta(self, id, nombre,  descripcion, imagen, ingredientes, procedimiento): 
        sql = "INSERT INTO recetas (id, nombre, descripcion, imagen_url, ingredientes, procedimiento) VALUES (%s, %s, %s, %s, %s,%s)" 
        valores = (id, nombre, descripcion,imagen, ingredientes, procedimiento) 

        self.cursor.execute(sql, valores) 
        self.conn.commit() 
        return self.cursor.lastrowid
    
    def consultar_receta(self, id): # Consultamos un producto a partir de su código 
        self.cursor.execute(f"SELECT * FROM recetas WHERE id = {id}") 
        return self.cursor.fetchone() #solo trae uno con el fetchone
    
    
    def modificar_receta(self, nuevo_id, nuevo_nombre, nueva_descripcion, nueva_imagen,nuevos_ingredientes, nuevo_procedimiento):
        sql = "UPDATE recetas SET nombre = %s, descripcion = %s, imagen_url = %s, ingredientes = %s, procedimiento = %s, WHERE id = %s" 
        valores = (nuevo_nombre, nueva_descripcion, nueva_imagen, nuevos_ingredientes, nuevo_procedimiento,nuevo_id,) 

        self.cursor.execute(sql, valores) 
        self.conn.commit()
        return self.cursor.rowcount > 0
    

    def mostrar_receta(self, id): # Mostramos los datos de un producto a partir de su código 
        receta = self.consultar_receta(id) 
        if receta: 
            print("-" * 40)
            print(f"Id.............: {receta['id']}") 
            print(f"Nombre.........: {receta['nombre']}")
            print(f"Descripción....: {receta['descripcion']}") 
            print(f"Imagen.........: {receta['imagen_url']}") 
            print(f"Ingredientes...: {receta['ingredientes']}") 
            print(f"Procedimiento..: {receta['procedimiento']}") 
            print("-" * 40) 
        else: 
            print("Receta no encontrada.")


    def listar_recetas(self): 
        self.cursor.execute("SELECT * FROM recetas")
        recetas = self.cursor.fetchall() 
        return recetas
    
    
    def eliminar_receta(self, id): # Eliminamos un producto de la tabla a partir de su código     
        self.cursor.execute(f"DELETE FROM recetas WHERE id = {id}") 
        self.conn.commit() 
        return self.cursor.rowcount > 0
    
catalogo= Catalogo(host='localhost', user='root', password='', database='normi')