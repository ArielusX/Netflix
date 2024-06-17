import numpy as np
from dataclasses import dataclass
from abc import ABCMeta, abstractmethod, ABC
import Recomanador
import Loader

fitxer1 = 'movies.csv'
fitxer2 = 'ratings.csv'
def mostrar_menu():
    print("Bienvenido al menu")
    print("Elige el set de datos a ser utilizado:")
    print("\t 1. Set de peliculas 1")
    print("\t 2. Set de peliculas 2")
    setdatos = input("Selecciona una opcion: ")

    print("Elige el set de datos a ser utilizado:")
    print("\t 1. Sistema de recomendación simple")
    print("\t 2. Sistema de recomendación colaborativo")
    sistema = input("Selecciona una opcion: ")

    return setdatos, sistema


def main():
    datos, sistema= mostrar_menu()
    
    loader = Loader.Loader()
    df_productes = loader.load(fitxer1)
    print(df_productes)

    df_ratings = loader.load(fitxer2)
    print(df_ratings)

    if sistema == "1":
        recomanador = Recomanador.Recomanacio_Simple(df_productes, df_ratings)
        recomanador.calcula_mitjanes()
        recomanador.calcula_score()
        recomanador.mitjanas_global()


if __name__ == "__main__":
    main()