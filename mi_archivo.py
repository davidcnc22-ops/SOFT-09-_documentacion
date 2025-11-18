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

# ...existing code...

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
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.\n")

if __name__ == "__main__":
    menu()


