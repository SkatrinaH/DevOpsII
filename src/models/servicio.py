class Servicio:
    def __init__(self, nombre, costo, descripcion=""):
        self.nombre = nombre
        self.costo = costo
        self.descripcion = descripcion

    def mostrar_info(self):
        return f"Servicio: {self.nombre}, Costo: ${self.costo}, Descripción: {self.descripcion}"
