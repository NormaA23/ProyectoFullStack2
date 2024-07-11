#########################################################################
# Parte 3
#########################################################################

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
            codigo INT AUTO_INCREMENT PRIMARY KEY, 
            nombre VARCHAR(255)NOT NULL,
            imagen_url VARCHAR(255),
            descripcion VARCHAR(255) NOT NULL, 
            ingredientes VARCHAR(700) NOT NULL, 
            procedimiento VARCHAR(900))''')
        self.conn.commit()

    def agregar_receta(self, nombre,  descripcion, imagen, ingredientes, procedimiento): 
        sql = "INSERT INTO recetas (nombre, descripcion, imagen_url, ingredientes, procedimiento) VALUES (%s, %s, %s, %s, %s)" 
        valores = (nombre, descripcion, imagen, ingredientes, procedimiento) 

        self.cursor.execute(sql, valores) 
        self.conn.commit() 
        return self.cursor.lastrowid

    def consultar_receta(self, codigo): # Consultamos un producto a partir de su código 
        self.cursor.execute(f"SELECT * FROM recetas WHERE codigo = {codigo}") 
        return self.cursor.fetchone() #solo trae uno con el fetchone

    def modificar_receta(self, codigo, nuevo_nombre, nueva_descripcion, nueva_imagen, nuevos_ingredientes, nuevo_procedimiento):
        sql = "UPDATE recetas SET nombre = %s, descripcion = %s, imagen_url = %s, ingredientes = %s, procedimiento = %s, WHERE codigo = %s" 
        valores = (nuevo_nombre, nueva_descripcion, nueva_imagen, nuevos_ingredientes, nuevo_procedimiento, codigo) 

        self.cursor.execute(sql, valores) 
        self.conn.commit()
        return self.cursor.rowcount > 0

    def mostrar_receta(self, codigo): # Mostramos los datos de un producto a partir de su código 
        receta = self.consultar_receta(codigo) 
        if receta: 
            print("-" * 40)
            print(f"Código.........: {receta['codigo']}") 
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

    def eliminar_receta(self, codigo): # Eliminar un producto de la tabla a partir de su código     
        self.cursor.execute(f"DELETE FROM recetas WHERE codigo = {codigo}") 
        self.conn.commit() 
        return self.cursor.rowcount > 0


catalogo = Catalogo(host="localhost", user="root", password="", database="normi") 
catalogo.agregar_receta('torta frita', 'Receta argentina con pocos ingredientes y muy fácil de hacer', 'images.jpg', '600 grs. de Harina 000 - 1 Cucharada de Sal fina, 50 grs. de manteca o grasa vacuna - 300 cc. de agua tibia - 100 grs. de azúcar para espolvorear - 1 litro de aceite para freir', 'Tamizamos la harina con la sal e incorporamos la manteca y el agua tibia - Formamos una masa y dejamos reposar media hora - Estiramos la masa y cortamos las tortas - Colocamos el aceite en la cacerola, tapamos y calentamos a fuego fuerte - Una vez caliente el aceite, colocamos las tortas, tapamos y cocinamos a fuego fuerte hasta finalizar la cocción - Servimos espolvoreadas con azúcar')