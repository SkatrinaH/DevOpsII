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