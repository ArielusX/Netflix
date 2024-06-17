# -*- coding: utf-8 -*-
"""
Created on Wed May  8 00:39:54 2024

@author: alex
"""

import numpy as np
from dataclasses import dataclass,field
from abc import ABCMeta, abstractmethod, ABC
import csv
import math
from typing import Dict,List,Tuple

fitxer1 = 'movies.csv'
fitxer2 = 'ratings.csv'

class Recomanacio (): #plantejar herencia
    def __init__(self):
        
        self.pelicules = np.array([])
        self.ratings = np.array([])

    #temporal
    def dades_pelicula(self, fitxer1):
        with open(fitxer1, 'r', encoding='utf8') as csv_file:
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)
            for row in csvreader:
                row_2 = np.array(row)
                self.pelicules = np.append(self.pelicules, row_2)
            print(self.pelicules)

        #Se puede importar con pandas
            
        return self.pelicules
    
    def dades_ratings(self, fitxer2):
        with open(fitxer2, 'r', encoding='utf8') as csv_file:
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)
            for row in csvreader:
                row_2 = np.array(row)
                self.ratings = np.append(self.ratings, row_2)
        return self.ratings
    
    def ratings_pelicula(self):
        dades_ratings = np.array([])
        

    

class Recomanacio_Simple(Recomanacio):
    def __init__(self):
        super().__init__()
        self.mitjanes = np.array([])
        self.score = np.array([])

        self.min_vots = 3
        self.mitjana = 0

    def obtenir_valoracio(self, tipus, usuaris):
        pass

    def calcula_mitjanes(self):
        ratings_numericos = self.ratings.astype(float)
        
        self.mitjana_global = np.mean(ratings_numericos[:, 2])
        
        pelicules = np.unique(ratings_numericos[:, 1])
        mitjanes_per_item = []
        for pelicula in pelicules:
            ratings_pelicula = ratings_numericos[ratings_numericos[:, 1] == pelicula, 2]
            mitjana_pelicula = np.mean(ratings_pelicula)
            num_vots_pelicula = len(ratings_pelicula)
            if num_vots_pelicula <3:
                break
            mitjanes_per_item.append((pelicula, mitjana_pelicula, num_vots_pelicula))
        
        self.mitjanes = np.array(mitjanes_per_item)
        print(self.mitjanes)
        return self.mitjanes

    def calcula_score(self):

        score_per_item = []

        for pelicula in self.mitjanes[:,0]:

            score_pelicula = (self.mitjanes[self.mitjanes[:, 0] == pelicula, 2] / (self.mitjanes[self.mitjanes[:, 0] == pelicula, 2] + self.min_vots)) * self.mitjanes[self.mitjanes[:, 0] == pelicula, 1] + (self.min_vots / (self.mitjanes[self.mitjanes[:, 0] == pelicula, 2] + self.min_vots)) * self.mitjana
            score_per_item.append((pelicula, score_pelicula))
        
        self.score = np.array(score_per_item)
        return self.score

    def mitjanas_global(self):
        self.mitjana= np.mean(self.mitjanes[:, 1])
        print(self.mitjana)
        return self.mitjana

class Recomanacio_Colaborativa(Recomanacio):
    def __init__():
        super().__init__()
        
    def obtenir_valoracio(self, usuaris):
        similaritats = {}
        for user_id, ratings in usuaris.items():
            similarity = self.cosine_similarity(usuaris[tipus], ratings)
            similaritats[user_id] = similarity

        return sorted(similaritats.items(), key=lambda x: x[1], reverse=True)

    def cosine_similarity(self, user1, user2):

        common_items = set(user1.keys()) & set(user2.keys()) 
        if len(common_items) == 0:
            return 0 
        dot = sum(user1[item] * user2[item] for item in common_items)
        mag_user1 = math.sqrt(sum(user1[item] ** 2 for item in user1))
        mag_user2 = math.sqrt(sum(user2[item] ** 2 for item in user2))
        similarity = dot / (mag_user1 * mag_user2)
        return similarity

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

def recomend(sistema,fitxer1, fitxer2):
    
    if sistema == "1":
        reco = Recomanacio_Simple()
    else :
        reco = Recomanacio_Colaborativa()

    reco.dades_pelicula(fitxer1)
    reco.dades_ratings(fitxer2)
    reco.calcula_mitjanes()

def main():
    datos, sistema= mostrar_menu()
    
    if datos == "1":
        fitxers = fitxer1, fitxer2
    elif datos == "2":
        fitxers = fitxer1, fitxer2
    else:
        #Error
        pass

    if sistema == "1":
        recomend(sistema,fitxer1, fitxer2)
    elif sistema == "2":
        pass
    else:
        # Error
        pass


if __name__ == "__main__":
    main()