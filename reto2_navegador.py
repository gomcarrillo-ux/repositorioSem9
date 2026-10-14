historial = []

def registrar():
    url = input("ingresa tu url pofavo:" )
    historial.append(url)

def regresar():
    if not historial:
        print("No hay un camino que lleve de regreso D:")
        return
    pagAnt = historial.pop()
    print(f"Regresando a la pagina anterior... {pagAnt}")

def consultar():
    if not historial:
        print("No hay nada pa' consultar mae njds xd")
    else:
        print(historial[-1])

def mostrar():
    print(historial)

def salir():
    print("NOS VEMOOOOOS")

while True:
    print()
    print("Menu diaverga")
    print("1.Registra una página")
    print("2.Regresa a tu pagina anterior")
    print("3.Consulta tu pagina actual")
    print("4.Mostrar historial")
    print("5.Salir")

    opción = input("\nSelecciona una opción: ")
    if opción == "1":
        registrar()
    elif opción == "2":
        regresar()
    elif opción == "3":
        consultar()
    elif opción == "4":
        mostrar()
    elif opción == "5":
        salir()
        break