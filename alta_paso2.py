
class Catalogo: 
    recetas = []

""" Agregar recetas """
def agregar_receta(self, id, nombre, descripcion, imagen, ingredientes, procedimiento): 
    if self.consultar_receta(id): 
        return False 
    
    nueva_receta = { 
        'id': id, 
        'nombre': nombre,
        'descripcion': descripcion, 
        'imagen': imagen, 
        'ingredientes': ingredientes, 
        'procedimiento': procedimiento
        } 
    self.recetas.append(nueva_receta) 
    return True


""" Consultar receta """
def consultar_receta(self, id): 
    for receta in self.recetas: 
        if receta['id'] == id: 
            return receta 
    return False


""" Modificar receta """
def modificar_receta(self, id,nuevo_nombre, nueva_descripcion, nueva_imagen, nuevo_ingredientes, nuevo_procedimiento):

    for receta in self.recetas: 
        if receta['id'] == id: 
            receta['nombre'] =nuevo_nombre
            receta['descripcion'] = nueva_descripcion 
            receta['imagen'] = nueva_imagen 
            receta['ingredientes'] = nuevo_ingredientes
            receta['procedimiento'] = nuevo_procedimiento 
            return True 
    return False


""" Listar recetas """
def listar_receta(self): 
    print("-" * 50) 
    
    for receta in self.recetas: 
        print(f"Id............: {receta['id']}") 
        print(f"Nombre........: {receta['nombre']}")
        print(f"Descripción...: {receta['descripcion']}") 
        print(f"Imagen........: {receta['imagen']}") 
        print(f"Ingredientes..: {receta['ingredientes']}") 
        print(f"Procedimiento.: {receta['procedimiento']}") 
        print("-" * 50)


""" Eliminar receta """
def eliminar_receta(self, id): 
    for receta in self.recetas: 
        if receta['id'] == id:
            self.recetas.remove(receta) 
            return True 
    return False


""" Mostrar recetas """
def mostrar_receta(self, id): 
    receta = self.consultar_receta(id) 
    if receta:
        print("-" * 50) 
        print(f"Id...............: {receta['id']}") 
        print(f"Nombre...........: {receta['nombre']}") 
        print(f"Descripción......: {receta['descripcion']}") 
        print(f"Imagen...........: {receta['imagen']}")
        print(f"Ingredientes.....: {receta['ingredientes']}") 
        print(f"Procedimiento....: {receta['procedimiento']}") 
        print("-" * 50) 
    else: 
        print("Receta no encontrada.")


catalogo = Catalogo()

catalogo.agregar_receta(2, 'torta frita', 'Receta argentina con pocos ingredientes y muy fácil de hacer', 'images.jpg', '600 grs. de Harina 000 - 1 Cucharada de Sal fina, 50 grs. de manteca o grasa vacuna - 300 cc. de agua tibia - 100 grs. de azúcar para espolvorear - 1 litro de aceite para freir', 'Tamizamos la harina con la sal e incorporamos la manteca y el agua tibia - Formamos una masa y dejamos reposar media hora - Estiramos la masa y cortamos las tortas - Colocamos el aceite en la cacerola, tapamos y calentamos a fuego fuerte - Una vez caliente el aceite, colocamos las tortas, tapamos y cocinamos a fuego fuerte hasta finalizar la cocción - Servimos espolvoreadas con azúcar')
catalogo.mostrar_receta(2)