
# La clase perro tiene: nombre, color, raza, edad
# Y habla

class Perro(object):
    def __init__(self, nombre, color, raza, edad):
        self.nombre = nombre
        self.color = color
        self.raza = raza
        self.edad = edad

    def habla(self):
        print("Guau!")

    def __str__(self):
        return f"Perro nombre {self.nombre}"

p = Perro("Jaime", "azul", "calle", 2)
print(p)

