import json
from models.servicio import Servicio

class Cliente:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.servicios_contratados = []

    def agregar_servicio(self, servicio):
        self.servicios_contratados.append(servicio)

    def mostrar_info(self):
        return f"Cliente: {self.nombre}, Email: {self.email}, Teléfono: {self.telefono}, Servicios: {len(self.servicios_contratados)}"

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "email": self.email,
            "telefono": self.telefono,
            "servicios_contratados": [servicio.to_dict() for servicio in self.servicios_contratados]
        }

    @staticmethod
    def from_dict(data):
        cliente = Cliente(data["nombre"], data["email"], data["telefono"])
        cliente.servicios_contratados = [Servicio.from_dict(s) for s in data["servicios_contratados"]]
        return cliente