import sys
from services.gestion_clientes import GestionClientes
from services.gestion_servicios import GestionServicios

def main():
    gestor_clientes = GestionClientes()
    gestor_servicios = GestionServicios()

    if not sys.stdin.isatty():  # Si el entorno no es interactivo (ejemplo: GitHub Actions)
        print("⚠️ Modo automatizado detectado: Ejecutando pruebas sin interacción.")
        # Aquí podrías agregar pruebas automáticas en lugar de input()
        return

    while True:
        print("\nMenú de opciones:")
        print("1. Agregar cliente")
        print("2. Ver clientes")
        print("3. Agregar servicio")
        print("4. Ver servicios")
        print("5. Salir")

        try:
            opcion = input("Seleccione una opción: ")
        except EOFError:
            print("Error: No se puede leer la entrada en modo automatizado.")
            break

        if opcion == "1":
            nombre = input("Nombre del cliente: ")
            email = input("Email del cliente: ")
            telefono = input("Teléfono del cliente: ")
            print(gestor_clientes.agregar_cliente(nombre, email, telefono))
        elif opcion == "2":
            print("\nClientes registrados:")
            for cliente in gestor_clientes.mostrar_clientes():
                print(cliente)
        elif opcion == "3":
            nombre_servicio = input("Nombre del servicio: ")
            costo = float(input("Costo del servicio: "))
            descripcion = input("Descripción del servicio: ")
            print(gestor_servicios.agregar_servicio(nombre_servicio, costo, descripcion))
        elif opcion == "4":
            print("\nServicios disponibles:")
            for servicio in gestor_servicios.mostrar_servicios():
                print(servicio)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()