from exceptions import CantidadInvalida, StockInsuficiente

class Producto:
    def __init__(self, codigo, stock):
        self.codigo = codigo
        self.stock = stock
        
    def retirar(self, cantidad):
        if not isinstance(cantidad, int) or isinstance(cantidad, bool) or cantidad <= 0:
            raise CantidadInvalida("La cantidad a retirar debe ser un número entero mayor a cero.")
        
        if cantidad > self.stock:
            raise StockInsuficiente("No hay suficiente stock disponible para este producto.")
        
        self.stock -= cantidad
        return self.stock