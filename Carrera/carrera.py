import random
import time
import os

class Caballo(object):
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero
        self.posicion = 0
        
    def limpia_posicion(self):
        self.posicion = 0
        
    def avanzar(self):
        numero = random.randrange(0, 10)
        if numero == 0:
        	self.posicion = self.posicion + 5
        elif numero >= 1 and numero < 5:
            self.posicion = self.posicion + 3
        else:
            self.posicion = self.posicion + 1
            

class Carrera(object):
    def __init__(self, distancia):
        self.distancia = distancia
        self.caballos  = []

    def agregar_caballo(self, caballo):
        caballo.limpia_posicion()
        self.caballos.append(caballo)
        
    def avanzar_caballos(self):
        i = 0
        while i < len(self.caballos):
            self.caballos[i].avanzar()
            i = i + 1
        
    def correr(self):
        
        while True:
            self.avanzar_caballos()
            i = 0
            while i < len(self.caballos):
                p = " " * self.caballos[i].posicion + "X"
                print("%20s(%d) | %s" % (self.caballos[i].nombre, self.caballos[i].numero, p))
                if self.caballos[i].posicion >= self.distancia:
                    return self.caballos[i]
                i = i + 1
            time.sleep(1)
            os.system("clear") # os.system("cls")
        
        

carrera = Carrera(50)
c1 = Caballo("Yatasto", 2)
c2 = Caballo("Toro", 3)
c3 = Caballo("Jose", 5)
c4 = Caballo("Mamerto", 7)
c5 = Caballo("Esteban", 1)
c6 = Caballo("Rayo", 4)

carrera.agregar_caballo(c1)
carrera.agregar_caballo(c2)
carrera.agregar_caballo(c3)
carrera.agregar_caballo(c4)
carrera.agregar_caballo(c5)
carrera.agregar_caballo(c6)

ganador = carrera.correr()
print("Ganador: ",ganador.nombre, ganador.numero)