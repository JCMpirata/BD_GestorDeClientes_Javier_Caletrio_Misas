import database as db
import helpers as hlp


def iniciar():
    print("Bienvenido al gestor de clientes")
    print("1. Crear cliente")
    print("2. Editar cliente")
    print("3. Eliminar cliente")
    print("4. Listar clientes")
    print("5. Buscar cliente")
    print("6. Salir")
    print()

    opcion = input("Elija una opción: ")

    if opcion == "1":
        id = hlp.validar_id("Ingrese el ID del cliente: ")
        nombre = hlp.validar_texto("Ingrese el nombre del cliente: ").capitalize()
        apellido = hlp.validar_texto("Ingrese el apellido del cliente: ").capitalize()
        dni = None
        while True:
            dni = hlp.validar_dni("Ingrese el DNI del cliente: ").upper()
            if hlp.validar_dni(dni, db.Clientes.lista):
                break
        cliente = db.Clientes.crear(id, nombre, apellido, dni)
        print("Cliente creado con éxito")



    elif opcion == "2":
        cliente = db.Clientes.buscar(int(input("Ingrese el ID del cliente que desea editar: ")))
        if cliente:
            nombre = hlp.validar_texto("Ingrese el nombre del cliente: ").capitalize()
            apellido = hlp.validar_texto("Ingrese el apellido del cliente: ").capitalize()
            dni = None
            while True:
                dni = hlp.validar_dni("Ingrese el DNI del cliente: ").upper()
                if hlp.validar_dni(dni, db.Clientes.lista):
                    break
            cliente = db.Clientes.editar(cliente.id, nombre, apellido, dni)
            print("Cliente editado con éxito")
        else:
            print("Cliente no encontrado")



    elif opcion == "3":
        cliente = db.Clientes.buscar(int(input("Ingrese el ID del cliente que desea eliminar: ")))
        if cliente:
            db.Clientes.borrar(cliente.id)
            print("Cliente eliminado con éxito")
        else:
            print("Cliente no encontrado")


    elif opcion == "4":
        for cliente in db.Clientes.lista:
            print(f"ID: {cliente.id}")
            print(f"Nombre: {cliente.nombre}")
            print(f"Apellido: {cliente.apellido}")
            print(f"DNI: {cliente.dni}")
            print()


    elif opcion == "5":
        cliente = db.Clientes.buscar(int(input("Ingrese el ID del cliente que desea buscar: ")))
        if cliente:
            print(f"ID: {cliente.id}")
            print(f"Nombre: {cliente.nombre}")
            print(f"Apellido: {cliente.apellido}")
            print(f"DNI: {cliente.dni}")
        else:
            print("Cliente no encontrado")


    elif opcion == "6":
        print("Hasta luego")
    else:
        print("Opción no válida")
        iniciar()