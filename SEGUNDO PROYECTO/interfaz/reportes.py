import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import logica.reportes_logica as reportes_logica


class VentanaReportes:
    """Ventana de reportes con dos graficos: barras y lineas."""

    def __init__(self, root):
        self.root = root
        self.root.title("Reportes - AutoTrust S.A.")
        self.root.geometry("550x400")
        self.root.resizable(False, False)

        self._construir_interfaz()

    def _construir_interfaz(self):
        # Titulo principal
        tk.Label(self.root, text="AutoTrust S.A.",
                 font=("Arial", 16, "bold")).pack(pady=(15, 5))
        tk.Label(self.root, text="Sistema de Reportes",
                 font=("Arial", 12)).pack(pady=(0, 15))

        # Reporte 1: Vehiculos mas rentados
        marco1 = tk.LabelFrame(self.root,
                               text=" Reporte 1: Vehiculos mas rentados ",
                               padx=10, pady=8,
                               font=("Arial", 11, "bold"))
        marco1.pack(fill="x", padx=20, pady=8)

        # Fila de fechas
        frame_fechas = tk.Frame(marco1)
        frame_fechas.pack(pady=5)

        tk.Label(frame_fechas, text="Desde:", font=("Arial", 10),
                width=6, anchor="e").grid(row=0, column=0, padx=5)
        self.entry_desde = tk.Entry(frame_fechas, width=12, font=("Arial", 10))
        self.entry_desde.grid(row=0, column=1, padx=5)
        self.entry_desde.insert(0, "2024-01-01")

        tk.Label(frame_fechas, text="Hasta:", font=("Arial", 10),
                width=6, anchor="e").grid(row=0, column=2, padx=5)
        self.entry_hasta = tk.Entry(frame_fechas, width=12, font=("Arial", 10))
        self.entry_hasta.grid(row=0, column=3, padx=5)
        self.entry_hasta.insert(0, datetime.now().strftime("%Y-%m-%d"))

        # Formato de fecha
        tk.Label(marco1, text="(Formato: YYYY-MM-DD)",
                 font=("Arial", 8), fg="gray").pack(pady=(0, 5))

        # Boton generar grafico de barras
        tk.Button(marco1, text="Generar grafico de barras",
                  width=30, height=1, font=("Arial", 10, "bold"),
                  bg="#4CAF50", fg="white",
                  command=self._reporte_vehiculos).pack(pady=5)

        # Reporte 2: Segmentacion por edad
        marco2 = tk.LabelFrame(self.root,
                               text=" Reporte 2: Segmentacion de clientes por edad ",
                               padx=10, pady=8,
                               font=("Arial", 11, "bold"))
        marco2.pack(fill="x", padx=20, pady=8)

        frame_anio = tk.Frame(marco2)
        frame_anio.pack(pady=10)

        tk.Label(frame_anio, text="Año:", font=("Arial", 10),
                width=6, anchor="e").grid(row=0, column=0, padx=5)
        self.entry_anio = tk.Entry(frame_anio, width=8, font=("Arial", 10))
        self.entry_anio.grid(row=0, column=1, padx=5)
        self.entry_anio.insert(0, str(datetime.now().year))

        # Boton generar grafico de lineas
        tk.Button(marco2, text="Generar grafico de lineas",
                  width=30, height=1, font=("Arial", 10, "bold"),
                  bg="#2196F3", fg="white",
                  command=self._reporte_edades).pack(pady=5)

    # Reporte 1: Vehiculos mas rentados (grafico de barras)
    def _reporte_vehiculos(self):
        try:
            desde_str = self.entry_desde.get().strip()
            hasta_str = self.entry_hasta.get().strip()

            if not desde_str or not hasta_str:
                messagebox.showwarning("Atencion", "Complete ambas fechas.")
                return

            # Validar formato de fechas
            try:
                datetime.strptime(desde_str, "%Y-%m-%d")
                datetime.strptime(hasta_str, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Error", "Formato de fecha invalido. Use YYYY-MM-DD")
                return

            # Obtener datos desde la logica
            etiquetas, valores, porcentajes = reportes_logica.obtener_vehiculos_mas_rentados(
                desde_str, hasta_str
            )

            if not etiquetas:
                messagebox.showinfo("Sin datos",
                                    "No hay alquileres en el rango de fechas indicado.")
                return

            # Crear ventana del grafico
            ventana_graf = tk.Toplevel(self.root)
            ventana_graf.title("Vehiculos mas rentados - AutoTrust S.A.")
            ventana_graf.geometry("750x550")
            ventana_graf.resizable(True, True)

            # Crear figura de matplotlib
            fig, ax = plt.subplots(figsize=(10, 6))
            barras = ax.barh(etiquetas, valores, color="steelblue")

            # Mostrar porcentaje al lado de cada barra
            for barra, pct in zip(barras, porcentajes):
                ax.text(barra.get_width() + 0.1,
                        barra.get_y() + barra.get_height() / 2,
                        f"{pct:.1f}%", va="center", fontsize=10, fontweight="bold")

            ax.set_xlabel("Total de alquileres", fontsize=11, fontweight="bold")
            ax.set_ylabel("Vehiculos", fontsize=11, fontweight="bold")
            ax.set_title(f"Vehiculos mas rentados\n({desde_str} al {hasta_str})",
                        fontsize=12, fontweight="bold")
            ax.invert_yaxis()
            ax.grid(True, linestyle="--", alpha=0.3)
            fig.tight_layout()

            # Mostrar grafico en la ventana
            canvas = FigureCanvasTkAgg(fig, master=ventana_graf)
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=True)

        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar reporte: {str(e)}")

    # Reporte 2: Segmentacion por edad (grafico de lineas)
    def _reporte_edades(self):
        try:
            anio = self.entry_anio.get().strip()

            if not anio:
                messagebox.showwarning("Atencion", "Ingrese un año.")
                return

            # Validar que sea un año valido
            try:
                anio_int = int(anio)
                if anio_int < 2000 or anio_int > 2100:
                    messagebox.showwarning("Atencion", "Ingrese un año valido (2000-2100).")
                    return
            except ValueError:
                messagebox.showerror("Error", "Ingrese un año valido (ej: 2025).")
                return

            # Obtener datos desde la logica
            datos_activos, meses = reportes_logica.obtener_segmentacion_edades(anio)

            if not datos_activos:
                messagebox.showinfo("Sin datos",
                                    f"No hay alquileres registrados para el año {anio}.")
                return

            # Crear ventana del grafico
            ventana_graf = tk.Toplevel(self.root)
            ventana_graf.title(f"Segmentacion por edad - {anio}")
            ventana_graf.geometry("800x550")
            ventana_graf.resizable(True, True)

            # Crear figura de matplotlib
            fig, ax = plt.subplots(figsize=(11, 6))

            # Colores para las lineas
            colores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
                       '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

            # Dibujar linea para cada rango de edad
            for i, (etiqueta, valores) in enumerate(datos_activos.items()):
                ax.plot(meses, valores, marker="o", label=etiqueta,
                       linewidth=2, color=colores[i % len(colores)])

            ax.set_xlabel("Mes", fontsize=11, fontweight="bold")
            ax.set_ylabel("Cantidad de alquileres", fontsize=11, fontweight="bold")
            ax.set_title(f"Segmentacion de clientes por edad - Año {anio}", fontsize=12, fontweight="bold")
            ax.legend(title="Rango de edad", bbox_to_anchor=(1.01, 1), loc="upper left")
            ax.grid(True, linestyle="--", alpha=0.5)
            fig.tight_layout()

            # Mostrar grafico en la ventana
            canvas = FigureCanvasTkAgg(fig, master=ventana_graf)
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=True)

        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar reporte: {str(e)}")


# Punto de entrada temporal
if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaReportes(root)
    root.mainloop()