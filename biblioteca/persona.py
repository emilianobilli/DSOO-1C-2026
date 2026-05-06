

class Persona(object):
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni    = dni

class Autor(Persona):
    def agregrar_biografia(self, biografia):
        self.bio = biografia

    


