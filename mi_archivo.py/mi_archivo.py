def main():
    print("¡Hola, mundo desde Python!")
    saludar("David")
    sumar(5, 3)

def saludar(nombre):
    print(f"Hola, {nombre}. ¡Bienvenida al ejercicio de Git y GitHub!")

def sumar(a, b):
    resultado = a + b
    print(f"La suma de {a} + {b} es: {resultado}")

if __name__ == "__main__":
    main()