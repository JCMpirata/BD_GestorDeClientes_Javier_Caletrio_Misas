import csv
import config 


class Cliente:
    def __init__(self, id, nombre, apellido, dni):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return f"{self.id}, {self.nombre}, {self.apellido}, {self.dni}"
    
    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "apellido": self.apellido, "dni": self.dni}
    
class Clientes:

    lista = []
    with open(config.DATABASE_PATH, newline = "\n") as fichero:
        lector = csv.DictReader(fichero, delimiter = ";")
        for id, nombre, apellido, dni in lector:
            lista.append(Cliente(int(id), nombre, apellido, dni))

    @staticmethod
    def buscar(id):
        for cliente in Clientes.lista:
            if cliente.id == id:
                return cliente

    @staticmethod
    def crear(id, nombre, apellido, dni):
        cliente = Cliente(id, nombre, apellido, dni)
        Clientes.lista.append(cliente)
        Clientes.guardar()
        return cliente
    
    @staticmethod
    def editar(id, nombre, apellido, dni):
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.id == id:
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellido = apellido
                Clientes.lista[indice].dni = dni
                Clientes.guardar()
                return Clientes.lista[indice]
            
    @staticmethod
    def borrar(id):
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.id == id:
                cliente = Clientes.lista.pop(indice)
                Clientes.guardar()
                return cliente

    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for cliente in Clientes.lista:
                writer.writerow((cliente.id, cliente.dni, cliente.nombre, cliente.apellido))