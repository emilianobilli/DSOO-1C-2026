#!/usr/bin/env python3
import argparse

PESOS = [7, 2, 3, 4, 5, 6, 7]  # para dígitos de izquierda a derecha (d1..d7)


def calcular_dv(partida: str) -> str:

    if not partida.isdigit() or len(partida) != 7:
        raise ValueError("partida incorrecta")

    suma = sum(int(d) * p for d, p in zip(partida, PESOS))
    r = suma % 11

    if r == 10:
        return "01"
    return f"{r:02d}"


if __name__ == "__main__":
    i = 4190130
    while i < 4190272:
        print("%s,%s" % (i, calcular_dv(str(i))))
        i = i + 1
