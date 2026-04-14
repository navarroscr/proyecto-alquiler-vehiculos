# interfaz/reportes.py
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, date
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datos.alquiler_datos as alquiler_datos
import datos.vehiculo_datos as vehiculo_datos
import datos.clientes_datos as clientes_datos


class VentanaReportes:
    """Ventana de reportes con dos gráficos: barras y líneas."""

    def __init__(self, root):
        self.root = root
        self.root.title("Reportes - AutoTrust S.A.")
        self.root.geometry("420x280")
        self.root.resizable(False, False)

        self._construir_interfaz()

    def _construir_interfaz(self):
        tk.Label(self.root, text="Reportes",
                 font=("Arial", 14, "bold")).pack(pady=(20, 10))

        # ── Reporte 1: Vehículos más rentados ───────────────────
        marco1 = tk.LabelFrame(self.root,
                               text="Reporte 1: Vehículos más rentados",
                               padx=10, pady=8)
        marco1.pack(fill="x", padx=20, pady=8)

        marco_fechas = tk.Frame(marco1)
        marco_fechas.pack()

        tk.Label(marco_fechas, text="Desde:").grid(row=0, column=0, padx=5)
        self.entry_desde = tk.Entry(marco_fechas, width=12)
        self.entry_desde.grid(row=0, column=1, padx=5)
        self.entry_desde.insert(0, "2024-01-01")

        tk.Label(marco_fechas, text="Hasta:").grid(row=0, column=2, padx=5)
        self.entry_hasta = tk.Entry(marco_fechas, width=12)
        self.entry_hasta.grid(row=0, column=3, padx=5)
        self.entry_hasta.insert(0, datetime.now().strftime("%Y-%m-%d"))

        tk.Label(marco_fechas, text="(YYYY-MM-DD)",
                 font=("Arial", 8), fg="gray").grid(
            row=1, column=0, columnspan=4, pady=2)

        tk.Button(marco1, text="Generar gráfico de barras", width=28,
                  command=self._reporte_vehiculos).pack(pady=(6, 2))

        # ── Reporte 2: Segmentación por edad ────────────────────
        marco2 = tk.LabelFrame(self.root,
                               text="Reporte 2: Segmentación de clientes por edad",
                               padx=10, pady=8)
        marco2.pack(fill="x", padx=20, pady=8)

        marco_anio = tk.Frame(marco2)
        marco_anio.pack()

        tk.Label(marco_anio, text="Año:").grid(row=0, column=0, padx=5)
        self.entry_anio = tk.Entry(marco_anio, width=8)
        self.entry_anio.grid(row=0, column=1, padx=5)
        self.entry_anio.insert(0, str(datetime.now().year))

        tk.Button(marco2, text="Generar gráfico de líneas", width=28,
                  command=self._reporte_edades).pack(pady=(6, 2))

    # ══════════════════════════════════════════════════════════
    #  REPORTE 1 — Vehículos más rentados (barras)
    # ══════════════════════════════════════════════════════════

    def _reporte_vehiculos(self):
        try:
            desde_str = self.entry_desde.get().strip()
            hasta_str = self.entry_hasta.get().strip()
            desde = datetime.strptime(desde_str, "%Y-%m-%d").date()
            hasta = datetime.strptime(hasta_str, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha inválido. Use YYYY-MM-DD.")
            return

        # Obtener todos los alquileres y filtrar por rango de fechas
        alquileres = alquiler_datos.obtener_todos_los_alquileres()
        conteo = {}  # id_vehiculo → cantidad de alquileres

        for a in alquileres:
            try:
                fecha_inicio = a.get("fecha_inicio")
                if isinstance(fecha_inicio, str):
                    fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
                elif hasattr(fecha_inicio, "date"):
                    fecha_inicio = fecha_inicio.date()

                if desde <= fecha_inicio <= hasta:
                    id_v = str(a.get("id_vehiculo", ""))
                    conteo[id_v] = conteo.get(id_v, 0) + 1
            except Exception:
                continue

        if not conteo:
            messagebox.showinfo("Sin datos",
                                "No hay alquileres en el rango de fechas indicado.")
            return

        # Obtener nombre del modelo para cada vehículo
        etiquetas = []
        valores   = []
        for id_v, cantidad in sorted(conteo.items(),
                                     key=lambda x: x[1], reverse=True):
            vehiculo = vehiculo_datos.buscar_vehiculo_por_id(id_v)
            if vehiculo:
                nombre = f"{vehiculo.get('marca', '')} {vehiculo.get('tipo', '')}"
            else:
                nombre = id_v
            etiquetas.append(nombre)
            valores.append(cantidad)

        # Calcular porcentajes
        total_alquileres = sum(valores)
        porcentajes = [(v / total_alquileres) * 100 for v in valores]

        # Crear ventana del gráfico
        ventana_graf = tk.Toplevel(self.root)
        ventana_graf.title("Vehículos más rentados")
        ventana_graf.geometry("700x480")

        fig, ax = plt.subplots(figsize=(9, 5))
        barras = ax.barh(etiquetas, valores, color="steelblue")

        # Mostrar porcentaje al lado de cada barra
        for barra, pct in zip(barras, porcentajes):
            ax.text(barra.get_width() + 0.1, barra.get_y() + barra.get_height() / 2,
                    f"{pct:.1f}%", va="center", fontsize=9)

        ax.set_xlabel("Total de alquileres")
        ax.set_title(f"Vehículos más rentados\n({desde_str} al {hasta_str})")
        ax.invert_yaxis()  # el más rentado arriba
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=ventana_graf)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    # ══════════════════════════════════════════════════════════
    #  REPORTE 2 — Segmentación por edad (líneas)
    # ══════════════════════════════════════════════════════════

    def _reporte_edades(self):
        try:
            anio = int(self.entry_anio.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Ingrese un año válido (ej: 2025).")
            return

        # Rangos de edad según instrucciones del proyecto
        rangos = [
            (18, 19, "18-19"),
            (20, 24, "20-24"),
            (25, 29, "25-29"),
            (30, 34, "30-34"),
            (35, 39, "35-39"),
            (40, 44, "40-44"),
            (45, 49, "45-49"),
            (50, 54, "50-54"),
            (55, 59, "55-59"),
            (60, 99, "60+"),
        ]

        # Obtener todos los alquileres del año indicado
        alquileres = alquiler_datos.obtener_todos_los_alquileres()
        alquileres_anio = []
        for a in alquileres:
            try:
                fecha_inicio = a.get("fecha_inicio")
                if isinstance(fecha_inicio, str):
                    fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
                elif hasattr(fecha_inicio, "date"):
                    fecha_inicio = fecha_inicio.date()
                if fecha_inicio.year == anio:
                    alquileres_anio.append((a, fecha_inicio))
            except Exception:
                continue

        if not alquileres_anio:
            messagebox.showinfo("Sin datos",
                                f"No hay alquileres registrados para el año {anio}.")
            return

        # Cargar clientes en un diccionario para búsqueda rápida
        clientes = {c.get("id_cliente"): c
                    for c in clientes_datos.obtener_clientes()}

        # Contar alquileres por rango de edad y mes
        # datos[rango_label][mes(1-12)] = cantidad
        datos = {r[2]: [0] * 12 for r in rangos}

        for alquiler, fecha_inicio in alquileres_anio:
            id_cliente = str(alquiler.get("id_cliente", ""))
            cliente = clientes.get(id_cliente)
            if not cliente:
                continue

            # Calcular edad del cliente al momento del alquiler
            nacimiento = cliente.get("fecha_nacimiento")
            if not nacimiento:
                continue
            try:
                if isinstance(nacimiento, str):
                    nacimiento = datetime.strptime(nacimiento, "%Y-%m-%d").date()
                elif hasattr(nacimiento, "date"):
                    nacimiento = nacimiento.date()

                edad = (fecha_inicio - nacimiento).days // 365
            except Exception:
                continue

            # Buscar en qué rango cae
            mes = fecha_inicio.month - 1  # índice 0-11
            for min_e, max_e, etiqueta in rangos:
                if min_e <= edad <= max_e:
                    datos[etiqueta][mes] += 1
                    break

        # Filtrar rangos que tienen al menos un alquiler
        datos_activos = {k: v for k, v in datos.items() if any(v)}

        if not datos_activos:
            messagebox.showinfo("Sin datos",
                                "No hay suficientes datos para generar el reporte.")
            return

        # Crear ventana del gráfico
        ventana_graf = tk.Toplevel(self.root)
        ventana_graf.title(f"Segmentación por edad - {anio}")
        ventana_graf.geometry("750x500")

        meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
                 "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

        fig, ax = plt.subplots(figsize=(10, 5.5))

        for etiqueta, valores in datos_activos.items():
            ax.plot(meses, valores, marker="o", label=etiqueta, linewidth=2)

        ax.set_xlabel("Mes")
        ax.set_ylabel("Cantidad de alquileres")
        ax.set_title(f"Segmentación de clientes por edad - Año {anio}")
        ax.legend(title="Rango de edad", bbox_to_anchor=(1.01, 1), loc="upper left")
        ax.grid(True, linestyle="--", alpha=0.5)
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=ventana_graf)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)


# ── Punto de entrada temporal ───────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaReportes(root)
    root.mainloop()