class ErrorInventario(Exception):
    def __init__(self, mensaje="Ocurrió un error en la operación de inventario."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class ProductoNoEncontrado(ErrorInventario):
    def __init__(self, codigo=None, mensaje=None):
        self.codigo = codigo
        if mensaje is None:
            if codigo is not None:
                mensaje = f"El producto con código '{codigo}' no existe en el inventario."
            else:
                mensaje = "El producto solicitado no existe en el inventario."
        super().__init__(mensaje)


class CantidadInvalida(ErrorInventario):
    def __init__(self, cantidad=None, mensaje=None):
        self.cantidad = cantidad
        if mensaje is None:
            mensaje = "La cantidad a retirar debe ser un número entero mayor a cero."
        super().__init__(mensaje)


class StockInsuficiente(ErrorInventario):
    def __init__(self, stock_disponible=None, cantidad_solicitada=None, mensaje=None):
        self.stock_disponible = stock_disponible
        self.cantidad_solicitada = cantidad_solicitada
        if mensaje is None:
            if stock_disponible is not None and cantidad_solicitada is not None:
                mensaje = (
                    f"No hay suficiente stock disponible (solicitado: {cantidad_solicitada}, "
                    f"disponible: {stock_disponible})."
                )
            else:
                mensaje = "No hay suficiente stock disponible para este producto."
        super().__init__(mensaje)