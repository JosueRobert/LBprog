
"""
Un concesionario de autos vende vehículos nacionales e importados.
Todos tienen 4 ruedas y capacidad para 5 pasajeros. Esta información
debe registrarse siempre por razones de ley. Requiere un programa que
le permita almacenar las 10 principales características de los autos. El
precio de venta de cada auto es igual al precio de compra multiplicado
por 1.4 que corresponde a su margen de ganancia.
"""
class Auto():
    marca = ""
    modelo = ""
    anio = 0
    color = ""
    tipo = ""
    vin = ""
    numero_motor = ""
    precio_costo = 0
    precio_venta = 0
    asientos = 0
    ruedas = 0

    def __init__(self):
        self.precio_costo = 0
        self.precio_venta = 0
        self.numero_motor = ""
        self.anio = 0
        self.asientos = 0
        self.ruedas = 0

    def info_del_vehiculo(self):
        self.precio_venta = self.precio_costo * 1.4
        print(f"El vehículo fue adquirido a: ${self.precio_costo}")
        print(f"El vehículo queda a: ${self.precio_venta}")
        
    def registrar_vehiculo(self):
        print("Hola, bienvenido al concesionario de Marine Ford")
        self.marca = input("Marca del vehículo: ")
        self.modelo = input("Modelo del vehículo: ")
        self.anio = int(input("Año del vehículo: "))
        self.color = input("Color del vehículo: ")
        self.tipo = input("Tipo de vehículo: ")
        self.vin = input("VIN: ")
        self.numero_motor = input("Número de motor: ")
        self.asientos = int(input("Cantidad de asientos: "))
        self.ruedas = int(input("Cantidad de ruedas: "))
        self.precio_costo = float(input("Precio costo: $"))

    def datos_rayo_mcqueen(self, precio_costo, precio_venta, marca, modelo, anio, color, tipo, vin, numero_motor, asientos, ruedas):    
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.tipo = tipo
        self.vin = vin
        self.numero_motor = numero_motor
        self.precio_costo = precio_costo
        self.precio_venta = precio_venta
        self.asientos = asientos    
        self.ruedas = ruedas
        
    def mostrar_datos(self):
        print("Gracias por comprar en nuestro concesionario :D")
        print("Marca del vehículo: ", self.marca)
        print("Modelo del vehículo: ", self.modelo)
        print("Año del vehículo: ", self.anio)
        print("Color del vehículo: ", self.color)
        print("Tipo de vehículo: ", self.tipo)
        print("VIN: ", self.vin)
        print("Número de motor: ", self.numero_motor)
        print("Cantidad de asientos: ", self.asientos)
        print("Cantidad de ruedas: ", self.ruedas)
        self.info_del_vehiculo()

# Ejecución del programa
carro = Auto()
print("********Factura*********")
carro.registrar_vehiculo()
print("********************")
carro.mostrar_datos()
print("¡Te esperamos pronto! :D")