import tkinter as tk
from tkinter import messagebox


class MenuCliente:
    """Ventana principal del menú para clientes."""

    def __init__(self, root, id_cliente=None):
        self.root = root
        self.id_cliente = id_cliente  # se usará cuando el login esté listo
        self.root.title("AutoTrust S.A. - Menú Cliente")
        self.root.geometry("400x420")
        self.root.resizable(False, False)

        self._construir_interfaz()

    def _construir_interfaz(self):
        # Título
        tk.Label(self.root, text="AutoTrust S.A.",
                 font=("Arial", 18, "bold")).pack(pady=(20, 5))
        tk.Label(self.root, text="Menú Cliente",
                 font=("Arial", 12)).pack(pady=(0, 20))

        # Marco de botones
        marco = tk.Frame(self.root)
        marco.pack(pady=10)

        botones = [
            ("Actualizar mis datos",         self.abrir_actualizar_datos),
            ("Ver vehículos disponibles",     self.abrir_vehiculos_disponibles),
            ("Solicitar alquiler",            self.abrir_solicitar_alquiler),
            ("Historial de alquileres",       self.abrir_historial),
        ]

        for texto, comando in botones:
            tk.Button(marco, text=texto, width=25, height=2,
                      command=comando).pack(pady=5)

        # Cerrar sesión
        tk.Button(self.root, text="Cerrar sesión", width=25,
                  command=self.cerrar_sesion).pack(pady=(20, 0))

    # ── Navegación ──────────────

    def abrir_actualizar_datos(self):
        from interfaz.clientes import VentanaActualizarCliente
        VentanaActualizarCliente(tk.Toplevel(self.root), self.id_cliente)

    def abrir_vehiculos_disponibles(self):
        from interfaz.vehiculos import VentanaVehiculosDisponibles
        VentanaVehiculosDisponibles(tk.Toplevel(self.root))

    def abrir_solicitar_alquiler(self):
        from interfaz.alquileres import VentanaSolicitarAlquiler
        VentanaSolicitarAlquiler(tk.Toplevel(self.root), self.id_cliente)

    def abrir_historial(self):
        from interfaz.alquileres import VentanaHistorialAlquileres
        VentanaHistorialAlquileres(tk.Toplevel(self.root), self.id_cliente)

    def cerrar_sesion(self):
        if messagebox.askyesno("Cerrar sesión", "¿Desea cerrar sesión?"):
            self.root.destroy()


# Punto de entrada 
if __name__ == "__main__":
    root = tk.Tk()
    app = MenuCliente(root, id_cliente="cliente_prueba")
    root.mainloop()