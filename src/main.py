from services.gestion_clientes import GestionClientes
from services.gestion_servicios import GestionServicios

def main():
    gestor_clientes = GestionClientes()
    gestor_servicios = GestionServicios()

    # Agregar clientes
    print(gestor_clientes.agregar_cliente("Juan Pérez", "juan@example.com", "123456789"))
    print(gestor_clientes.agregar_cliente("Ana Gómez", "ana@example.com", "987654321"))

    # Agregar servicios
    print(gestor_servicios.agregar_servicio("Internet", 50, "Conexión de 100 Mbps"))
    print(gestor_servicios.agregar_servicio("Telefonía", 30, "Llamadas ilimitadas nacionales"))
    
    # Asignar servicios a clientes
    print(gestor_clientes.asignar_servicio_a_cliente("Juan Pérez", gestor_servicios, "Internet"))
    print(gestor_clientes.asignar_servicio_a_cliente("Ana Gómez", gestor_servicios, "Telefonía"))

    # Mostrar clientes y servicios asignados
    print("\nClientes registrados:")
    for cliente in gestor_clientes.mostrar_clientes():
        print(cliente)

    print("\nServicios disponibles:")
    for servicio in gestor_servicios.mostrar_servicios():
        print(servicio)

if __name__ == "__main__":
    main()