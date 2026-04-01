
# La clase perro tiene: nombre, color, raza, edad
# Y habla

class perro (object):
  def __init__(self, nombre, color, raza,edad):
    self.nombre = nombre
    self.color = color
    self.raza = raza
    self.edad = edad      

  def habla(self):
    print("guau")

  def __str__(self):
    return f"{self.nombre} {self.color} {self.raza} {self.edad}"
p = perro ("jaime","marron","callejero", 2)
print(p)

