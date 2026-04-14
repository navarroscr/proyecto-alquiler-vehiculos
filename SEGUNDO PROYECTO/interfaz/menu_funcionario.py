import tkinter as tk
from tkinter import messagebox


class MenuFuncionario:
    """Ventana principal del menú para funcionarios."""

    def __init__(self, root):
        self.root = root
        self.root.title("AutoTrust S.A. - Menú Funcionario")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self._construir_interfaz()

    def _construir_interfaz(self):
        # Título
        tk.Label(self.root, text="AutoTrust S.A.",
                 font=("Arial", 18, "bold")).pack(pady=(20, 5))
        tk.Label(self.root, text="Menú Funcionario",
                 font=("Arial", 12)).pack(pady=(0, 20))

        # Marco de botones
        marco = tk.Frame(self.root)
        marco.pack(pady=10)

        botones = [
            ("Clientes",      self.abrir_clientes),
            ("Funcionarios",  self.abrir_funcionarios),
            ("Vehículos",     self.abrir_vehiculos),
            ("Alquileres",    self.abrir_alquileres),
            ("Devoluciones",  self.abrir_devoluciones),
            ("Reportes",      self.abrir_reportes),
            ("Acerca de",     self.abrir_acerca_de),
        ]

        for texto, comando in botones:
            tk.Button(marco, text=texto, width=25, height=2,
                      command=comando).pack(pady=5)

        # Botón cerrar sesión abajo
        tk.Button(self.root, text="Cerrar sesión", width=25,
                  command=self.cerrar_sesion).pack(pady=(15, 0))

    # ── Navegación ─────────────────

    def abrir_clientes(self):
        from interfaz.clientes import VentanaClientes
        VentanaClientes(tk.Toplevel(self.root))

    def abrir_funcionarios(self):
        from interfaz.funcionarios import VentanaFuncionarios
        VentanaFuncionarios(tk.Toplevel(self.root))

    def abrir_vehiculos(self):
        from interfaz.vehiculos import VentanaVehiculos
        VentanaVehiculos(tk.Toplevel(self.root))

    def abrir_alquileres(self):
        from interfaz.alquileres import VentanaAlquileres
        VentanaAlquileres(tk.Toplevel(self.root))

    def abrir_devoluciones(self):
        from interfaz.devoluciones import VentanaDevoluciones
        VentanaDevoluciones(tk.Toplevel(self.root))

    def abrir_reportes(self):
        from interfaz.reportes import VentanaReportes
        VentanaReportes(tk.Toplevel(self.root))

    def abrir_acerca_de(self):
        messagebox.showinfo(
            "Acerca de",
            "AutoTrust S.A.\nSistema de Alquiler de Vehículos\n\n"
            "Desarrollado por:\nJean Carlo Navarro\nSamuel Brenes\n\n"
            "Programación III - I Cuatrimestre 2026"
        )

    def cerrar_sesion(self):
        if messagebox.askyesno("Cerrar sesión", "¿Desea cerrar sesión?"):
            self.root.destroy()


# ── Punto de entrada temporal
if __name__ == "__main__":
    root = tk.Tk()
    app = MenuFuncionario(root)
    root.mainloop()