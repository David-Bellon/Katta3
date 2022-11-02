import pandas as pd
import re
halcon = "Millennium Falcon"
estrella = "Star Destroyer"
class Nave():
    def __init__(self, nombre, largo, tripulacion, pasajeros) -> None:
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros

def set_up():
    df = pd.read_csv("exaclau\Ejer3\data.csv")
    lista_naves = []
    for i in range(df.shape[0]):
        lista_naves.append(Nave(df["nombre"][i], df["largo"][i], df["tripulacion"][i], df["pasajeros"][i]))

    return df, lista_naves


def falcon_star(naves):
    for nave in naves:
        if nave.nombre == halcon or nave.nombre == estrella:
            print("Nombre:", nave.nombre, "Largo:", nave.largo, "Tripulacion:", nave.tripulacion, "Pasajeros:", nave.pasajeros)


def pas_capacity(df, naves):
    sorted = df.sort_values(by=["pasajeros"], ascending=False)
    to_return = []
    for i in range(len(sorted.head())):
        to_return.append(naves[sorted.index[i]])
    #Si quieres pues se printea
    return to_return

def max_trip(naves):
    max = naves[0]
    for nave in naves[1:]:
        if nave.tripulacion > max.tripulacion:
            max = nave
    return nave.nombre

def at(naves):
    for nave in naves:
        if re.search("^AT", nave.nombre):
            print(nave.nombre)
    
def more_six(naves):
    out = []
    for nave in naves:
        if nave.pasajeros >= 6:
            out.append(nave)
            print(nave.nombre)
    return out

def h_l(naves):
    max = naves[0]
    min = naves[0]
    for nave in naves[1:]:
        if float(nave.largo.replace(",",".")) > float(max.largo):
            max = nave
        if float(nave.largo.replace(",",".")) < float(min.largo):
            min = nave
    
    print("Maxima Longitud")
    print("Nombre:", max.nombre, "Largo:", max.largo, "Tripulacion:", max.tripulacion, "Pasajeros:", max.pasajeros)
    print("Minima Capacidad")
    print("Nombre:", min.nombre, "Largo:", min.largo, "Tripulacion:", min.tripulacion, "Pasajeros:", min.pasajeros)


def main():
    df, naves = set_up()
    falcon_star(naves)
    pas_capacity(df, naves)
    print(max_trip(naves))
    at(naves)
    more_six(naves)
    h_l(naves)