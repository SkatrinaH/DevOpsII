from services.gestion_clientes import GestionClientes
from services.gestion_servicios import GestionServicios

def main():
    gestor_clientes = GestionClientes()
    gestor_servicios = GestionServicios()

    while True:
        print("\nMenú de opciones:")
        print("1. Agregar cliente")
        print("2. Ver clientes")
        print("3. Agregar servicio")
        print("4. Ver servicios")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            email = input("Email: ")
            telefono = input("Teléfono: ")
            print(gestor_clientes.agregar_cliente(nombre, email, telefono))
        elif opcion == "2":
            print("\nClientes registrados:")
            for cliente in gestor_clientes.mostrar_clientes():
                print(cliente)
        elif opcion == "3":
            nombre = input("Nombre del servicio: ")
            costo = float(input("Costo: "))
            descripcion = input("Descripción: ")
            print(gestor_servicios.agregar_servicio(nombre, costo, descripcion))
        elif opcion == "4":
            print("\nServicios disponibles:")
            for servicio in gestor_servicios.mostrar_servicios():
                print(servicio)
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()