import tkinter as tk
from tkinter import messagebox, ttk
import logica.devolucion_logica as devolucion_logica
import datos.alquiler_datos as alquiler_datos


class VentanaDevoluciones:
    """Formulario para procesar la devolución de un vehículo"""

    def __init__(self, root):
        self.root = root
        self.root.title("Devolución de Vehículo")
        self.root.geometry("520x600")
        self.root.resizable(False, False)

        self._construir_interfaz()
        self._cargar_alquileres_activos()

    def _construir_interfaz(self):
        tk.Label(self.root, text="Devolución de Vehículo",
                 font=("Arial", 14, "bold")).pack(pady=(15, 5))

        # ── Tabla de alquileres en préstamo ─────────
        marco_tabla = tk.LabelFrame(self.root,
                                    text="Alquileres en préstamo (seleccione uno)",
                                    padx=8, pady=8)
        marco_tabla.pack(fill="x", padx=15, pady=5)

        columnas = ("id_alquiler", "id_cliente", "id_vehiculo", "fecha_fin")
        self.tabla = ttk.Treeview(marco_tabla, columns=columnas,
                                  show="headings", height=4)

        encabezados = ("ID Alquiler", "ID Cliente", "ID Vehículo", "Fecha fin pactada")
        anchos = (100, 100, 100, 130)
        for col, enc, ancho in zip(columnas, encabezados, anchos):
            self.tabla.heading(col, text=enc)
            self.tabla.column(col, width=ancho, anchor="center")

        self.tabla.pack(fill="x")
        self.tabla.bind("<<TreeviewSelect>>", self._seleccionar_alquiler)

        # ── Formulario de devolución ────────────
        marco_form = tk.LabelFrame(self.root, text="Datos de la devolución",
                                   padx=12, pady=10)
        marco_form.pack(fill="x", padx=15, pady=8)

        # ID Alquiler 
        tk.Label(marco_form, text="ID Alquiler:", anchor="e", width=16).grid(
            row=0, column=0, sticky="e", pady=5)
        self.entry_id_alquiler = tk.Entry(marco_form, width=25, state="disabled")
        self.entry_id_alquiler.grid(row=0, column=1, pady=5, padx=5)

        # Fecha de devolución
        tk.Label(marco_form, text="Fecha devolución:", anchor="e", width=16).grid(
            row=1, column=0, sticky="e", pady=5)
        self.entry_fecha = tk.Entry(marco_form, width=25)
        self.entry_fecha.grid(row=1, column=1, pady=5, padx=5)
        tk.Label(marco_form, text="(YYYY-MM-DD)", font=("Arial", 8),
                 fg="gray").grid(row=1, column=2, sticky="w")

        # Seguro diario
        tk.Label(marco_form, text="Seguro diario:", anchor="e", width=16).grid(
            row=2, column=0, sticky="e", pady=5)
        self.entry_seguro = tk.Entry(marco_form, width=25)
        self.entry_seguro.grid(row=2, column=1, pady=5, padx=5)

        # daños checkbox
        self.var_danos = tk.BooleanVar()
        tk.Checkbutton(marco_form, text="¿El vehículo tiene daños?",
                       variable=self.var_danos,
                       command=self._toggle_danos).grid(
            row=3, column=0, columnspan=2, sticky="w", pady=5)

        # Descripción del daño
        tk.Label(marco_form, text="Descripción daño:", anchor="e", width=16).grid(
            row=4, column=0, sticky="e", pady=5)
        self.entry_descripcion = tk.Entry(marco_form, width=25, state="disabled")
        self.entry_descripcion.grid(row=4, column=1, pady=5, padx=5)

        # Costo del daño
        tk.Label(marco_form, text="Costo daño:", anchor="e", width=16).grid(
            row=5, column=0, sticky="e", pady=5)
        self.entry_costo_dano = tk.Entry(marco_form, width=25, state="disabled")
        self.entry_costo_dano.grid(row=5, column=1, pady=5, padx=5)

        # Botón procesar
        tk.Button(self.root, text="Procesar Devolución", width=22,
                  command=self._procesar).pack(pady=10)

        # ── Resumen ─────────────────
        self.marco_resumen = tk.LabelFrame(self.root, text="Resumen de cobros",
                                           padx=10, pady=8)
        self.marco_resumen.pack(fill="x", padx=15, pady=5)

        self.lbl_retraso  = tk.Label(self.marco_resumen, text="Días de retraso: -")
        self.lbl_interes  = tk.Label(self.marco_resumen, text="Interés (15%): -")
        self.lbl_impuesto = tk.Label(self.marco_resumen, text="Impuesto (13%): -")
        self.lbl_seguro   = tk.Label(self.marco_resumen, text="Seguro mora: -")
        self.lbl_danos    = tk.Label(self.marco_resumen, text="Costo daños: -")
        self.lbl_total    = tk.Label(self.marco_resumen, text="TOTAL A COBRAR: -",
                                     font=("Arial", 10, "bold"))

        for lbl in [self.lbl_retraso, self.lbl_interes, self.lbl_impuesto,
                    self.lbl_seguro, self.lbl_danos, self.lbl_total]:
            lbl.pack(anchor="w")

    # ── Lógica de la interfaz ──────────

    def _cargar_alquileres_activos(self):
        """Carga solo los alquileres en estado 'en prestamo'."""
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        for a in alquiler_datos.obtener_todos_los_alquileres():
            if a.get("estado") == "en prestamo":
                self.tabla.insert("", "end", values=(
                    a.get("id_alquiler"), a.get("id_cliente"),
                    a.get("id_vehiculo"), a.get("fecha_fin")
                ))

    def _seleccionar_alquiler(self, event):
        """Al seleccionar una fila llena el campo ID Alquiler automáticamente"""
        seleccion = self.tabla.selection()
        if not seleccion:
            return
        id_alquiler = self.tabla.item(seleccion[0])["values"][0]
        self.entry_id_alquiler.config(state="normal")
        self.entry_id_alquiler.delete(0, tk.END)
        self.entry_id_alquiler.insert(0, str(id_alquiler))
        self.entry_id_alquiler.config(state="disabled")

    def _toggle_danos(self):
        """Habilita o deshabilita los campos de daño según el checkbox"""
        if self.var_danos.get():
            self.entry_descripcion.config(state="normal")
            self.entry_costo_dano.config(state="normal")
        else:
            self.entry_descripcion.config(state="disabled")
            self.entry_descripcion.delete(0, tk.END)
            self.entry_costo_dano.config(state="disabled")
            self.entry_costo_dano.delete(0, tk.END)

    def _procesar(self):
        try:
            id_alquiler  = self.entry_id_alquiler.get().strip()
            fecha        = self.entry_fecha.get().strip()
            seguro       = float(self.entry_seguro.get().strip())
            hay_danos    = self.var_danos.get()
            descripcion  = self.entry_descripcion.get().strip() if hay_danos else ""
            costo_danos  = float(self.entry_costo_dano.get().strip()) if hay_danos else 0.0

            if not id_alquiler:
                messagebox.showwarning("Atención",
                                       "Seleccione un alquiler de la tabla.")
                return

            resultado = devolucion_logica.procesar_devolucion(
                id_alquiler, fecha, hay_danos, descripcion, costo_danos, seguro
            )

            # Mostrar resumen
            self.lbl_retraso.config(
                text=f"Días de retraso: {resultado['dias_retraso']}")
            self.lbl_interes.config(
                text=f"Interés (15%): ₡{resultado['interes']:,.2f}")
            self.lbl_impuesto.config(
                text=f"Impuesto (13%): ₡{resultado['impuesto_mora']:,.2f}")
            self.lbl_seguro.config(
                text=f"Seguro mora: ₡{resultado['seguro_mora']:,.2f}")
            self.lbl_danos.config(
                text=f"Costo daños: ₡{resultado['costo_danos']:,.2f}")
            self.lbl_total.config(
                text=f"TOTAL A COBRAR: ₡{resultado['total']:,.2f}")

            messagebox.showinfo(
                "Devolución procesada",
                f"Devolución registrada correctamente.\n"
                f"ID: {resultado['id_devolucion']}\n"
                f"El vehículo queda disponible nuevamente."
            )

            # Recargar tabla y limpiar formulario
            self._cargar_alquileres_activos()
            self._limpiar()

        except ValueError as e:
            messagebox.showerror("Error de validación", str(e))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _limpiar(self):
        self.entry_id_alquiler.config(state="normal")
        self.entry_id_alquiler.delete(0, tk.END)
        self.entry_id_alquiler.config(state="disabled")
        self.entry_fecha.delete(0, tk.END)
        self.entry_seguro.delete(0, tk.END)
        self.var_danos.set(False)
        self._toggle_danos()


# ── Punto de entrada temporal ─────────
if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaDevoluciones(root)
    root.mainloop()