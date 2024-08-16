
#se llma asi porque es para el ejercicio 2 la papeleria

class Papeleria():
    tipo_cuaderno = ""
    tipo_lapiz = ""
    cantidad_cuadernos = 0
    cantidad_lapices = 0
    precio_venta = 0
    precio_lapices = 0
    ganancia = 0
    lleva_cuadernos = ""
    lleva_lapices = ""

    def __init__(self):
        self.ganancia = 0
        self.tipo_cuaderno = ""
        self.tipo_lapiz = ""

    def tipo_cuaderno_funcion(self):
        if self.tipo_cuaderno == "grande":
            self.precio_venta = (self.cantidad_cuadernos * 3.50) * 1.30
            print(f"Llevas {self.cantidad_cuadernos} cuadernos grandes y su precio es {self.precio_venta}")
            print("Marca Hojitas")
        elif self.tipo_cuaderno == "pequeño":
            self.precio_venta = (self.cantidad_cuadernos * 1.75) * 1.30
            print(f"Llevas {self.cantidad_cuadernos} cuadernos pequeños y su precio es {self.precio_venta}")
            print("Marca Hojitas")
        else:
            print("No conozco esa opción")

    def tipo_lapiz_funcion(self):
        if self.tipo_lapiz == "grafito":
            self.precio_lapices = (self.cantidad_lapices * 0.25) * 1.30
            print(f"Llevas {self.cantidad_lapices} lápices de grafito y su precio es {self.precio_lapices}")
            print("Marca Rayitas")
        elif self.tipo_lapiz == "color":
            self.precio_lapices = round(((self.cantidad_lapices * 0.50) * 1.30), 2)
            print(f"Llevas {self.cantidad_lapices} lápices de color y su precio es {self.precio_lapices}")
            print("Marca Rayitas")
        else:
            print("No conozco esa opción")

    def datos_compra(self):
        self.tipo_cuaderno_funcion()
        self.tipo_lapiz_funcion()

    def registrar_compra(self):
        print("**Bienvenido al sistema **")
        self.lleva_cuadernos = input("¿Llevarás cuadernos? (S/N): ").lower()
        if self.lleva_cuadernos == "s":
            self.tipo_cuaderno = input("Tipo de cuaderno (grande/pequeño): ").lower()
            self.cantidad_cuadernos = int(input("¿Cuántos cuadernos llevas?: "))
        else: 
            print("Recuerda, tenemos producto exclusivo en cuadernos.")
        print("****************")   
        self.lleva_lapices = input("¿Llevarás lápices? (S/N): ").lower()
        if self.lleva_lapices == "s":
            self.tipo_lapiz = input("Tipo de lápiz (grafito/color): ").lower()
            self.cantidad_lapices = int(input("¿Cuántos lápices llevas?: "))
        else: 
            print("Recuerda, tenemos producto exclusivo en lápices.")
        print("****************")   

    def mostrar_datos_compras(self):
        print("**Bienvenido al sistema **")
        print("Estado Cuadernos: ", self.lleva_cuadernos)
        if self.lleva_cuadernos == "s":
            self.tipo_cuaderno_funcion()
        else: 
            print("Recuerda, tenemos producto exclusivo en cuadernos.")
        print("****************")
        print("Estado Lápices: ", self.lleva_lapices)
        if self.lleva_lapices == "s":
            self.tipo_lapiz_funcion()
        else: 
            print("Recuerda, tenemos producto exclusivo en lápices.")
        print("***************")

# Creación de una instancia de Papeleria
compra1 = Papeleria()
print("******Bienvenido al sistema ******")
compra1.registrar_compra()
print("********************")
compra1.mostrar_datos_compras()
print("********************")