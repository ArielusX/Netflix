import numpy as np
from dataclasses import dataclass
from abc import ABCMeta, abstractmethod, ABC
import Recomanador
import Loader as Loader

fitxer1 = './Datasets/movies.csv'
fitxer2 = './Datasets/ratings2.csv'
fitxer3 = './Datasets/Books.csv'
fitxer4 = './Datasets/Ratings.csv'
fitxer5 = './Datasets/Users.csv'
def mostrar_menu():
    print("Bienvenido al menu")
    print("Elige el set de datos a ser utilizado:")
    print("\t 1. Set de peliculas")
    print("\t 2. Set de libros")
    setdatos = input("Selecciona una opcion: ")

    print("Elige el set de datos a ser utilizado:")
    print("\t 1. Sistema de recomendación simple")
    print("\t 2. Sistema de recomendación colaborativo")
    sistema = input("Selecciona una opcion: ")

    return setdatos, sistema

def main():
    datos, sistema= mostrar_menu()
    
    loader = Loader.Loader()

    users = df_users = loader.load_users(fitxer5)
    if datos == "1":
        df_productes = loader.load_products(fitxer1)
        df_ratings = loader.load_ratings_pro(fitxer2, users)
    else: 
        df_productes = loader.load_products(fitxer3)
        df_ratings = loader.load_ratings_pro(fitxer4, users)

    if sistema == "1":
        recomanador = Recomanador.Recomanacio_Simple(df_productes, df_ratings)
        recomanador.obtenir_valoracio(2)

    if sistema == "2":
        recomanador = Recomanador.Recomanacio_Colaborativa(df_productes, df_ratings, df_users)
        recomanador.obtenir_valoracio(2)


if __name__ == "__main__":
    main()