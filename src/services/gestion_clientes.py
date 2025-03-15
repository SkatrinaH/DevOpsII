from models.cliente import Cliente
from services.gestion_servicios import GestionServicios

class GestionClientes:
    def __init__(self):
        self.clientes = {}

    def agregar_cliente(self, nombre, email, telefono):
        if nombre not in self.clientes:
            self.clientes[nombre] = Cliente(nombre, email, telefono)
            return f"Cliente {nombre} agregado correctamente."
        return "El cliente ya existe."

    def mostrar_clientes(self):
        return [cliente.mostrar_info() for cliente in self.clientes.values()]

    def asignar_servicio_a_cliente(self, nombre_cliente, gestion_servicios, nombre_servicio):
        if nombre_cliente in self.clientes:
            return gestion_servicios.asignar_servicio_a_cliente(self.clientes[nombre_cliente], nombre_servicio)
        return "El cliente no existe."
