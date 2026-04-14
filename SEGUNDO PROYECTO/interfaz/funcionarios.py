# interfaz/funcionarios.py
import tkinter as tk
from tkinter import messagebox, ttk
import logica.funcionario_logica as funcionario_logica


class VentanaFuncionarios:
    """Gestión completa de funcionarios (solo funcionario con permisos)."""

    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Funcionarios")
        self.root.geometry("750x520")
        self.root.resizable(False, False)

        self._construir_interfaz()
        self._cargar_tabla()

    def _construir_interfaz(self):
        tk.Label(self.root, text="Gestión de Funcionarios",
                 font=("Arial", 14, "bold")).pack(pady=(10, 5))

        # ── Formulario ──────────────────────────────────────────
        marco_form = tk.LabelFrame(self.root, text="Datos del funcionario",
                                   padx=10, pady=10)
        marco_form.pack(fill="x", padx=15, pady=5)

        campos = [
            ("ID Funcionario", "entry_id"),
            ("Nombre",         "entry_nombre"),
            ("Cédula",         "entry_cedula"),
            ("Teléfono",       "entry_telefono"),
            ("Correo",         "entry_correo"),
            ("Puesto",         "entry_puesto"),
        ]

        for i, (etiqueta, atributo) in enumerate(campos):
            fila   = i // 2
            columna = (i % 2) * 2
            tk.Label(marco_form, text=etiqueta + ":").grid(
                row=fila, column=columna, sticky="e", padx=5, pady=4)
            entry = tk.Entry(marco_form, width=25)
            entry.grid(row=fila, column=columna + 1, padx=5, pady=4)
            setattr(self, atributo, entry)

        # ── Botones ─────────────────────────────────────────────
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

        # ── Tabla ───────────────────────────────────────────────
        marco_tabla = tk.Frame(self.root)
        marco_tabla.pack(fill="both", expand=True, padx=15, pady=5)

        columnas = ("id", "nombre", "cedula", "telefono", "correo", "puesto", "estado")
        self.tabla = ttk.Treeview(marco_tabla, columns=columnas,
                                  show="headings", height=8)

        encabezados = ("ID",  "Nombre", "Cédula", "Teléfono", "Correo", "Puesto", "Estado")
        anchos      = (80,    150,      90,       90,         150,      100,      70)
        for col, enc, ancho in zip(columnas, encabezados, anchos):
            self.tabla.heading(col, text=enc)
            self.tabla.column(col, width=ancho, anchor="center")

        scroll = ttk.Scrollbar(marco_tabla, orient="vertical",
                               command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll.set)
        self.tabla.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        self.tabla.bind("<<TreeviewSelect>>", self._seleccionar_fila)

    # ── Lógica de la interfaz ───────────────────────────────────

    def _cargar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        for f in funcionario_logica.obtener_todos_los_funcionarios():
            self.tabla.insert("", "end", values=(
                f.get("id_funcionario"), f.get("nombre"),   f.get("cedula"),
                f.get("telefono"),       f.get("correo"),   f.get("puesto"),
                f.get("estado")
            ))

    def _seleccionar_fila(self, event):
        seleccion = self.tabla.selection()
        if not seleccion:
            return
        valores = self.tabla.item(seleccion[0])["values"]
        entries = [self.entry_id, self.entry_nombre, self.entry_cedula,
                   self.entry_telefono, self.entry_correo, self.entry_puesto]
        for entry, valor in zip(entries, valores[:6]):
            entry.config(state="normal")
            entry.delete(0, tk.END)
            entry.insert(0, str(valor))
        self.entry_id.config(state="disabled")  # el ID no se edita

    def _agregar(self):
        try:
            funcionario_logica.crear_funcionario(
                self.entry_id.get().strip(),
                self.entry_nombre.get().strip(),
                self.entry_cedula.get().strip(),
                self.entry_telefono.get().strip(),
                self.entry_correo.get().strip(),
                self.entry_puesto.get().strip()
            )
            messagebox.showinfo("Éxito", "Funcionario agregado correctamente.")
            self._limpiar()
            self._cargar_tabla()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _modificar(self):
        id_funcionario = self.entry_id.get().strip()
        if not id_funcionario:
            messagebox.showwarning("Atención", "Seleccione un funcionario de la tabla.")
            return
        nuevos_datos = {}
        if self.entry_nombre.get().strip():
            nuevos_datos["nombre"]   = self.entry_nombre.get().strip()
        if self.entry_telefono.get().strip():
            nuevos_datos["telefono"] = self.entry_telefono.get().strip()
        if self.entry_correo.get().strip():
            nuevos_datos["correo"]   = self.entry_correo.get().strip()
        if self.entry_puesto.get().strip():
            nuevos_datos["puesto"]   = self.entry_puesto.get().strip()
        if not nuevos_datos:
            messagebox.showwarning("Atención", "No hay datos para modificar.")
            return
        try:
            funcionario_logica.actualizar_funcionario(id_funcionario, nuevos_datos)
            messagebox.showinfo("Éxito", "Funcionario actualizado correctamente.")
            self._limpiar()
            self._cargar_tabla()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _desactivar(self):
        id_funcionario = self.entry_id.get().strip()
        if not id_funcionario:
            messagebox.showwarning("Atención", "Seleccione un funcionario de la tabla.")
            return
        if messagebox.askyesno("Confirmar",
                               f"¿Desactivar el funcionario {id_funcionario}?"):
            try:
                funcionario_logica.eliminar_funcionario(id_funcionario)
                messagebox.showinfo("Éxito", "Funcionario desactivado.")
                self._limpiar()
                self._cargar_tabla()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def _limpiar(self):
        for entry in [self.entry_id, self.entry_nombre, self.entry_cedula,
                      self.entry_telefono, self.entry_correo, self.entry_puesto]:
            entry.config(state="normal")
            entry.delete(0, tk.END)


# ── Punto de entrada temporal ───────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaFuncionarios(root)
    root.mainloop()