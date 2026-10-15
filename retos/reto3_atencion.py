from collections import deque
cola = deque()

def registro():
    nombre = input("\nIngrese el nombre del cliente: ")
    if not nombre.strip:
        print("No se acepta eso")
    turno = input(f"\nIngrese el turno para {nombre}: ")
    cola.append((nombre,turno))

def atender():
    if not cola:
        print("\nNo hay clientes por atender... ")
    else:
        nombre,turno = cola.popleft()
        print(f"\n{nombre} esta siendo atendido! ")

def consultar():
    if not cola:
        print("\nNo hay nada que concultar... ")
    else:
        print(f"\nEl proximo cliente es: {cola[0][0]}!")

def mostrar():
    if not cola:
        print("\nNo hay clientes esperando...")
    else:
        print(f"\nLos clientes esperando son: ")
        for cliente in cola:
            print(cliente[0])

def cantidad():
    print(f"\nTienes {len(cola)} pendientes")

def salir():
    print("Saliendo del sistema...")

while True:
    print()
    print("Menu")
    print("1.Registrar nuevo cliente")
    print("2.Atender cliente")
    print("3.Consultar proximo cliente")
    print("4.Mostrar los clientes pendientes")
    print("5.Cantidad de pendientes")
    print("6.Salir")

    opción = input("\nElige una opción: ")
    if opción == "1":
        registro()
    elif opción == "2":
        atender()
    elif opción == "3":
        consultar()
    elif opción == "4":
        mostrar()
    elif opción == "5":
        cantidad()
    elif opción == "6":
        salir()
        break