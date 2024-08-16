"""
Ejercicio4
Un almacén vende dispositivos electrónicos (celulares, tablets y portátiles). 
Todos PHR que es una nueva marca que está entrando en el mercado. 
Se requiere almacenar sus 6 principales características. 
Todos son productos importados y su precio de venta es igual al precio de compra multiplicado por 1.7 que corresponde a su margen de ganancia.
"""
class PHR():
    tipo_producto = ""
    modelo = ""
    almacenamiento = 0
    ram = 0
    precio_costo = 0
    precio_venta = 0

    def __init__(self):
        self.precio_costo = 0
        self.precio_venta = 0
        self.almacenamiento = 0
        self.ram = 0

    def info_del_producto(self):
        self.precio_venta = self.precio_costo * 1.7
        print(f"El artículo fue adquirido a: ${self.precio_costo}")
        print(f"El artículo queda a: ${self.precio_venta}")

    def registrar_producto(self):
        print("¡Hola, bienvenido a PHR!")
        self.tipo_producto = input("Tipo de Producto: ")
        self.modelo = input("Modelo: ")
        self.almacenamiento = int(input("Almacenamiento (en Gigas): "))
        self.ram = int(input("RAM (en Gigas): "))
        self.precio_costo = float(input("Precio Proveedor: $"))

    def datos_phr(self, precio_costo, precio_venta, tipo_producto, modelo, almacenamiento, ram):    
        self.tipo_producto = tipo_producto
        self.modelo = modelo
        self.almacenamiento = almacenamiento
        self.ram = ram
        self.precio_costo = precio_costo
        self.precio_venta = precio_venta

    def mostrar_datos(self):
        print("Gracias por comprar en PHR.")
        print("Tipo de producto: ", self.tipo_producto)
        print(f"Modelo del {self.tipo_producto}: ", self.modelo)
        print("Almacenamiento: ", self.almacenamiento, "Gigas")
        print("RAM: ", self.ram, "Gigas")
        self.info_del_producto()

# Ejecución del programa
articulo = PHR()
print("********Factura*********")
articulo.registrar_producto()
print("********************")
articulo.mostrar_datos()
print("¡Te esperamos pronto! :D")