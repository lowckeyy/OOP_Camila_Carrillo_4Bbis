from inventory import Inventario
from exceptions import ErrorInventario

def main():
    inventario = Inventario()
    codigo = input("Código del producto: ")
    
    try:
        cantidad = int(input("Cantidad a retirar: "))
        stock_restante = inventario.retirar(codigo, cantidad)
        
    except ValueError:
        print("Error: La cantidad debe ser un número entero.")
        
    except ErrorInventario as error:
        print(f"No se pudo realizar la operación: {error}")
        
    else:
        print(f"Retiro realizado con éxito. Stock restante: {stock_restante}")

if __name__ == "__main__":
    main()