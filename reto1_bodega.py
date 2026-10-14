bodega = []

def apilar():
    caja = int(input("Dime el codigo de la caja que deseas apilar? "))
    if caja not in bodega:
        bodega.append(caja)
        print("Su caja ha sido apilada exitosamente!")
    else:
        print("Este codigo ya esta guardado ")

def desapilar():
    if not bodega:
        print("La bodega esta vacía, no hay nada que retirar")
    else:
        bodega.pop()
        print("Su caja ha sido retirada " )

def consultar_tope():
    if not bodega:
        print("La bodega esta vacía")
    else:
        print (bodega[-1])

def mostrar_pila():
    if not bodega:
        print("La bodega esta vacía")
    else:
        for caja in bodega:
            print (caja)

def salir():
    print("¡Hasta luego! cuidate ¡mucho!")

while True:
    print()
    print("Menu")
    print("1.Apilar")
    print("2.Desapilar")
    print("3.Consultar tope")
    print("4.Mostrar pila")
    print("5.Salir")
    opción = input(f"\nElige una opción: ")
    if opción == "1":
        apilar()
    elif opción == "2":
        desapilar()
    elif opción == "3":
        consultar_tope()
    elif opción == "4":
        mostrar_pila()
    elif opción == "5":
        salir()
        break
