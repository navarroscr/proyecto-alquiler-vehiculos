# interfaz/vehiculos.py
import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from datetime import datetime
import logica.vehiculo_logica as vehiculo_logica
import logica.alquiler_logica as alquiler_logica


# ============================================
# VENTANA COMPLETA — para el funcionario
# ============================================

class VentanaVehiculos:
    """Gestion completa de vehiculos (solo funcionario)"""

    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de Vehiculos")
        self.root.geometry("900x580")
        self.root.resizable(False, False)

        self._construir_interfaz()
        self._cargar_tabla()

    def _construir_interfaz(self):
        tk.Label(self.root, text="Gestion de Vehiculos",
                 font=("Arial", 14, "bold")).pack(pady=(10, 5))

        # Formulario
        marco_form = tk.LabelFrame(self.root, text="Datos del vehiculo",
                                   padx=10, pady=10)
        marco_form.pack(fill="x", padx=15, pady=5)

        # Fila 0
        tk.Label(marco_form, text="ID Vehiculo:").grid(
            row=0, column=0, sticky="e", padx=5, pady=3)
        self.entry_id = tk.Entry(marco_form, width=20)
        self.entry_id.grid(row=0, column=1, padx=5, pady=3)

        tk.Label(marco_form, text="Marca:").grid(
            row=0, column=2, sticky="e", padx=5, pady=3)
        self.entry_marca = tk.Entry(marco_form, width=20)
        self.entry_marca.grid(row=0, column=3, padx=5, pady=3)

        tk.Label(marco_form, text="Tipo:").grid(
            row=0, column=4, sticky="e", padx=5, pady=3)
        self.combo_tipo = ttk.Combobox(marco_form, width=17, state="readonly",
                                       values=["automovil", "SUV", "pickup", "VAN"])
        self.combo_tipo.grid(row=0, column=5, padx=5, pady=3)

        # Fila 1
        tk.Label(marco_form, text="Placa:").grid(
            row=1, column=0, sticky="e", padx=5, pady=3)
        self.entry_placa = tk.Entry(marco_form, width=20)
        self.entry_placa.grid(row=1, column=1, padx=5, pady=3)

        tk.Label(marco_form, text="N° Motor:").grid(
            row=1, column=2, sticky="e", padx=5, pady=3)
        self.entry_motor = tk.Entry(marco_form, width=20)
        self.entry_motor.grid(row=1, column=3, padx=5, pady=3)

        tk.Label(marco_form, text="Transmision:").grid(
            row=1, column=4, sticky="e", padx=5, pady=3)
        self.combo_transmision = ttk.Combobox(marco_form, width=17, state="readonly",
                                              values=["manual", "automatico"])
        self.combo_transmision.grid(row=1, column=5, padx=5, pady=3)

        # Fila 2
        tk.Label(marco_form, text="Combustible:").grid(
            row=2, column=0, sticky="e", padx=5, pady=3)
        self.combo_combustible = ttk.Combobox(marco_form, width=17, state="readonly",
                                              values=["gasolina", "diesel", "electrico"])
        self.combo_combustible.grid(row=2, column=1, padx=5, pady=3)

        tk.Label(marco_form, text="Color:").grid(
            row=2, column=2, sticky="e", padx=5, pady=3)
        self.entry_color = tk.Entry(marco_form, width=20)
        self.entry_color.grid(row=2, column=3, padx=5, pady=3)

        tk.Label(marco_form, text="Pasajeros:").grid(
            row=2, column=4, sticky="e", padx=5, pady=3)
        self.entry_pasajeros = tk.Entry(marco_form, width=18)
        self.entry_pasajeros.grid(row=2, column=5, padx=5, pady=3)

        # Fila 3
        tk.Label(marco_form, text="Costo diario:").grid(
            row=3, column=0, sticky="e", padx=5, pady=3)
        self.entry_costo = tk.Entry(marco_form, width=20)
        self.entry_costo.grid(row=3, column=1, padx=5, pady=3)

        tk.Label(marco_form, text="Maletas:").grid(
            row=3, column=2, sticky="e", padx=5, pady=3)
        self.entry_maletas = tk.Entry(marco_form, width=20)
        self.entry_maletas.grid(row=3, column=3, padx=5, pady=3)

        # Imagen con boton para explorar archivo
        tk.Label(marco_form, text="Imagen (ruta):").grid(
            row=3, column=4, sticky="e", padx=5, pady=3)
        marco_img = tk.Frame(marco_form)
        marco_img.grid(row=3, column=5, padx=5, pady=3)
        self.entry_imagen = tk.Entry(marco_img, width=13)
        self.entry_imagen.pack(side="left")
        tk.Button(marco_img, text="...", width=3,
                  command=self._explorar_imagen).pack(side="left", padx=2)

        # Botones
        marco_botones = tk.Frame(self.root)
        marco_botones.pack(pady=6)

        tk.Button(marco_botones, text="Agregar",    width=12,
                  command=self._agregar).grid(row=0, column=0, padx=5)
        tk.Button(marco_botones, text="Modificar",  width=12,
                  command=self._modificar).grid(row=0, column=1, padx=5)
        tk.Button(marco_botones, text="Desactivar", width=12,
                  command=self._desactivar).grid(row=0, column=2, padx=5)
        tk.Button(marco_botones, text="Limpiar",    width=12,
                  command=self._limpiar).grid(row=0, column=3, padx=5)

        # Tabla
        marco_tabla = tk.Frame(self.root)
        marco_tabla.pack(fill="both", expand=True, padx=15, pady=5)

        columnas = ("id", "marca", "tipo", "placa", "transmision",
                    "combustible", "color", "pasajeros", "costo", "estado")
        self.tabla = ttk.Treeview(marco_tabla, columns=columnas,
                                  show="headings", height=7)

        encabezados = ("ID", "Marca", "Tipo", "Placa", "Transmision",
                       "Combustible", "Color", "Pasajeros", "Costo/dia", "Estado")
        anchos = (60, 80, 70, 80, 90, 80, 70, 70, 70, 80)
        for col, enc, ancho in zip(columnas, encabezados, anchos):
            self.tabla.heading(col, text=enc)
            self.tabla.column(col, width=ancho, anchor="center")

        scroll = ttk.Scrollbar(marco_tabla, orient="vertical",
                               command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll.set)
        self.tabla.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        self.tabla.bind("<<TreeviewSelect>>", self._seleccionar_fila)

    def _cargar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        for v in vehiculo_logica.obtener_todos_los_vehiculos():
            self.tabla.insert("", "end", values=(
                v.get("id_vehiculo"),  v.get("marca"),       v.get("tipo"),
                v.get("placa"),        v.get("transmision"),  v.get("combustible"),
                v.get("color"),        v.get("cantidad_pasajeros"),
                v.get("costo_diario"), v.get("estado")
            ))

    def _seleccionar_fila(self, event):
        seleccion = self.tabla.selection()
        if not seleccion:
            return
        id_vehiculo = self.tabla.item(seleccion[0])["values"][0]
        v = vehiculo_logica.buscar_vehiculo(str(id_vehiculo))
        if not v:
            return

        campos = [
            (self.entry_id,           v.get("id_vehiculo", "")),
            (self.entry_marca,        v.get("marca", "")),
            (self.entry_placa,        v.get("placa", "")),
            (self.entry_motor,        v.get("numero_motor", "")),
            (self.entry_color,        v.get("color", "")),
            (self.entry_pasajeros,    str(v.get("cantidad_pasajeros", ""))),
            (self.entry_costo,        str(v.get("costo_diario", ""))),
            (self.entry_maletas,      str(v.get("cantidad_maletas", ""))),
            (self.entry_imagen,       v.get("imagen", "")),
        ]
        for entry, valor in campos:
            entry.config(state="normal")
            entry.delete(0, tk.END)
            entry.insert(0, valor)
        self.entry_id.config(state="disabled")

        self.combo_tipo.set(v.get("tipo", ""))
        self.combo_transmision.set(v.get("transmision", ""))
        self.combo_combustible.set(v.get("combustible", ""))

    def _explorar_imagen(self):
        ruta = filedialog.askopenfilename(
            title="Seleccionar imagen",
            filetypes=[("Imagenes", "*.png *.jpg *.jpeg *.gif *.bmp")]
        )
        if ruta:
            self.entry_imagen.delete(0, tk.END)
            self.entry_imagen.insert(0, ruta)

    def _agregar(self):
        try:
            vehiculo_logica.crear_vehiculo(
                self.entry_id.get().strip(),
                self.entry_marca.get().strip(),
                self.combo_tipo.get().strip(),
                self.entry_placa.get().strip(),
                self.entry_motor.get().strip(),
                self.combo_transmision.get().strip(),
                self.combo_combustible.get().strip(),
                self.entry_color.get().strip(),
                int(self.entry_pasajeros.get().strip()),
                float(self.entry_costo.get().strip()),
                int(self.entry_maletas.get().strip()),
                self.entry_imagen.get().strip()
            )
            messagebox.showinfo("Exito", "Vehiculo agregado correctamente.")
            self._limpiar()
            self._cargar_tabla()
        except ValueError as e:
            messagebox.showerror("Error de validacion", str(e))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _modificar(self):
        id_vehiculo = self.entry_id.get().strip()
        if not id_vehiculo:
            messagebox.showwarning("Atencion", "Seleccione un vehiculo de la tabla.")
            return
        nuevos_datos = {}
        if self.entry_marca.get().strip():
            nuevos_datos["marca"]    = self.entry_marca.get().strip()
        if self.entry_color.get().strip():
            nuevos_datos["color"]    = self.entry_color.get().strip()
        if self.entry_costo.get().strip():
            nuevos_datos["costo_diario"] = float(self.entry_costo.get().strip())
        if self.entry_imagen.get().strip():
            nuevos_datos["imagen"]   = self.entry_imagen.get().strip()
        if self.combo_tipo.get().strip():
            nuevos_datos["tipo"]     = self.combo_tipo.get().strip()
        if self.combo_transmision.get().strip():
            nuevos_datos["transmision"] = self.combo_transmision.get().strip()
        if self.combo_combustible.get().strip():
            nuevos_datos["combustible"] = self.combo_combustible.get().strip()

        if not nuevos_datos:
            messagebox.showwarning("Atencion", "No hay datos para modificar.")
            return
        try:
            vehiculo_logica.actualizar_vehiculo(id_vehiculo, nuevos_datos)
            messagebox.showinfo("Exito", "Vehiculo actualizado correctamente.")
            self._limpiar()
            self._cargar_tabla()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _desactivar(self):
        id_vehiculo = self.entry_id.get().strip()
        if not id_vehiculo:
            messagebox.showwarning("Atencion", "Seleccione un vehiculo de la tabla.")
            return
        if messagebox.askyesno("Confirmar",
                               f"Desactivar el vehiculo {id_vehiculo}?"):
            try:
                vehiculo_logica.eliminar_vehiculo(id_vehiculo)
                messagebox.showinfo("Exito", "Vehiculo desactivado.")
                self._limpiar()
                self._cargar_tabla()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def _limpiar(self):
        for entry in [self.entry_id, self.entry_marca, self.entry_placa,
                      self.entry_motor, self.entry_color, self.entry_pasajeros,
                      self.entry_costo, self.entry_maletas, self.entry_imagen]:
            entry.config(state="normal")
            entry.delete(0, tk.END)
        self.combo_tipo.set("")
        self.combo_transmision.set("")
        self.combo_combustible.set("")


# ============================================
# VENTANA SOLO LECTURA — para el cliente (CON FILTRO DE FECHAS)
# ============================================

class VentanaVehiculosDisponibles:
    """El cliente puede ver los vehiculos disponibles filtrando por fechas."""

    def __init__(self, root):
        self.root = root
        self.root.title("Vehiculos Disponibles")
        self.root.geometry("850x520")
        self.root.resizable(False, False)

        self._construir_interfaz()
        self._cargar_tabla()

    def _construir_interfaz(self):
        tk.Label(self.root, text="Vehiculos Disponibles",
                 font=("Arial", 14, "bold")).pack(pady=(10, 5))

        # Filtro de fechas
        marco_filtro = tk.LabelFrame(self.root, text="Filtrar por fechas",
                                     padx=10, pady=8)
        marco_filtro.pack(fill="x", padx=15, pady=5)

        frame_fechas = tk.Frame(marco_filtro)
        frame_fechas.pack(pady=5)

        tk.Label(frame_fechas, text="Fecha inicio:", font=("Arial", 10)).grid(row=0, column=0, padx=5)
        self.entry_fecha_inicio = tk.Entry(frame_fechas, width=12, font=("Arial", 10))
        self.entry_fecha_inicio.grid(row=0, column=1, padx=5)
        self.entry_fecha_inicio.insert(0, datetime.now().strftime("%Y-%m-%d"))

        tk.Label(frame_fechas, text="Fecha fin:", font=("Arial", 10)).grid(row=0, column=2, padx=5)
        self.entry_fecha_fin = tk.Entry(frame_fechas, width=12, font=("Arial", 10))
        self.entry_fecha_fin.grid(row=0, column=3, padx=5)
        self.entry_fecha_fin.insert(0, datetime.now().strftime("%Y-%m-%d"))

        tk.Label(marco_filtro, text="(Formato: YYYY-MM-DD)",
                 font=("Arial", 8), fg="gray").pack(pady=(0, 5))

        # Botones
        marco_botones = tk.Frame(marco_filtro)
        marco_botones.pack(pady=5)

        tk.Button(marco_botones, text="Buscar disponibles", width=18,
                  command=self._cargar_tabla).grid(row=0, column=0, padx=5)
        tk.Button(marco_botones, text="Mostrar todos disponibles", width=20,
                  command=self._cargar_todos).grid(row=0, column=1, padx=5)

        # Tabla
        marco_tabla = tk.Frame(self.root)
        marco_tabla.pack(fill="both", expand=True, padx=15, pady=5)

        columnas = ("marca", "tipo", "placa", "transmision",
                    "combustible", "color", "pasajeros", "maletas", "costo")
        self.tabla = ttk.Treeview(marco_tabla, columns=columnas,
                                  show="headings", height=12)

        encabezados = ("Marca", "Tipo", "Placa", "Transmision",
                       "Combustible", "Color", "Pasajeros", "Maletas", "Costo/dia")
        anchos = (80, 70, 80, 90, 80, 70, 70, 65, 80)
        for col, enc, ancho in zip(columnas, encabezados, anchos):
            self.tabla.heading(col, text=enc)
            self.tabla.column(col, width=ancho, anchor="center")

        scroll = ttk.Scrollbar(marco_tabla, orient="vertical",
                               command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll.set)
        self.tabla.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

    def _cargar_tabla(self):
        """Carga los vehiculos disponibles en el rango de fechas seleccionado."""
        try:
            fecha_inicio_str = self.entry_fecha_inicio.get().strip()
            fecha_fin_str = self.entry_fecha_fin.get().strip()

            if not fecha_inicio_str or not fecha_fin_str:
                messagebox.showwarning("Atencion", "Complete ambas fechas.")
                return

            # Validar formato de fechas
            try:
                fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d").date()
                fecha_fin = datetime.strptime(fecha_fin_str, "%Y-%m-%d").date()
            except ValueError:
                messagebox.showerror("Error", "Formato de fecha invalido. Use YYYY-MM-DD")
                return

            # Validar que la fecha fin no sea menor a la fecha inicio
            if fecha_fin < fecha_inicio:
                messagebox.showwarning("Atencion", "La fecha fin no puede ser menor a la fecha inicio.")
                return

            # Validar que no sean fechas pasadas
            hoy = datetime.now().date()
            if fecha_inicio < hoy:
                messagebox.showwarning("Atencion", "La fecha de inicio no puede ser anterior a hoy.")
                return

            # Limpiar tabla
            for fila in self.tabla.get_children():
                self.tabla.delete(fila)

            # Obtener todos los vehiculos disponibles
            todos_vehiculos = vehiculo_logica.obtener_vehiculos_disponibles()

            # Filtrar por disponibilidad en el rango de fechas
            vehiculos_filtrados = []
            for v in todos_vehiculos:
                id_vehiculo = v.get("id_vehiculo")
                # Verificar si el vehiculo esta disponible en el rango de fechas
                if alquiler_logica.verificar_disponibilidad_vehiculo(id_vehiculo, fecha_inicio_str, fecha_fin_str):
                    vehiculos_filtrados.append(v)

            if not vehiculos_filtrados:
                messagebox.showinfo("Sin resultados",
                                    f"No hay vehiculos disponibles del {fecha_inicio_str} al {fecha_fin_str}.")
                return

            # Mostrar vehiculos filtrados
            for v in vehiculos_filtrados:
                self.tabla.insert("", "end", values=(
                    v.get("marca"),              v.get("tipo"),
                    v.get("placa"),              v.get("transmision"),
                    v.get("combustible"),        v.get("color"),
                    v.get("cantidad_pasajeros"), v.get("cantidad_maletas"),
                    v.get("costo_diario")
                ))

        except Exception as e:
            messagebox.showerror("Error", f"Error al buscar vehiculos: {str(e)}")

    def _cargar_todos(self):
        """Muestra todos los vehiculos disponibles sin filtro de fechas."""
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        for v in vehiculo_logica.obtener_vehiculos_disponibles():
            self.tabla.insert("", "end", values=(
                v.get("marca"),              v.get("tipo"),
                v.get("placa"),              v.get("transmision"),
                v.get("combustible"),        v.get("color"),
                v.get("cantidad_pasajeros"), v.get("cantidad_maletas"),
                v.get("costo_diario")
            ))


# Punto de entrada temporal
if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaVehiculos(root)
    root.mainloop()