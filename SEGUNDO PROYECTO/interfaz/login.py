import tkinter as tk
from tkinter import messagebox
import datos.usuarios_datos as usuarios_datos


class VentanaLogin:
    """Ventana de ingreso al sistema."""

    def __init__(self, root):
        self.root = root
        self.root.title("AutoTrust S.A. - Ingreso")
        self.root.geometry("360x280")
        self.root.resizable(False, False)

        self._construir_interfaz()

    def _construir_interfaz(self):
        tk.Label(self.root, text="AutoTrust S.A.",
                 font=("Arial", 18, "bold")).pack(pady=(30, 5))
        tk.Label(self.root, text="Ingrese sus credenciales",
                 font=("Arial", 10)).pack(pady=(0, 20))

        marco = tk.Frame(self.root)
        marco.pack(padx=30)

        # Usuario
        tk.Label(marco, text="Usuario:", anchor="e",
                 width=12).grid(row=0, column=0, pady=8)
        self.entry_usuario = tk.Entry(marco, width=22)
        self.entry_usuario.grid(row=0, column=1, pady=8, padx=5)

        # Contraseña
        tk.Label(marco, text="Contraseña:", anchor="e",
                 width=12).grid(row=1, column=0, pady=8)
        self.entry_contrasena = tk.Entry(marco, width=22, show="*")
        self.entry_contrasena.grid(row=1, column=1, pady=8, padx=5)

        # Botón ingresar
        tk.Button(self.root, text="Ingresar", width=20,
                  command=self._ingresar).pack(pady=(15, 5))

        # También permite presionar Enter para ingresar
        self.root.bind("<Return>", lambda event: self._ingresar())

        # Botón registro de nuevo cliente
        tk.Button(self.root, text="Registrarme como cliente", width=20,
                  command=self._registrar_cliente).pack()

    # ── Lógica del login ────────────────────────────────────────

    def _ingresar(self):
        nombre_usuario = self.entry_usuario.get().strip()
        contrasena     = self.entry_contrasena.get().strip()

        if not nombre_usuario or not contrasena:
            messagebox.showwarning("Atención", "Ingrese usuario y contraseña.")
            return

        # Buscar usuario en MongoDB
        usuario = usuarios_datos.buscar_usuario_por_nombre(nombre_usuario)

        if not usuario:
            messagebox.showerror("Error", "Usuario no encontrado.")
            return

        # Verificar que esté activo
        if usuario.get("estado") != "activo":
            messagebox.showerror("Acceso denegado",
                                 "Su cuenta está inactiva. "
                                 "Contacte a un funcionario.")
            return

        # Verificar contraseña
        if usuario.get("contrasena") != contrasena:
            messagebox.showerror("Error", "Contraseña incorrecta.")
            return

        # Redirigir según tipo de usuario
        tipo = usuario.get("tipo_usuario", "").lower()
        id_referencia = usuario.get("id_usuario")

        self.root.destroy()  # cierra el login

        nueva_root = tk.Tk()
        if tipo == "funcionario":
            from interfaz.menu_funcionario import MenuFuncionario
            MenuFuncionario(nueva_root)
        elif tipo == "cliente":
            from interfaz.menu_cliente import MenuCliente
            MenuCliente(nueva_root, id_cliente=id_referencia)
        else:
            messagebox.showerror("Error", "Tipo de usuario desconocido.")
            return

        nueva_root.mainloop()

    def _registrar_cliente(self):
        """Abre el formulario de registro para nuevos clientes."""
        from interfaz.clientes import VentanaClientes
        VentanaClientes(tk.Toplevel(self.root))


# ── Punto de entrada principal del sistema ──────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaLogin(root)
    root.mainloop()