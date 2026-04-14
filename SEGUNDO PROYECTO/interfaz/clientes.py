import tkinter as tk
from tkinter import messagebox, ttk
import logica.clientes_logica as clientes_logica


# ══════════════════════════════════════════════════════════════
#  VENTANA COMPLETA — para el funcionario
# ══════════════════════════════════════════════════════════════

class VentanaClientes:
    """Gestión completa de clientes (solo funcionario)."""

    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Clientes")
        self.root.geometry("800x540")
        self.root.resizable(False, False)

        self._construir_interfaz()
        self._cargar_tabla()

    def _construir_interfaz(self):
        tk.Label(self.root, text="Gestión de Clientes",
                 font=("Arial", 14, "bold")).pack(pady=(10, 5))

        # ── Formulario ──────────────
        marco_form = tk.LabelFrame(self.root, text="Datos del cliente", padx=10, pady=10)
        marco_form.pack(fill="x", padx=15, pady=5)

        campos = [
            ("ID Cliente",       "entry_id"),
            ("Nombre",           "entry_nombre"),
            ("Cédula",           "entry_cedula"),
            ("Teléfono",         "entry_telefono"),
            ("Correo",           "entry_correo"),
            ("Dirección",        "entry_direccion"),
            ("Fecha nacimiento", "entry_nacimiento"),
        ]

        for i, (etiqueta, atributo) in enumerate(campos):
            fila = i // 2
            columna = (i % 2) * 2
            tk.Label(marco_form, text=etiqueta + ":").grid(
                row=fila, column=columna, sticky="e", padx=5, pady=4)
            entry = tk.Entry(marco_form, width=25)
            entry.grid(row=fila, column=columna + 1, padx=5, pady=4)
            setattr(self, atributo, entry)

        # ── Botones ────────────
        marco_botones = tk.Frame(self.root)
        marco_botones.pack(pady=8)

        tk.Button(marco_botones, text="Agregar",    width=12,
                  command=self._agregar).grid(row=0, column=0, padx=5)
        tk.Button(marco_botones, text="Modificar",  width=12,
                  command=self._modificar).grid(row=0, column=1, padx=5)
        tk.Button(marco_botones, text="Desactivar", width=12,
                  command=self._desactivar).grid(row=0, column=2, padx=5)
        tk.Button(marco_botones, text="Limpiar",    width=12,
                  command=self._limpiar).grid(row=0, column=3, padx=5)

        # ── Tabla ──────────────────
        marco_tabla = tk.Frame(self.root)
        marco_tabla.pack(fill="both", expand=True, padx=15, pady=5)

        columnas = ("id", "nombre", "cedula", "telefono", "correo",
                    "direccion", "nacimiento", "estado")
        self.tabla = ttk.Treeview(marco_tabla, columns=columnas,
                                  show="headings", height=8)

        encabezados = ("ID", "Nombre", "Cédula", "Teléfono", "Correo",
                       "Dirección", "Nacimiento", "Estado")
        anchos      = (80,   150,      90,        90,         140,
                       120,  90,       70)
        for col, enc, ancho in zip(columnas, encabezados, anchos):
            self.tabla.heading(col, text=enc)
            self.tabla.column(col, width=ancho, anchor="center")

        scroll = ttk.Scrollbar(marco_tabla, orient="vertical",
                               command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll.set)
        self.tabla.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        # llena el formulario
        self.tabla.bind("<<TreeviewSelect>>", self._seleccionar_fila)

    # ── Lógica de la interfaz ───────────

    def _cargar_tabla(self):
        """Recarga todos los clientes desde la BD."""
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        for c in clientes_logica.obtener_todos_los_clientes():
            self.tabla.insert("", "end", values=(
                c.get("id_cliente"),        c.get("nombre"),    c.get("cedula"),
                c.get("telefono"),          c.get("correo"),    c.get("direccion"),
                c.get("fecha_nacimiento"),  c.get("estado")
            ))

    def _seleccionar_fila(self, event):
        """Llena el formulario con los datos de la fila seleccionada"""
        seleccion = self.tabla.selection()
        if not seleccion:
            return
        valores = self.tabla.item(seleccion[0])["values"]
        entries = [self.entry_id,    self.entry_nombre,    self.entry_cedula,
                   self.entry_telefono, self.entry_correo, self.entry_direccion,
                   self.entry_nacimiento]
        for entry, valor in zip(entries, valores[:7]):
            entry.config(state="normal")
            entry.delete(0, tk.END)
            entry.insert(0, str(valor))
        self.entry_id.config(state="disabled")  # el ID no se edita

    def _agregar(self):
        try:
            clientes_logica.crear_cliente(
                self.entry_id.get().strip(),
                self.entry_nombre.get().strip(),
                self.entry_cedula.get().strip(),
                self.entry_telefono.get().strip(),
                self.entry_correo.get().strip(),
                self.entry_direccion.get().strip(),
                self.entry_nacimiento.get().strip()
            )
            messagebox.showinfo("Éxito", "Cliente agregado correctamente.")
            self._limpiar()
            self._cargar_tabla()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _modificar(self):
        id_cliente = self.entry_id.get().strip()
        if not id_cliente:
            messagebox.showwarning("Atención", "Seleccione un cliente de la tabla.")
            return
        nuevos_datos = {}
        if self.entry_nombre.get().strip():
            nuevos_datos["nombre"]    = self.entry_nombre.get().strip()
        if self.entry_telefono.get().strip():
            nuevos_datos["telefono"]  = self.entry_telefono.get().strip()
        if self.entry_correo.get().strip():
            nuevos_datos["correo"]    = self.entry_correo.get().strip()
        if self.entry_direccion.get().strip():
            nuevos_datos["direccion"] = self.entry_direccion.get().strip()
        if not nuevos_datos:
            messagebox.showwarning("Atención", "No hay datos para modificar.")
            return
        try:
            clientes_logica.actualizar_cliente(id_cliente, nuevos_datos)
            messagebox.showinfo("Éxito", "Cliente actualizado correctamente.")
            self._limpiar()
            self._cargar_tabla()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _desactivar(self):
        id_cliente = self.entry_id.get().strip()
        if not id_cliente:
            messagebox.showwarning("Atención", "Seleccione un cliente de la tabla.")
            return
        if messagebox.askyesno("Confirmar", f"¿Desactivar el cliente {id_cliente}?"):
            try:
                clientes_logica.eliminar_cliente(id_cliente)
                messagebox.showinfo("Éxito", "Cliente desactivado.")
                self._limpiar()
                self._cargar_tabla()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def _limpiar(self):
        for entry in [self.entry_id,       self.entry_nombre,    self.entry_cedula,
                      self.entry_telefono, self.entry_correo,    self.entry_direccion,
                      self.entry_nacimiento]:
            entry.config(state="normal")
            entry.delete(0, tk.END)


# ══════════════════════════════════════════════════════════════
#  VENTANA — el cliente solo edita sus propios datos
# ══════════════════════════════════════════════════════════════

class VentanaActualizarCliente:
    """El cliente solo puede modificar su propio teléfono, correo y dirección."""

    def __init__(self, root, id_cliente):
        self.root = root
        self.id_cliente = id_cliente
        self.root.title("Actualizar mis datos")
        self.root.geometry("380x300")
        self.root.resizable(False, False)

        self._construir_interfaz()
        self._cargar_datos()

    def _construir_interfaz(self):
        tk.Label(self.root, text="Actualizar mis datos",
                 font=("Arial", 13, "bold")).pack(pady=(15, 10))

        marco = tk.Frame(self.root)
        marco.pack(padx=20)

        campos = [("Teléfono", "entry_telefono"),
                  ("Correo",   "entry_correo"),
                  ("Dirección","entry_direccion")]

        for i, (etiqueta, atributo) in enumerate(campos):
            tk.Label(marco, text=etiqueta + ":", width=10,
                     anchor="e").grid(row=i, column=0, pady=6)
            entry = tk.Entry(marco, width=28)
            entry.grid(row=i, column=1, pady=6, padx=5)
            setattr(self, atributo, entry)

        tk.Button(self.root, text="Guardar cambios", width=20,
                  command=self._guardar).pack(pady=15)

    def _cargar_datos(self):
        """Precarga los datos actuales del cliente."""
        cliente = clientes_logica.buscar_cliente(self.id_cliente)
        if cliente:
            self.entry_telefono.insert(0, cliente.get("telefono", ""))
            self.entry_correo.insert(0,   cliente.get("correo", ""))
            self.entry_direccion.insert(0, cliente.get("direccion", ""))

    def _guardar(self):
        nuevos_datos = {
            "telefono":  self.entry_telefono.get().strip(),
            "correo":    self.entry_correo.get().strip(),
            "direccion": self.entry_direccion.get().strip(),
        }
        try:
            clientes_logica.actualizar_cliente(self.id_cliente, nuevos_datos)
            messagebox.showinfo("Éxito", "Datos actualizados correctamente.")
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))