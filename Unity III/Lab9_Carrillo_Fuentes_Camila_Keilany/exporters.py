import csv
import json
from fpdf import FPDF


class Exportador:

  def exportar(self, datos, ruta_archivo):
    """Método abstracto que debe ser sobrescrito por las clases hijas."""
    raise NotImplementedError(
        "Este método debe ser implementado por la subclase."
    )


class ExportadorCSV(Exportador):

  def exportar(self, datos, ruta_archivo):
    with open(ruta_archivo, "w", newline="", encoding="utf-8") as file:
      writer = csv.writer(file)
      writer.writerow(["ID", "Nombre", "Precio", "Stock"])
      for producto in datos:
        writer.writerow([
            producto["id"],
            producto["nombre"],
            producto["precio"],
            producto["stock"],
        ])
    print(f"Archivo CSV generado en: {ruta_archivo}")


class ExportadorTXT(Exportador):

  def exportar(self, datos, ruta_archivo):
    with open(ruta_archivo, "w", encoding="utf-8") as file:
      file.write("--- REPORTE DE PRODUCTOS ---\n")
      for producto in datos:
        file.write(
            f"ID: {producto['id']} | Nombre: {producto['nombre']} | Precio:"
            f" ${float(producto['precio']):.2f} | Stock: {producto['stock']}\n"
        )
    print(f"Archivo TXT generado en: {ruta_archivo}")


class ExportadorJSON(Exportador):

  def exportar(self, datos, ruta_archivo):
    datos_serializables = []
    for prod in datos:
      p = dict(prod)
      p["precio"] = float(p["precio"])
      datos_serializables.append(p)

    with open(ruta_archivo, "w", encoding="utf-8") as file:
      json.dump(datos_serializables, file, indent=4, ensure_ascii=False)
    print(f"Archivo JSON generado en: {ruta_archivo}")


class ExportadorPDF(Exportador):

  def exportar(self, datos, ruta_archivo):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(
        200, 10, txt="Reporte de Inventario de Productos", ln=True, align="C"
    )
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    for producto in datos:
      texto_linea = (
          f"ID: {producto['id']} | Producto: {producto['nombre']} | Precio:"
          f" ${float(producto['precio']):.2f} | Stock: {producto['stock']}"
      )
      pdf.cell(200, 10, txt=texto_linea, ln=True)

    pdf.output(ruta_archivo)
    print(f"Archivo PDF generado en: {ruta_archivo}")