import re
import os
import platform
import database as db


def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def validar_id(id, lista):
    if re.match(int("^[0-9]+$"), id):
        for cliente in lista:
            if cliente.id == id:
                print("El ID ya existe")
                return False
        return True
    else:
        print("El ID no es válido")
        return False


def validar_texto(longitud_min = 3, longitud_max = 50):
    while True:
        texto = input("Introduce un texto: ")
        if re.match("^[a-zA-ZñÑáéíóúÁÉÍÓÚ ]+$", texto):
            if longitud_min <= len(texto) <= longitud_max:
                return texto
            else:
                print("El texto debe tener entre {} y {} caracteres".format(longitud_min, longitud_max))
        else:
            print("El texto no es válido")

    
def validar_dni(dni, lista):
    if re.match("^[0-9]{8}[A-Z]$", dni):
        return True
    else:
        for cliente in lista:
            if cliente.dni == dni:
                print("El DNI ya existe")
                return False
        print("El DNI no es válido")
        return False
    

    

