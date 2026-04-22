from abc_animal import Animal

class Pajarito(Animal):
    def hacer_sonido(self):
        print("Pio Pio")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau Miau")


if __name__ == "__main__":
    p = Pajarito()
    p.hacer_sonido()
    g = Gato()
    g.hacer_sonido()