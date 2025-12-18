"""
Problema: Registro básico de productos en una tienda
Contexto
Una tienda pequeña necesita un sistema sencillo para registrar sus productos y consultar información básica de cada uno. Cada producto se identifica por un código único y tiene un precio asociado.
Instrucciones
1. Crea una clase llamada Inventario.
2. La clase debe tener:
Un constructor que inicialice un diccionario vacío de productos.
El diccionario debe usar:
Clave: código del producto (string).
Valor: precio del producto (número).
Un método agregar_producto que reciba el código y el precio de un producto y lo agregue al diccionario.
Un método mostrar_productos que muestre todos los productos con su código y precio.
Un método consultar_precio que reciba un código y muestre el precio del producto correspondiente.
3. En el programa principal:
Agrega varios productos.
Muestra el inventario completo.
Consulta el precio de distintos productos
"""
class inventario:
    def __init__(self):
        self.productos = {}
    
    def agregar_producto(self, codigo, precio):
        #si no esta el codigo lo agrego 
        if codigo not in self.productos:
            self.productos[codigo] = precio
    
    def mostrar_productos(self):
        for codigo in self.productos:
            print(f" {codigo} ${self.productos[codigo]}")
    
    def consultar_precio(self, codigo):
         #saber si el producto existe 
        if codigo  in self.productos:
            print(f"{codigo} ${self.productos[codigo]}")
        

tienda = inventario()

tienda.agregar_producto("coca", 15)
tienda.agregar_producto("chetos", 18) 
tienda.agregar_producto("caguama", 47)     

tienda.mostrar_productos()

tienda.consultar_precio("chetos")





