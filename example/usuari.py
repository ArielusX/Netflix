# -*- coding: utf-8 -*-
"""
Created on Mon May  2 10:58:24 2022

@author: Juan Pablo Codina
"""

from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Usuari:
    """
    Esta es la clase más importante de todo el proyecto. Durante su preprocesamiento
    esta se somete a una generacion del atributo categorias. Lo que se hace es 
    que se saca el promedio de la calificación que le ha dado el usuario a los
    productos de un cierto genero y luego se pondera con la cantidad para darse 
    una idea de que es lo que consume el usuario. Esto último funciona de forma
    muy similar a la ponderación usada en el sistema de recomedador simple.
    Además de esto, cuenta con la lista de amigos/followed que tiene el usuario.
    """
    _id: int
    _amics: List[int]
    _ratings: List[Tuple[int,float]]#además de poner los ratings por pelicula también poner los ratings por género
    _categorias: List[Tuple[str,float]]
    
    def __init__(self,id: int,amics: list, ratings:list,categorias:list):
        self._id = id
        self._amics = amics
        self._ratings = ratings
        self._categorias = categorias
    
    def to_tuple(self):
        return (self._id,self._amics,self._ratings,self._categorias)
    
    def get_ratings(self):
        return self._ratings
    
    def get_categorias(self):
        return self._categorias
    
    def get_amics(self):
        return self._amics
    
    def get_id(self):
        return self._id
    
    def get_cant_amics(self):
        return len(self._amics)
    
@dataclass
class Usuari ():
    _nickname:str
    _edat:str=''
    _poblacio:str=''
    _professio:str=''
    _pelicules:Dict=field(default_factory=dict) #diccionaris que recopilen totes les opinions de cada usuari, no conté cap objecte película
    _llibres:Dict=field(default_factory=dict)
    
    @property
    def nickname (self):
        return self._nickname
    
    @property
    def edat (self):
        return self._edat
    
    @property
    def poblacio (self):
        return self._poblacio
    
    @property
    def professio (self):
        return self._professio
    
    @property
    def pelicules(self):
        return self._pelicules
    
    @pelicules.setter
    def pelicules(self,pelicules):
        self._pelicules=pelicules
        
    @property
    def llibres(self):
        return self._llibres
    
    @llibres.setter
    def llibres(self,llibres):
        self._llibres=llibres
    
    def afegir_pelicula(self,opinio):
        self._pelicules[opinio[0]]=float(opinio[1])
    
    def afegir_llibre(self,opinio):
        self._llibres[opinio[0]]=float(opinio[1])
    
    def get_valoracio (self,item,nom_item): #devuelve valoraciones del item pasado (peli o libro)
        if item=='pelicula':
            return self._pelicules[nom_item]
        elif item=='llibre':
            return self._llibres[nom_item]
        else: print('Item no vàlid')

    def mitjana_puntuacions_usuari (self,item):
        count=0
        sumatori=0.0
        if item=='pelicula':
            for puntuacio in self._pelicules.values():
                sumatori+=puntuacio
                count+=1
        elif item=='llibre':
            for puntuacio in self._llibres.values():
                sumatori+=puntuacio
                count+=1
        if count!=0:
            return sumatori/count
        else: print('Item no vàlid')