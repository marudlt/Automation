from Calculadora.utils import pedir_numero, pedir_opcion
from Calculadora.operaciones import sumar, restar, multiplicar, dividir


while True:
    opcion = pedir_opcion()

    a = pedir_numero("Ingresar un número entero: ")
    b = pedir_numero("Ingresar un número entero: ")

    match opcion:
        case "1":
            print("Resultado:", sumar(a, b))
        case "2":
            print("Resultado:", restar(a, b))
        case "3":
            print("Resultado:", multiplicar(a, b))
        case "4":
            print("Resultado:", dividir(a, b))
        case _:
            print("Opción incorrecta")

    otra = input("¿Querés hacer otra operación? (s/n): ")

    if otra != "s":
        print("Hasta la próxima!!!!!")
        break