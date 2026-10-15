from collections import deque
 
cola = deque()
 
def registrar_paciente():
    nombre = input("\nIngresa el nombre del paciente: ")
    cola.append(nombre)
    print(f"\nRegistrado: {nombre}")
 
def atender_paciente():
    if not cola:
        print("\nNo hay pacientes en espera")
    else:
        paciente = cola.popleft()
        print(f"\nAtendiendo a: {paciente}")
 
def mostrar_cola():
    if not cola:
        print("\nLa cola está vacía")
    else:
        print("\nPacientes en espera:")
        for posicion, paciente in enumerate(cola, 1):
            print(f"{posicion}. {paciente}")

def salir():
    print("Saliendo del sistema...")
    

while True:
    print()
    print("Menu")
    print("1.Registrar paciente")
    print("2.Paciente en curso")
    print("3.Pacientes en espera")
    print("4.Salir")

    opción = input("\nSelecciona una opción: ")
    if opción == "1":
        registrar_paciente()
    elif opción == "2":
        atender_paciente()
    elif opción == "3":
        mostrar_cola()
    elif opción == "4":
        salir()
        break