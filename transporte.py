from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def moverse(self):
        pass

    @abstractmethod
    def energia(self):
        pass

    @abstractmethod
    def capacidad(self):
        pass

    def descripcion(self):
        return f"{self.marca} {self.modelo}"


class Auto(Transporte):
    def moverse(self):
        return "Se mueve por la calle"

    def energia(self):
        return "Combustible"

    def capacidad(self):
        return 5


class Bicicleta(Transporte):
    def moverse(self):
        return "Se mueve pedaleando"

    def energia(self):
        return "Energía humana"

    def capacidad(self):
        return 1


class Barco(Transporte):
    def moverse(self):
        return "Se mueve navegando"

    def energia(self):
        return "Combustible"

    def capacidad(self):
        return 20

    def hundirse(self):
        return "Se fue a pique"

b = Barco("Titanic", "1912")
print(b.descripcion())
print(b.moverse())
print(b.hundirse())

