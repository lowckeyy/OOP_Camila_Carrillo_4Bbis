from tkinter import filedialog, messagebox
from exporters import (
    ExportadorCSV,
    ExportadorJSON,
    ExportadorPDF,
    ExportadorTXT,
)
from models.products_model import Producto


class ProductosController:

  def __init__(self):
    self.modelo_producto = Producto()

  def exportar_reporte(self, formato_seleccionado):
    """Obtiene los datos del Modelo, selecciona la estrategia (clase hija)

    y ejecuta el método exportar() polimórficamente.
    """
    if not formato_seleccionado:
      messagebox.showwarning(
          "Selección requerida", "Por favor selecciona un formato de exportación."
      )
      return

    # Mapeo de formato a su clase con filtro de extensión corregido para Tkinter
    mapa_exportadores = {
        "CSV": (ExportadorCSV, ".csv", ("Archivos CSV", "*.csv")),
        "TXT": (ExportadorTXT, ".txt", ("Archivos TXT", "*.txt")),
        "JSON": (ExportadorJSON, ".json", ("Archivos JSON", "*.json")),
        "PDF": (ExportadorPDF, ".pdf", ("Archivos PDF", "*.pdf")),
    }

    if formato_seleccionado not in mapa_exportadores:
      messagebox.showerror(
          "Error", f"Formato '{formato_seleccionado}' no soportado."
      )
      return

    clase_exportador, ext_def, filtro = mapa_exportadores[formato_seleccionado]

    # Cuadro de diálogo para seleccionar ruta donde guardar
    ruta_archivo = filedialog.asksaveasfilename(
        defaultextension=ext_def,
        filetypes=[filtro, ("Todos los archivos", "*.*")],
        title=f"Guardar reporte como {formato_seleccionado}",
    )

    if not ruta_archivo:
      return  # El usuario canceló la ventana de guardado

    try:
      # 1. Obtener los productos desde el modelo (PostgreSQL)
      datos = self.modelo_producto.obtener_todos()
      if not datos:
        messagebox.showwarning(
            "Sin datos", "No hay productos registrados para exportar."
        )
        return

      # 2. Instanciar la clase correspondiente
      exportador = clase_exportador()

      # 3. Invocar la exportación polimórfica
      exportador.exportar(datos, ruta_archivo)

      messagebox.showinfo(
          "Éxito", f"Reporte exportado correctamente en:\n{ruta_archivo}"
      )
    except Exception as e:
      messagebox.showerror("Error de Exportación", f"Ocurrió un error: {e}")