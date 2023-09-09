# Lista que contendrá los diccionarios de computadoras
computadoras = []

# Función para agregar una computadora al diccionario
def agregar_computadora():
    marca = input("Ingrese la marca de la computadora: ")
    modelo = input("Ingrese el modelo de la computadora: ")
    estado = input("Ingrese el estado de la computadora: ")
    tipo = input("Ingrese el tipo de la computadora: ")
    
    nueva_computadora = {
        'marca': marca,
        'modelo': modelo,
        'estado': estado,
        'tipo': tipo
    }
    
    computadoras.append(nueva_computadora)
    print("Se ha agregado la computadora al diccionario.")

# Función para buscar una computadora por marca y modelo
def buscar_computadora():
    marca = input("Ingrese la marca de la computadora a buscar: ")
    modelo = input("Ingrese el modelo de la computadora a buscar: ")
    
    for computadora in computadoras:
        if computadora['marca'] == marca and computadora['modelo'] == modelo:
            print("Información de la computadora encontrada:")
            print(f"Marca: {computadora['marca']}")
            print(f"Modelo: {computadora['modelo']}")
            print(f"Estado: {computadora['estado']}")
            print(f"Tipo: {computadora['tipo']}")
            return
    
    print("Computadora no encontrada.")

# Función para actualizar información de una computadora por marca y modelo
def actualizar_computadora():
    marca = input("Ingrese la marca de la computadora a actualizar: ")
    modelo = input("Ingrese el modelo de la computadora a actualizar: ")
    
    for computadora in computadoras:
        if computadora['marca'] == marca and computadora['modelo'] == modelo:
            print("Información actual de la computadora:")
            print(f"Marca: {computadora['marca']}")
            print(f"Modelo: {computadora['modelo']}")
            print(f"Estado: {computadora['estado']}")
            print(f"Tipo: {computadora['tipo']}")
            
            nueva_marca = input("Ingrese la nueva marca (o presione Enter para mantener la actual): ")
            nueva_modelo = input("Ingrese el nuevo modelo (o presione Enter para mantener el actual): ")
            nueva_estado = input("Ingrese el nuevo estado (o presione Enter para mantener el actual): ")
            nuevo_tipo = input("Ingrese el nuevo tipo (o presione Enter para mantener el actual): ")
            
            computadora['marca'] = nueva_marca if nueva_marca else computadora['marca']
            computadora['modelo'] = nueva_modelo if nueva_modelo else computadora['modelo']
            computadora['estado'] = nueva_estado if nueva_estado else computadora['estado']
            computadora['tipo'] = nuevo_tipo if nuevo_tipo else computadora['tipo']
            
            print("Información de la computadora actualizada.")
            return
    
    print("Computadora no encontrada.")

# Función para eliminar una computadora por marca y modelo
def eliminar_computadora():
    marca = input("Ingrese la marca de la computadora a eliminar: ")
    modelo = input("Ingrese el modelo de la computadora a eliminar: ")
    
    for computadora in computadoras:
        if computadora['marca'] == marca and computadora['modelo'] == modelo:
            computadoras.remove(computadora)
            print("Computadora eliminada del diccionario.")
            return
    
    print("Computadora no encontrada.")

# Menú principal
while True:
    print("\nDiccionario de Computadoras:")
    for idx, computadora in enumerate(computadoras, start=1):
        print(f"Computadora {idx}:")
        print(f"Marca: {computadora['marca']}")
        print(f"Modelo: {computadora['modelo']}")
        print(f"Estado: {computadora['estado']}")
        print(f"Tipo: {computadora['tipo']}")
        print()
    
    print("\nMenú:")
    print("1. Agregar computadora")
    print("2. Buscar computadora")
    print("3. Actualizar información de computadora")
    print("4. Eliminar computadora")
    print("5. Salir")
    
    opcion = input("Digite su opción: ")
    
    if opcion == '1':
        agregar_computadora()
    elif opcion == '2':
        buscar_computadora()
    elif opcion == '3':
        actualizar_computadora()
    elif opcion == '4':
        eliminar_computadora()
    elif opcion == '5':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida del menú.")
1