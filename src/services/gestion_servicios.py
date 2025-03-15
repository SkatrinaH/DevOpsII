from models.servicio import Servicio

class GestionServicios:
    def __init__(self):
        self.servicios = {}

    def agregar_servicio(self, nombre, costo, descripcion=""):
        if nombre not in self.servicios:
            self.servicios[nombre] = Servicio(nombre, costo, descripcion)
            return f"Servicio {nombre} agregado correctamente."
        return "El servicio ya existe."

    def mostrar_servicios(self):
        return [servicio.mostrar_info() for servicio in self.servicios.values()]

    def asignar_servicio_a_cliente(self, cliente, nombre_servicio):
        if nombre_servicio in self.servicios:
            cliente.agregar_servicio(self.servicios[nombre_servicio])
            return f"Servicio {nombre_servicio} asignado a {cliente.nombre}."
        return "El servicio no existe."