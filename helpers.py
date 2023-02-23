import re
import os
import platform
import database as db


def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def validar_texto(texto):
    patron = r"^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+$"
    if re.match(patron, texto):
        return True
    else:
        print("El texto no es válido")
        return False
    
def validar_dni(dni):
    if re.match("^[0-9]{8}[A-Z]$", dni):
        return True
    else:
        for cliente in db.Clientes.lista:
            if cliente.dni == dni:
                print("El DNI ya existe")
                return False
    

    

