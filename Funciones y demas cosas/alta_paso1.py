
recetas = []


""" Agregar recetas"""
def agregar_receta(id, nombre, descripcion, imagen, ingredientes, procedimiento):     
    if consultar_receta(id): 
        return False
     
    nueva_receta = { 
        'id': id, 
        'nombre': nombre,
        'descripcion': descripcion, 
        'imagen': imagen, 
        'ingredientes': ingredientes, 
        'procedimiento': procedimiento
        } 
    
    recetas.append(nueva_receta) 
    return True


""" Consultar receta """
def consultar_receta(id): 
    for receta in recetas: 
        if receta['id'] == id:
            return receta 
    return False


""" Modificar receta """
def modificar_receta(id, nuevo_nombre, nueva_descripcion,nueva_imagen, nuevo_ingredientes, nuevo_procedimiento): 
    for receta in recetas: 
        if receta['id'] == id: 
            receta['nombre'] = nuevo_nombre
            receta['descripcion'] = nueva_descripcion
            receta['imagen'] = nueva_imagen 
            receta['ingredientes'] = nuevo_ingredientes
            recetas['procedimiento'] = nuevo_procedimiento
            return True 
    return False


""" Listar recetas """
def listar_recetas(): 
    print("-" * 50)
    for receta in recetas: 
        print(f"Id............: {receta['id']}") 
        print(f"Nombre........: {receta['nombre']}")
        print(f"Descripcion...: {receta['descripcion']}") 
        print(f"Imagen........: {receta['imagen']}") 
        print(f"Ingredientes..: {receta['ingredientes']}")
        print(f"Procedimiento.: {receta['procedimiento']}") 
        print("-" * 50)


""" Eliminar receta """
def eliminar_receta(id): 
    for receta in recetas: 
        if receta['id'] == id:
            recetas.remove(receta)