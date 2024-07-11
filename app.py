#------------------------------------------------
# Instalar con pip install Flask
from flask import Flask, request, jsonify

# Instalar con pip install flask-cors
from flask_cors import CORS 

# Instalar con pip install mysql-connector-python
import mysql.connector

# Si es necesario, pip install Werkzeug
from werkzeug.utils import secure_filename 

# No es necesario instalar, es parte del sistema standard de Python
import os
import time
""" import datosconexion as bd """
#------------------------------

app = Flask(__name__)
CORS(app)

class Catalogo:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()
        
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS recetas ( 
            codigo INT AUTO_INCREMENT PRIMARY KEY, 
            nombre VARCHAR(255)NOT NULL,
            imagen_url VARCHAR(255),
            descripcion VARCHAR(255) NOT NULL, 
            ingredientes VARCHAR(700) NOT NULL, 
            procedimiento VARCHAR(900))''')
        self.conn.commit()
        
        
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)

    def listar_recetas(self):
        self.cursor.execute("SELECT * FROM recetas")
        recetas = self.cursor.fetchall()
        return recetas
    
    def consultar_receta(self, codigo):
        
        self.cursor.execute(f"SELECT * FROM recetas WHERE codigo = {codigo}")
        return self.cursor.fetchone()

    def mostrar_receta(self, codigo):
        
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
            print("Receta no encontrado.")

    def agregar_receta(self, nombre,  descripcion, imagen, ingredientes, procedimiento): 
        sql = "INSERT INTO recetas (nombre, descripcion, imagen_url, ingredientes, procedimiento) VALUES (%s, %s, %s, %s, %s)" 
        valores = (nombre, descripcion, imagen, ingredientes, procedimiento)

        self.cursor.execute(sql,valores)
        self.conn.commit()
        return self.cursor.lastrowid

    def modificar_receta(self, codigo, nuevo_nombre, nueva_descripcion, nueva_imagen, nuevos_ingredientes, nuevo_procedimiento):
        sql = "UPDATE recetas SET nombre = %s, descripcion = %s, imagen_url = %s, ingredientes = %s, procedimiento = %s, WHERE codigo = %s" 
        valores = (nuevo_nombre, nueva_descripcion, nueva_imagen, nuevos_ingredientes, nuevo_procedimiento, codigo)

        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def eliminar_receta(self, codigo): # Eliminar un producto de la tabla a partir de su código     
        self.cursor.execute(f"DELETE FROM recetas WHERE codigo = {codigo}") 
        self.conn.commit() 
        return self.cursor.rowcount > 0

#--------------------------------------------------------------------
# Cuerpo del programa
#--------------------------------------------------------------------
# Crear una instancia de la clase Catalogo

catalogo = Catalogo(host="localhost", user="root", password="", database="normi") 
# las variables con los datos de la conexion estan guardadas en el archivo datosconexion.py


# Carpeta para guardar las imagenes
ruta_destino = 'Tp full stack 2/img' # Reemplazar por los datos de Pythonanywhere

#ruta_destino = '/home/normi/mysite/static/imagenes/'

@app.route("/recetas", methods=["GET"])
def listar_recetas():
    recetas = catalogo.listar_recetas()
    return jsonify(recetas)

@app.route("/recetas/<int:codigo>", methods=["GET"])
def mostrar_receta(codigo):
    receta = catalogo.consultar_receta(codigo)
    if receta:
        return jsonify(receta)
    else:
        return "Receta no encontrada", 404

@app.route("/recetas", methods=["POST"])
def agregar_receta():
    #Recojo los datos del form
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    imagen = request.files['imagen']
    ingredientes = request.form['ingredientes']
    procedimiento = request.form['procedimiento']
    nombre_imagen = ""  

    # Genero el nombre de la imagen
    nombre_imagen = secure_filename(imagen.filename) 
    nombre_base, extension = os.path.splitext(nombre_imagen) 
    nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}" 

    nuevo_codigo = catalogo.agregar_receta(nombre, descripcion, nombre_imagen, ingredientes, procedimiento)
    if nuevo_codigo:    
        imagen.save(os.path.join(ruta_destino, nombre_imagen))
        return jsonify({"mensaje": "Receta agregada correctamente.", "codigo": nuevo_codigo, "imagen": nombre_imagen}), 201
    else:
        return jsonify({"mensaje": "Error al agregar la receta."}), 500

@app.route("/recetas/<int:codigo>", methods=["PUT"])
def modificar_receta(codigo):
    #Se recuperan los nuevos datos del formulario
    nuevo_nombre = request.form.get("nombre")
    nueva_descripcion = request.form.get("descripcion")
    nuevos_ingredientes = request.form.get("ingredientes")
    nuevo_procedimiento = request.form.get("procedimiento")
    
    # Verifica si se proporcionó una nueva imagen
    if 'imagen' in request.files:
        imagen = request.files['imagen']
        # Procesamiento de la imagen
        nombre_imagen = secure_filename(imagen.filename) 
        nombre_base, extension = os.path.splitext(nombre_imagen) 
        nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}" 

        # Guardar la imagen en el servidor
        imagen.save(os.path.join(ruta_destino, nombre_imagen))
        
        # Busco el producto guardado
        receta = catalogo.consultar_receta(codigo)
        if receta: # Si existe el producto...
            imagen_vieja = receta["imagen_url"]
            # Armo la ruta a la imagen
            ruta_imagen = os.path.join(ruta_destino, imagen_vieja)

            # Y si existe la borro.
            if os.path.exists(ruta_imagen):
                os.remove(ruta_imagen)
    else:     
        receta = catalogo.consultar_receta(codigo)
        if receta:
            nombre_imagen = receta["imagen_url"]

# Se llama al método modificar_producto pasando el codigo del producto y los nuevos datos.
    if catalogo.modificar_receta(codigo, nuevo_nombre, nueva_descripcion, nombre_imagen,nuevos_ingredientes, nuevo_procedimiento):
        return jsonify({"mensaje": "Receta modificada"}), 200
    else:
        return jsonify({"mensaje": "Receta no encontrada"}), 403

@app.route("/recetas/<int:codigo>", methods=["DELETE"])
def eliminar_receta(codigo):
    # Primero, obtiene la información del producto para encontrar la imagen
    receta = catalogo.consultar_receta(codigo)
    if receta:
        # Eliminar la imagen asociada si existe
        ruta_imagen = os.path.join(ruta_destino, receta['imagen_url'])
        if os.path.exists(ruta_imagen):
            os.remove(ruta_imagen)

        # Luego, elimina el producto del catálogo
        if catalogo.eliminar_receta(codigo):
            return jsonify({"mensaje": "Receta eliminada"}), 200
        else:
            return jsonify({"mensaje": "Error al eliminar la receta"}), 500
    else:
        return jsonify({"mensaje": "Receta no encontrada"}), 404


if __name__ == "__main__":
    app.run(debug=True)