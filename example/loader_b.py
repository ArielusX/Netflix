# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 21:05:54 2022

@author: User
"""
from dataclasses import dataclass
from example.usuari import Usuari
from pellicula import Pellicula
from joc import Joc
from typing import Dict
import csv

@dataclass
class LoaderB:
    """
    1. Loader B
    Esta clase es una clase ficticia encargada de realizar el preprocesamiento 
    de datos. En la versión sin restricciones, esta permite realizar varias
    personalizar varios aspectos que ya serán explicados durante la presentación.
    Esta versión en particular, la versión B, Es una simplificada de la original 
    que permite escoger el dataset con el que se va a trabajar, ya sea con 
    videojuegos o con películas. En la versión original esto no era necesario 
    debido a que se juntaban  ambos datasets y luego, de la mano del polimorfismo,
    se manejaba un nuevo dataset mixto.
    """
    _usuaris: Dict[str,object]
    _productes: Dict[str,object]
    
    def __init__(self, gamefile = 'game.csv', moviefile = 'movie.csv',userfile = "users.csv", movies = True):
        cont = 1
        self._productes = {}
        self._usuaris = {}
        maxi_vots = 0
        movies_cat = {}
        if movies:
            with open(moviefile, newline='', encoding="utf8") as csvfile:
                pelis = csv.reader(csvfile, delimiter='@')
    
                for peli in pelis:
                    if int(peli[3]) > maxi_vots:
                        maxi_vots = int(peli[3])
                with open(moviefile, newline='', encoding="utf8") as csvfile:
                    pelis = csv.reader(csvfile, delimiter='@')
                    for peli in pelis:
                        genres = peli[2].replace("'", "")[1:-1] 
                        rating_n = self.normalize_rating(0.6,peli[4], peli[3], maxi_vots)
                        self._productes.update({peli[0]:Pellicula(cont, peli[1], genres.split(', '), rating_n,peli[4])})     
                        movies_cat.update({peli[0]: genres.split(', ')})
                        cont += 1
        else:    
            with open(gamefile, newline='', encoding="utf8") as csvfile:
                jocs = csv.reader(csvfile, delimiter='@')
                for joc in jocs:
                    self._productes.update({str(cont):Joc(cont, joc[0], joc[2].split('|'), joc[1])})
                    cont += 1
        
        
        with open(userfile, newline='', encoding="utf8") as csvfile:
            users = csv.reader(csvfile, delimiter='@')
            
            for user in users:
                rat = []
                cates = []
                amics = user[1][1:-1].split(', ')
                ratings = user[2][2:-2].split('), (')
                cats = user[3][2:-2].split('), (')
                for rating in ratings:
                    aux = rating.split(', ')
                    rat.append((int(float(aux[0])),float(aux[1])))
                for cat in cats:
                    aux = cat.split(', ')
                    cates.append((aux[0][1:-1],float(aux[1])))
                self._usuaris.update({user[0]:Usuari(user[0], amics, rat, cates)})
    
    def normalize_rating(self,percentage: float,avg_rating: float,cant_ratings: int,maxi_vots: int):
        return percentage*(int(cant_ratings)/maxi_vots)+(1-percentage)*(float(avg_rating)/5)
    

    def get_usuaris(self):
        return self._usuaris
    def get_productes(self):
        return self._productes
    

'''
l1 = LoaderB('game.csv', 'movie.csv', 'users.csv',False)
...
#l1.save_network('network.csv')
'''