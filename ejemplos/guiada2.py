acciones = []
 
def registrar_accion():
    descripcion = input("Describe la acción a realizar ")
    acciones.append(descripcion)
    print("Acción registrada:", descripcion)
 
def deshacer():
    if not acciones:
        print("No existen acciones para deshacer")
        return
    ultima = acciones.pop()
    print("Se deshizo:", ultima)
 
def historial():
    print("Acciones pendientes:", acciones)

def salir():
    print("HE APRENDIDO!")
    
while True:
    print()
    print("Menu")
    print("1.Registrar Acción")
    print("2.Deshacer")
    print("3.Ver historial")
    print("4.Salir")
    
    opción = (input("Selecciona una opción: "))
    if opción == "1":
        registrar_accion()
    elif opción == "2":
        deshacer()
    elif opción == "3":
        historial()
    elif opción == "4":
        salir()
        break