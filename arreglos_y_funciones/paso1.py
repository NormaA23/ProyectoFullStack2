################################################################
# Parte 1
################################################################


recetas = []

#   Agregar recetas
def agregar_receta(codigo, nombre, descripcion, imagen, ingredientes, procedimiento):     
    if consultar_receta(codigo): 
        return False
    nueva_receta = { 
        'codigo': codigo, 
        'nombre': nombre,
        'descripcion': descripcion, 
        'imagen': imagen, 
        'ingredientes': ingredientes, 
        'procedimiento': procedimiento
        } 
    recetas.append(nueva_receta) 
    return True


#   Consultar receta 
def consultar_receta(codigo): 
    for receta in recetas: 
        if receta['codigo'] == codigo:
            return receta 
    return False


#   Modificar receta
def modificar_receta(codigo, nuevo_nombre, nueva_descripcion, nueva_imagen, nuevos_ingredientes, nuevo_procedimiento): 
    for receta in recetas: 
        if receta['codigo'] == codigo: 
            receta['nombre'] = nuevo_nombre
            receta['descripcion'] = nueva_descripcion
            receta['imagen'] = nueva_imagen 
            receta['ingredientes'] = nuevos_ingredientes
            recetas['procedimiento'] = nuevo_procedimiento
            return True 
    return False


#   Listar recetas 
def listar_recetas(): 
    print("-" * 50)
    for receta in recetas: 
        print(f"Código........: {receta['codigo']}") 
        print(f"Nombre........: {receta['nombre']}")
        print(f"Descripcion...: {receta['descripcion']}") 
        print(f"Imagen........: {receta['imagen']}") 
        print(f"Ingredientes..: {receta['ingredientes']}")
        print(f"Procedimiento.: {receta['procedimiento']}") 
        print("-" * 50)


#   Eliminar receta 
def eliminar_receta(codigo): 
    for receta in recetas: 
        if receta['codigo'] == codigo:
            recetas.remove(receta)
            return True
        return False
    

agregar_receta(3, 'torta frita', 'Receta argentina con pocos ingredientes y muy fácil de hacer', 'images.jpg', '600 grs. de Harina 000 - 1 Cucharada de Sal fina, 50 grs. de manteca o grasa vacuna - 300 cc. de agua tibia - 100 grs. de azúcar para espolvorear - 1 litro de aceite para freir', 'Tamizamos la harina con la sal e incorporamos la manteca y el agua tibia - Formamos una masa y dejamos reposar media hora - Estiramos la masa y cortamos las tortas - Colocamos el aceite en la cacerola, tapamos y calentamos a fuego fuerte - Una vez caliente el aceite, colocamos las tortas, tapamos y cocinamos a fuego fuerte hasta finalizar la cocción - Servimos espolvoreadas con azúcar')

consultar_receta(3) 
""" modificar_receta(1, 'torta frita', 'Receta argentina con pocos ingredientes y muy fácil de hacer', 'images.jpg', '600 grs. de Harina 000 - 1 Cucharada de Sal fina, 50 grs. de manteca o grasa vacuna - 300 cc. de agua tibia - 100 grs. de azúcar para espolvorear - 1 litro de aceite para freir', 'Tamizamos la harina con la sal e incorporamos la manteca y el agua tibia - Formamos una masa y dejamos reposar media hora - Estiramos la masa y cortamos las tortas - Colocamos el aceite en la cacerola, tapamos y calentamos a fuego fuerte - Una vez caliente el aceite, colocamos las tortas, tapamos y cocinamos a fuego fuerte hasta finalizar la cocción - Servimos espolvoreadas con azúcar') 
listar_recetas() 
consultar_receta(1) """   
""" eliminar_receta(1) """
consultar_receta(1)




