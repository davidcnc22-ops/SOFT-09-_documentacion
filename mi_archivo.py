"Hola Mundo" 

def saludar ():
    return saludar 

print ("Hola, . ¡Bienvenida al ejercicio de Git y GitHub!")


import random

# Lista de diccionarios que almacena los celulares en memoria
celulares = []
modificado = False  # Variable global para saber si hubo cambios

def cargar_informacion(nombre_archivo):
    global celulares, modificado
    try:
        with open(nombre_archivo, "r") as archivo:
            celulares = []
            for linea in archivo:
                id_cel, marca, modelo, precio, stock = linea.strip().split(",") #.split(",") separar por comas
                celulares.append({      #.append agregar a la lista
                    "id": int(id_cel),
                    "marca": marca,
                    "modelo": modelo,
                    "precio": float(precio),
                    "stock": int(stock)
                })
        print("Información cargada correctamente.\n")
        modificado = False
    except FileNotFoundError:
        print("El archivo no existe. Se creará uno al guardar.\n")


def mostrar_celulares():
    if not celulares:
        print("No hay celulares cargados.\n")
        return
    for cel in celulares:
        print(cel)
    print()


def existe_celular(marca, modelo):
    for cel in celulares:
        if cel["marca"].lower() == marca.lower() and cel["modelo"].lower() == modelo.lower():   #.lower() para ignorar mayúsculas/minúsculas
            return True
    return False


def agregar_stock():
    global modificado

    marca = input("Marca: ").strip() #.strip() para eliminar espacios en blanco
    modelo = input("Modelo: ").strip()

    if existe_celular(marca, modelo):
        print("Ya existe un celular con esa marca y modelo.\n")
        return

    try:
        precio = float(input("Precio: "))
        if precio < 0:
            print("El precio no puede ser negativo.\n")
            return

        cantidad = int(input("Cantidad a agregar: "))
        if cantidad < 0:
            print("El stock no puede ser negativo.\n")
            return
    except ValueError:
        print("Entrada inválida.\n")
        return

    nuevo = {
        "id": random.randint(1, 5000),         #.randint para generar un ID aleatorio
        "marca": marca,
        "modelo": modelo,
        "precio": precio,
        "stock": cantidad
    }

    celulares.append(nuevo)     #.append para agregar a la lista
    modificado = True   # Indicar que hubo cambios
    print("Celular agregado correctamente.\n")


def cambiar_precio():
    global modificado   #global para modificar la variable fuera de la función
    marca = input("Ingrese la marca a modificar precio: ").strip()

    for cel in celulares:
        if cel["marca"].lower() == marca.lower():
            try:
                nuevo_precio = float(input("Nuevo precio: "))
                if nuevo_precio < 0:
                    print("El precio no puede ser negativo.\n")
                    return
            except ValueError:
                print("Entrada inválida.\n")
                return

            cel["precio"] = nuevo_precio
            modificado = True #booleano o bandera para indicar que hubo cambios
            print("Precio actualizado.\n")
            return

    print("No se encontró la marca.\n")


def cambiar_stock():
    global modificado
    try:
        id_buscar = int(input("ID del celular: "))
    except ValueError:
        print("Entrada inválida.\n")
        return

    for cel in celulares:
        if cel["id"] == id_buscar:
            try:
                nuevo_stock = int(input("Nuevo stock: "))
                if nuevo_stock < 0:
                    print("El stock no puede ser negativo.\n")
                    return
            except ValueError:
                print("Entrada inválida.\n")
                return

            cel["stock"] = nuevo_stock
            modificado = True
            print("Stock actualizado.\n")
            return

    print("No se encontró el ID.\n")


def buscar_por_marca():
    marca = input("Marca a buscar: ").strip()
    encontrados = [cel for cel in celulares if cel["marca"].lower() == marca.lower()]

    if encontrados:
        for cel in encontrados:
            print(cel)
        print()
    else:
        print("No se encontraron celulares con esa marca.\n")


def vender():
    global modificado
    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()

    for cel in celulares:
        if cel["marca"].lower() == marca.lower() and cel["modelo"].lower() == modelo.lower():

            try:
                cantidad = int(input("Cantidad a vender: "))
                if cantidad <= 0:
                    print("Cantidad inválida.\n")
                    return
            except ValueError:
                print("Entrada inválida.\n")
                return

            if cantidad > cel["stock"]:
                print("No hay suficiente stock.\n")
                return

            cel["stock"] -= cantidad        #-= para restar de la variable
            modificado = True
            print("Venta realizada.\n")
            return

    print("No se encontró ese celular.\n")


#MENU
def menu():
    archivo = "celulares.txt"

    while True:     #Bucle infinito hasta que el usuario decida salir
        print("===== SISTEMA DE CELULARES =====")
        print("1. Cargar información")
        print("2. Agregar stock")
        print("3. Cambiar precio")
        print("4. Cambiar stock")
        print("5. Buscar por marca")
        print("6. Vender")
        print("7. Listar celulares")
        print("8. Salir")
        opcion = input("Elija una opción: ")

        # Procesar la opción
        if opcion == "1":
            cargar_informacion(archivo)
        elif opcion == "2":
            agregar_stock()
        elif opcion == "3":
            cambiar_precio()
        elif opcion == "4":
            cambiar_stock()
        elif opcion == "5":
            buscar_por_marca()
        elif opcion == "6":
            vender()
        elif opcion == "7":
            mostrar_celulares()
            modificado = False
        else:
            print("Opción inválida.\n")

menu()



