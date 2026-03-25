
def convertir_segundos_hh_mm_ss(total_segundos):
        hh  = total_segundos // 3600
        tmp = total_segundos % 3600
        mm = tmp // 60
        ss = tmp % 60

        return (hh,mm,ss)

class Hora(object):
    def __init__(self, hh = 0, mm = 0, ss = 0):
        self.ss = mm * 60 + ss + hh * 3600

    def __str__(self):
        hh, mm, ss = convertir_segundos_hh_mm_ss(self.ss)
        return f"{hh}:{mm}:{ss}"

    def __add__(self, other):
        total_segundos = self.ss + other.ss
        hh, mm, ss = convertir_segundos_hh_mm_ss(total_segundos)
        return Hora(hh,mm,ss)

    def sumar(self,other):
        total_segundos = self.ss + other.ss
        hh, mm, ss = convertir_segundos_hh_mm_ss(total_segundos)
        return Hora(hh,mm,ss)

h1 = Hora(22,32,15)
h2 = Hora(10,30,50)
#h3 = h1.sumar(h2) # h2.sumar(h1)
h3 = h1 + h2
   
print(h3)





