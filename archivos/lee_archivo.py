
f = open("texto.txt", "rt")
linea = f.readline()
while linea:
    print(linea)
    linea = f.readline()

f.close()