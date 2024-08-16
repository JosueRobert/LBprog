class ElPerro():
    tipo = "Perro"
    nombre_perro = ""
    raza = ""
    edad = 0
    color_pelaje = ""
    dueño = ""
    peso = 0
    estado = "No Atendido"
    
    def __init__(self):
        self.tipo = "Perro"
        self.peso = 0
    
    def registrar_perro(self):
        self.estado = "Atendido"
        print("ATENDIDO :D")
    
    def peso_perro(self):
        if self.peso > 10:
            print(f"Perro grande, su peso es: {self.peso} kg")
        else:
            print(f"Perro pequeño, su peso es: {self.peso} kg")
    
    def datos_perro(self, tipo, nombre, raza, edad, color_pelaje, dueño, peso, estado):
        self.tipo = tipo
        self.nombre_perro = nombre
        self.raza = raza
        self.edad = edad
        self.color_pelaje = color_pelaje
        self.dueño = dueño
        self.peso = peso
        self.estado = estado

    def recibir_datos_del_perro(self):
        print("***** Doctor Chapatín *****")
        nombre = input("Nombre de la mascota: ")
        raza = input("¿Qué raza es?: ")
        edad = int(input("¿Cuál es la edad?: "))
        color_pelaje = input("¿Cuál es el color del pelaje?: ")
        dueño = input("¿Quién es su dueño?: ")
        peso = int(input("¿Cuánto pesa en kg?: "))
        estado = input("¿El perro ya fue atendido? (S/N): ").lower()
        print("***************")
        self.datos_perro("Perro", nombre, raza, edad, color_pelaje, dueño, peso, estado)
    
    def mostrar_datos_perro(self):
        print("***** Doctor Chapatín *****")
        print("El nombre del perro es: ", self.nombre_perro)
        print("Raza del canino: ", self.raza)
        print("Edad del perro es: ", self.edad)
        print("Color del pelaje: ", self.color_pelaje)
        print("El dueño o encargado es: ", self.dueño)
        print("Peso del perro es: ", self.peso, "kg")
        if self.peso > 10:
            print("Este es un perro grande.")
        else:
            print("Este es un perro pequeño.")
        print("Estado: ", self.estado)
        if self.estado == "s":
            print("Su estado es Atendido.")
        else:
            print("Aún no fue atendido D:")

# Creación de una instancia de ElPerro
perro1 = ElPerro()
print("***** Doctor Chapatín *****")
print("Datos del Perro")
print("***************")
perro1.recibir_datos_del_perro() 
perro1.mostrar_datos_perro() 
print("***************")