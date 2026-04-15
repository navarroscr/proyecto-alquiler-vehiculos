import tkinter as tk
from tkinter import messagebox, ttk
import logica.alquiler_logica as alquiler_logica
import datos.alquiler_datos as alquiler_datos
import logica.vehiculo_logica as vehiculo_logica


# ══════════════════════════════════════════════════════════════
#  REGISTRAR ALQUILER — funcionario y cliente
# ══════════════════════════════════════════════════════════════

class VentanaSolicitarAlquiler:
    """Formulario para registrar un nuevo alquiler (queda en estado pendiente)"""

    def __init__(self, root, id_cliente=None):
        self.root = root
        self.id_cliente = id_cliente
        self.root.title("Solicitar Alquiler")
        self.root.geometry("480x420")
        self.root.resizable(False, False)

        self._construir_interfaz()

    def _construir_interfaz(self):
        tk.Label(self.root, text="Solicitar Alquiler",
                 font=("Arial", 14, "bold")).pack(pady=(15, 10))

        marco = tk.LabelFrame(self.root, text="Datos del alquiler", padx=15, pady=10)
        marco.pack(fill="x", padx=20, pady=5)

        # ID Cliente
        tk.Label(marco, text="ID Cliente:", anchor="e", width=14).grid(
            row=0, column=0, sticky="e", pady=5)
        self.entry_id_cliente = tk.Entry(marco, width=25)
        self.entry_id_cliente.grid(row=0, column=1, pady=5, padx=5)
        # Si ya viene el id_cliente lo precarga y bloquea
        if self.id_cliente:
            self.entry_id_cliente.insert(0, self.id_cliente)
            self.entry_id_cliente.config(state="disabled")

        # ID Vehículo
        tk.Label(marco, text="ID Vehículo:", anchor="e", width=14).grid(
            row=1, column=0, sticky="e", pady=5)
        self.entry_id_vehiculo = tk.Entry(marco, width=25)
        self.entry_id_vehiculo.grid(row=1, column=1, pady=5, padx=5)

        # Fecha inicio
        tk.Label(marco, text="Fecha inicio:", anchor="e", width=14).grid(
            row=2, column=0, sticky="e", pady=5)
        self.entry_fecha_inicio = tk.Entry(marco, width=25)
        self.entry_fecha_inicio.grid(row=2, column=1, pady=5, padx=5)
        tk.Label(marco, text="(YYYY-MM-DD)", font=("Arial", 8),
                 fg="gray").grid(row=2, column=2, sticky="w")

        # Fecha fin
        tk.Label(marco, text="Fecha fin:", anchor="e", width=14).grid(
            row=3, column=0, sticky="e", pady=5)
        self.entry_fecha_fin = tk.Entry(marco, width=25)
        self.entry_fecha_fin.grid(row=3, column=1, pady=5, padx=5)
        tk.Label(marco, text="(YYYY-MM-DD)", font=("Arial", 8),
                 fg="gray").grid(row=3, column=2, sticky="w")

        # Seguro diario
        tk.Label(marco, text="Seguro diario:", anchor="e", width=14).grid(
            row=4, column=0, sticky="e", pady=5)
        self.entry_seguro = tk.Entry(marco, width=25)
        self.entry_seguro.grid(row=4, column=1, pady=5, padx=5)

        # Botón calcular / registrar
        tk.Button(self.root, text="Calcular y Registrar", width=22,
                  command=self._registrar).pack(pady=12)

        # Resumen de costos
        self.marco_resumen = tk.LabelFrame(self.root, text="Resumen de costos",
                                           padx=10, pady=8)
        self.marco_resumen.pack(fill="x", padx=20)

        self.lbl_dias     = tk.Label(self.marco_resumen, text="Días: -")
        self.lbl_subtotal = tk.Label(self.marco_resumen, text="Subtotal: -")
        self.lbl_impuesto = tk.Label(self.marco_resumen, text="Impuesto (13%): -")
        self.lbl_seguro   = tk.Label(self.marco_resumen, text="Seguro: -")
        self.lbl_total    = tk.Label(self.marco_resumen, text="TOTAL: -",
                                     font=("Arial", 10, "bold"))

        for lbl in [self.lbl_dias, self.lbl_subtotal, self.lbl_impuesto,
                    self.lbl_seguro, self.lbl_total]:
            lbl.pack(anchor="w")

    def _registrar(self):
        try:
            id_cliente   = self.entry_id_cliente.get().strip()
            id_vehiculo  = self.entry_id_vehiculo.get().strip()
            fecha_inicio = self.entry_fecha_inicio.get().strip()
            fecha_fin    = self.entry_fecha_fin.get().strip()
            seguro       = float(self.entry_seguro.get().strip())

            resultado = alquiler_logica.registrar_alquiler(
                id_cliente, id_vehiculo, fecha_inicio, fecha_fin, seguro
            )

            # Mostrar resumen
            self.lbl_dias.config(
                text=f"Días: {resultado['dias']}")
            self.lbl_subtotal.config(
                text=f"Subtotal: ₡{resultado['subtotal']:,.2f}")
            self.lbl_impuesto.config(
                text=f"Impuesto (13%): ₡{resultado['impuesto']:,.2f}")
            self.lbl_seguro.config(
                text=f"Seguro: ₡{resultado['seguro']:,.2f}")
            self.lbl_total.config(
                text=f"TOTAL: ₡{resultado['total']:,.2f}")

            messagebox.showinfo(
                "Alquiler registrado",
                f"Alquiler registrado correctamente.\n"
                f"ID: {resultado['id_alquiler']}\n"
                f"Estado: PENDIENTE\n\n"
                f"Preséntese a retirar el vehículo para activarlo."
            )
        except ValueError as e:
            messagebox.showerror("Error de validación", str(e))
        except Exception as e:
            messagebox.showerror("Error", str(e))


# ══════════════════════════════════════════════════════════════
#  GESTIÓN DE ALQUILERES — solo funcionario
# ══════════════════════════════════════════════════════════════

class VentanaAlquileres:
    """Lista todos los alquileres. El funcionario puede activar los pendientes."""

    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Alquileres")
        self.root.geometry("820x480")
        self.root.resizable(False, False)

        self._construir_interfaz()
        self._cargar_tabla()

    def _construir_interfaz(self):
        tk.Label(self.root, text="Gestión de Alquileres",
                 font=("Arial", 14, "bold")).pack(pady=(10, 5))

        # Botones superiores
        marco_botones = tk.Frame(self.root)
        marco_botones.pack(pady=5)

        tk.Button(marco_botones, text="Nuevo alquiler", width=16,
                  command=self._nuevo_alquiler).grid(row=0, column=0, padx=5)
        tk.Button(marco_botones, text="Activar (pendiente → en préstamo)", width=30,
                  command=self._activar_alquiler).grid(row=0, column=1, padx=5)
        tk.Button(marco_botones, text="Actualizar lista", width=14,
                  command=self._cargar_tabla).grid(row=0, column=2, padx=5)

        # Tabla
        marco_tabla = tk.Frame(self.root)
        marco_tabla.pack(fill="both", expand=True, padx=15, pady=10)

        columnas = ("id", "id_cliente", "id_vehiculo", "fecha_inicio",
                    "fecha_fin", "dias", "total", "estado")
        self.tabla = ttk.Treeview(marco_tabla, columns=columnas,
                                  show="headings", height=14)

        encabezados = ("ID Alquiler", "ID Cliente", "ID Vehículo",
                       "Fecha inicio", "Fecha fin", "Días", "Total", "Estado")
        anchos = (90, 90, 90, 95, 90, 45, 90, 90)
        for col, enc, ancho in zip(columnas, encabezados, anchos):
            self.tabla.heading(col, text=enc)
            self.tabla.column(col, width=ancho, anchor="center")

        scroll = ttk.Scrollbar(marco_tabla, orient="vertical",
                               command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll.set)
        self.tabla.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

    def _cargar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        for a in alquiler_datos.obtener_todos_los_alquileres():
            self.tabla.insert("", "end", values=(
                a.get("id_alquiler"),  a.get("id_cliente"),
                a.get("id_vehiculo"),  a.get("fecha_inicio"),
                a.get("fecha_fin"),    a.get("cantidad_dias"),
                f"₡{a.get('total', 0):,.2f}", a.get("estado")
            ))

    def _nuevo_alquiler(self):
        VentanaSolicitarAlquiler(tk.Toplevel(self.root))

    def _activar_alquiler(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione un alquiler de la tabla.")
            return

        valores = self.tabla.item(seleccion[0])["values"]
        id_alquiler = str(valores[0])
        id_vehiculo = str(valores[2])
        estado      = str(valores[7])

        if estado != "pendiente":
            messagebox.showwarning("Atención",
                                   "Solo se pueden activar alquileres en estado 'pendiente'.")
            return

        if messagebox.askyesno("Confirmar",
                               f"¿Activar el alquiler {id_alquiler}?\n"
                               f"El vehículo pasará a estado 'en préstamo'."):
            try:
                alquiler_logica.activar_alquiler(id_alquiler, id_vehiculo)
                messagebox.showinfo("Éxito", "Alquiler activado correctamente.")
                self._cargar_tabla()
            except Exception as e:
                messagebox.showerror("Error", str(e))


# ══════════════════════════════════════════════════════════════
#  HISTORIAL — solo cliente
# ══════════════════════════════════════════════════════════════

class VentanaHistorialAlquileres:
    """El cliente ve el historial de sus propios alquileres."""

    def __init__(self, root, id_cliente):
        self.root = root
        self.id_cliente = id_cliente
        self.root.title("Mi historial de alquileres")
        self.root.geometry("720x350")
        self.root.resizable(False, False)

        self._construir_interfaz()
        self._cargar_tabla()

    def _construir_interfaz(self):
        tk.Label(self.root, text="Mi historial de alquileres",
                 font=("Arial", 13, "bold")).pack(pady=(12, 8))

        marco_tabla = tk.Frame(self.root)
        marco_tabla.pack(fill="both", expand=True, padx=15, pady=5)

        columnas = ("id", "id_vehiculo", "fecha_inicio",
                    "fecha_fin", "dias", "total", "estado")
        self.tabla = ttk.Treeview(marco_tabla, columns=columnas,
                                  show="headings", height=10)

        encabezados = ("ID Alquiler", "Vehículo", "Fecha inicio",
                       "Fecha fin", "Días", "Total", "Estado")
        anchos = (100, 90, 95, 90, 45, 100, 90)
        for col, enc, ancho in zip(columnas, encabezados, anchos):
            self.tabla.heading(col, text=enc)
            self.tabla.column(col, width=ancho, anchor="center")

        scroll = ttk.Scrollbar(marco_tabla, orient="vertical",
                               command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll.set)
        self.tabla.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

    def _cargar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        for a in alquiler_datos.buscar_alquileres_cliente(self.id_cliente):
            self.tabla.insert("", "end", values=(
                a.get("id_alquiler"),  a.get("id_vehiculo"),
                a.get("fecha_inicio"), a.get("fecha_fin"),
                a.get("cantidad_dias"),
                f"₡{a.get('total', 0):,.2f}", a.get("estado")
            ))


# ── Punto de entrada temporal ───────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaAlquileres(root)
    root.mainloop()