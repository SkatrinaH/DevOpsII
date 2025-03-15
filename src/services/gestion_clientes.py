import json
import os
from models.cliente import Cliente

class GestionClientes:
    def __init__(self, file_path="clientes.json"):
        self.file_path = file_path
        self.clientes = self.cargar_clientes()

    def cargar_clientes(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                data = json.load(file)
                return {nombre: Cliente.from_dict(info) for nombre, info in data.items()}
        return {}

    def guardar_clientes(self):
        with open(self.file_path, "w") as file:
            json.dump({nombre: cliente.to_dict() for nombre, cliente in self.clientes.items()}, file, indent=4)

    def agregar_cliente(self, nombre, email, telefono):
        if nombre not in self.clientes:
            self.clientes[nombre] = Cliente(nombre, email, telefono)
            self.guardar_clientes()
            return f"Cliente {nombre} agregado correctamente."
        return "El cliente ya existe."

    def mostrar_clientes(self):
        return [cliente.mostrar_info() for cliente in self.clientes.values()]