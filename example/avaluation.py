# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 16:57:39 2022

@author: Joel
"""

import numpy as np
from dataclasses import dataclass,field
from abc import ABCMeta, abstractmethod, ABC
import csv
import math
from typing import Dict,List,Tuple
import time
from item2 import Item,Pelicula,Llibre
from sklearn.feature_extraction.text import TfidfVectorizer
from score import Score,Score_simple,Score_colaborativa,Score_contingut
from recomanacio2 import Recomanacio,Recomanacio_Colaborativa,Recomanacio_Simple,Recomanacio_Contingut


def get_keys_with_value(dic, value):
    return [key for key, val in dic.items() if val == value]


@dataclass
class Avaluacio ():
    def __init__ (self,items_training={},items_test={}):
        self._train=items_training
        self._test=items_test #I𝑡: Conjunt de ítems del conjunt de test (només els que tenen valoració diferent de zero)
        self._llindar=0.0
        self._n=0
    
    @property
    def llindar (self):
        return self._llindar
    
    @llindar.setter
    def llindar (self,llindar):
        self._llindar=llindar
    
    @property
    def n (self):
        return self._n
    
    @n.setter
    def n (self,n):
        self._n=n
    
    def inicialitza_n_prediccions (self):
        self._pelicules_def=[]
        test_ordenat=(reversed(sorted(self._train.values())))
        for value in test_ordenat:
            pelicules=get_keys_with_value(self._train, value)
            for element in pelicules:
                if element not in self._pelicules_def:
                    self._pelicules_def.append(element)
                if len(self._pelicules_def)==self._n:
                    break
            else:
                continue
            break

    
    def mean_absolut_error (self,usuari): #prediccio: diccionari de diccionaris d'usuaris amb les prediccions del sistema de cada usuari, base_dades: Base_Dades_Usuari, usuari: número d'usuari
            sumatori=0.0
            count=0
            for element in self._test:
                if element in self._train:
                    count+=1
                    sumatori+=abs(float(self._train[element])-float(self._test[element]))
            return sumatori/count
    
    def precision (self,usuari): #prediccio: diccionari de diccionaris d'usuaris amb les prediccions del sistema de cada usuari, base_dades: Base_Dades_Usuari, usuari: número d'usuari
        conjunt=0
        for pelicula in self._pelicules_def:
                if pelicula in self._test:
                    if (self._test[pelicula]>=self._llindar):
                        conjunt+=1
        return (conjunt)/self._n
    
    def recall (self,usuari): #prediccio: diccionari de diccionaris d'usuaris amb les prediccions del sistema de cada usuari, base_dades: Base_Dades_Usuari, usuari: número d'usuari
        conjunt1=0
        conjunt2=0
        for pelicula in self._pelicules_def:
                if pelicula in self._test:
                    if (self._train[pelicula]>=self._llindar):
                        conjunt1+=1    
        for pelicula in self._test:
            if self._test[pelicula]>self._llindar:
                conjunt2+=1
        return conjunt1/conjunt2


