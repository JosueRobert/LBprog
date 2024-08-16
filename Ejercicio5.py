"""
Un concesionario de electrodomésticos vende productos como refrigeradores, lavadoras y microondas. 
Cada producto tiene características específicas que deben registrarse.
 El precio de venta de cada electrodoméstico es igual al precio de compra multiplicado por 1.3,
 que corresponde a su margen de ganancia.
"""
class Electrodomestico():
    Marca = ""
    Modelo = ""
    Año = 0
    Color = ""
    Tipo = ""
    Serial = ""
    PrecioCosto = 0
    PrecioVenta = 0
    Garantia = 0
    Voltaje = 0

    def __init__(self):
        self.PrecioCosto = 0
        self.PrecioVenta = 0
        self.Serial = ""
        self.Año = 0
        self.Garantia = 0
        self.Voltaje = 0

    def InfoDelElectrodomestico(self):
        self.PrecioVenta = self.PrecioCosto * 1.3
        print(f"El electrodoméstico fue adquirido a: ${self.PrecioCosto}")
        print(f"El electrodoméstico queda a: ${self.PrecioVenta}")

    def RegistrarElectrodomestico(self):
        print("¡Bienvenido a la Tienda de Electrodomésticos!")
        self.Marca = input("Marca del electrodoméstico: ")
        self.Modelo = input("Modelo del electrodoméstico: ")
        self.Año = int(input("Año del electrodoméstico: "))
        self.Color = input("Color del electrodoméstico: ")
        self.Tipo = input("Tipo de electrodoméstico: ")
        self.Serial = input("Número de serie: ")
        self.Garantia = int(input("Garantía (en meses): "))
        self.Voltaje = int(input("Voltaje (en voltios): "))
        self.PrecioCosto = float(input("Precio Costo: $"))

    def MostrarDatos(self):
        print("Gracias por comprar en nuestra tienda :D")
        print("Marca del electrodoméstico: ", self.Marca)
        print("Modelo del electrodoméstico: ", self.Modelo)
        print("Año del electrodoméstico: ", self.Año)
        print("Color del electrodoméstico: ", self.Color)
        print("Tipo de electrodoméstico: ", self.Tipo)
        print("Número de serie: ", self.Serial)
        print("Garantía: ", self.Garantia, "meses")
        print("Voltaje: ", self.Voltaje, "V")
        self.InfoDelElectrodomestico()

# Ejecución del programa
electrodomestico = Electrodomestico()
print("********Factura*********")
electrodomestico.RegistrarElectrodomestico()
print("********************")
electrodomestico.MostrarDatos()
print("*******Gracias por su compra********")
print("¡Te esperamos pronto! :D")