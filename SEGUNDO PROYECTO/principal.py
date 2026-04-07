from logica import *

def menu_principal():
    """Muestra el menú principal de opciones del sistema."""
    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestión de Clientes")
        print("2. Gestión de Funcionarios")
        print("3. Gestión de Vehículos")
        print("4. Alquileres")
        print("5. Devoluciones")
        print("6. Reportes")
        print("7. Salir")
        
        opcion = input("Seleccione una opción (1-7): ")

        if opcion == '1':
            menu_clientes()
        elif opcion == '2':
            menu_funcionarios()
        elif opcion == '3':
            menu_vehiculos()
        elif opcion == '4':
            menu_alquileres()
        elif opcion == '5':
            menu_devoluciones()
        elif opcion == '6':
            menu_reportes()
        elif opcion == '7':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_clientes():
    """Submenú de gestión de clientes."""
    print("\n--- Gestión de Clientes ---")
    print("Funcionalidad aún no implementada.")

def menu_funcionarios():
    """Submenú de gestión de funcionarios."""
    print("\n--- Gestión de Funcionarios ---")
    print("Funcionalidad aún no implementada.")

def menu_vehiculos():
    """Submenú de gestión de vehículos."""
    print("\n--- Gestión de Vehículos ---")
    print("Funcionalidad aún no implementada.")

def menu_alquileres():
    """Submenú de alquileres."""
    print("\n--- Alquileres ---")
    print("Funcionalidad aún no implementada.")

def menu_devoluciones():
    """Submenú de devoluciones."""
    print("\n--- Devoluciones ---")
    print("Funcionalidad aún no implementada.")

def menu_reportes():
    """Submenú de reportes."""
    print("\n--- Reportes ---")
    print("Funcionalidad aún no implementada.")


if __name__ == "__main__":
    menu_principal()