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
