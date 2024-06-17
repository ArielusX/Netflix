# -*- coding: utf-8 -*-
"""
Created on Wed May  8 00:39:54 2024

@author: alex
"""

import numpy as np
from dataclasses import dataclass
from abc import ABCMeta, abstractmethod, ABC
import math
class Recomanacio(ABC):
    """
    Clase abstracta para recomanaciones.
    """

    def __init__(self):
        self.productes = np.array([])
        self.ratings = np.array([])

    @abstractmethod
    def obtenir_valoracio(self, tipus, usuaris):
        pass

    @abstractmethod
    def calcula_mitjanes(self):
        pass

    @abstractmethod
    def calcula_score(self):
        pass

    @abstractmethod
    def mitjanas_global(self):
        pass

@dataclass
class Recomanacio_Simple(Recomanacio):
    """
    Clase de recomanación simple.
    """

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
        
        productes = np.unique(ratings_numericos[:, 1])
        mitjanes_per_item = []
        for producte in productes:
            ratings = ratings_numericos[ratings_numericos[:, 1] == producte, 2]
            mitjana = np.mean(ratings)
            num_vots = len(ratings)
            if num_vots < 3:
                break
            mitjanes_per_item.append((producte, mitjana, num_vots))
        
        self.mitjanes = np.array(mitjanes_per_item)
        print(self.mitjanes)
        return self.mitjanes

    def calcula_score(self):
        score_per_item = []

        for producte in self.mitjanes[:, 0]:

            score_producte = (self.mitjanes[self.mitjanes[:, 0] == producte, 2] / (self.mitjanes[self.mitjanes[:, 0] == producte, 2] + self.min_vots)) * self.mitjanes[self.mitjanes[:, 0] == producte, 1] + (self.min_vots / (self.mitjanes[self.mitjanes[:, 0] == producte, 2] + self.min_vots)) * self.mitjana
            score_per_item.append((producte, score_producte))
        
        self.score = np.array(score_per_item)
        return self.score

    def mitjanas_global(self):
        self.mitjana = np.mean(self.mitjanes[:, 1])
        print(self.mitjana)
        return self.mitjana

@dataclass
class Recomanacio_Colaborativa(Recomanacio):
    """
    Clase de recomanación colaborativa.
    """

    def __init__(self):
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
    