from animales import Gato

gatito = Gato()


def mi_decorador(funcion):
    def envoltura():
        print("Esto se ejecuta antes")
        funcion()
        print("Esto se ejecuta despues")
    return envoltura

@mi_decorador
def saludar():
    print("Hola")


saludar = mi_decorador(saludar)

saludar()