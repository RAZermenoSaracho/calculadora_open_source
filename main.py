from sumar import sumar
from restar import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def menu():
    while True:
        print("\nCalculadora Open Source")
        print("1. Sumar dos números")
        print("2. Restar dos números")
        print("3. Multiplicar dos números")
        print("4. Dividir dos números")
        print("5. Suma avanzada (N números)")
        print("6. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print(f"Resultado: {sumar(a, b)}")
        
        elif opcion == '2':
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print(f"Resultado: {restar(a, b)}")

        elif opcion == '3':
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print(f"Resultado: {multiplicar(a, b)}")

        elif opcion == '4':
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            try:
                print(f"Resultado: {dividir(a, b)}")
            except ZeroDivisionError:
                print("Error: No se puede dividir entre cero.")

        elif opcion == '5':
            n = int(input("¿Cuántos números vas a sumar? "))
            numeros = []
            for i in range(n):
                num = float(input(f"Ingresa el número {i+1}: "))
                numeros.append(num)
            print(f"Resultado: {suma_avanzada(numeros)}")

        elif opcion == '6':
            print("Gracias por usar la calculadora.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
