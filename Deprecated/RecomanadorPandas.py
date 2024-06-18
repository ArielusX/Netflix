# -*- coding: utf-8 -*-
"""
Created on Wed May  8 00:39:54 2024

@author: alex
"""

import numpy as np
from dataclasses import dataclass
from abc import ABCMeta, abstractmethod, ABC
import math
import pandas as pd
class Recomanacio(ABC):
    """
    Clase abstracta para recomanaciones.
    """

    def __init__(self, df_producte, df_ratings):
        super().__init__()
        self.producte = df_producte
        self.ratings = df_ratings.head(5000)

    @abstractmethod
    def obtenir_valoracio(self, tipus, usuaris):
        pass

@dataclass
class Recomanacio_Simple(Recomanacio):
    """
    Clase de recomanación simple.
    """

    def __init__(self, df_producte, df_ratings):
        super().__init__(df_producte, df_ratings)
        self.mitjanes =  self.calcula_mitjanes()
        self.score = self.calcula_score()
        self.min_vots = 3
        self.mitjana = self.mitjanes_global()

    def obtenir_valoracio(self, usuari):

        #ARREGLARRR
        productes_totals = set(self.ratings['product_id'].unique())
        productes_valorats = set(self.ratings[self.ratings['user_id'] == usuari]['product_id'])
        productes_no_valorats = list(productes_totals - productes_valorats)
        score_no_valorats = self.score[self.score['product_id'].isin(productes_no_valorats)]
        
        score_no_valorats = score_no_valorats.sort_values(by='score', ascending=False)
        top_5_productes = score_no_valorats.head(5)['product_id']


        top_5_df = self.producte[self.producte['id'].isin(top_5_productes)].merge(
            self.score, left_on='id', right_on='product_id', how='left'
        )

        top_5_df = top_5_df[['name', 'score']].sort_values(by='score', ascending=False)

        print(f"Las películas recomendadas para el usuario {usuari} son:")
        for _, row in top_5_df.iterrows():
            print(f"\t{row['name']} (Score: {row['score']:.2f})")
        
        return top_5_df['name'].tolist()

    def calcula_mitjanes(self):
     
        self.mitjana_global = self.ratings['rating'].mean()
        
        mitjanes_per_item = []
        for producte in self.ratings['product_id'].unique():
            ratings = self.ratings[self.ratings['product_id'] == producte]['rating']
            mitjana = ratings.mean()
            num_vots = len(ratings)
            if num_vots < self.min_vots:
                continue
            mitjanes_per_item.append((producte, mitjana, num_vots))
        
        self.mitjanes = pd.DataFrame(mitjanes_per_item, columns=['product_id', 'mitjana', 'num_vots'])
        return self.mitjanes

    def calcula_score(self):
        score_per_item = []

        for producte in self.mitjanes['product_id'].unique():
            ratings_producte = self.mitjanes[self.mitjanes['product_id'] == producte]
            
            score_producte = (ratings_producte['num_vots'] / (ratings_producte['num_vots'] + self.min_vots)) * ratings_producte['mitjana'] + (self.min_vots / (ratings_producte['num_vots'] + self.min_vots)) * self.mitjana
            
            score_per_item.append((producte, score_producte.values[0]))
        
        self.score = pd.DataFrame(score_per_item, columns=['product_id', 'score'])
        return self.score

    def mitjanes_global(self):
        self.mitjana = self.mitjanes['mitjana'].mean()
        return self.mitjana


@dataclass
class Recomanacio_Colaborativa(Recomanacio):
    """
    Clase de recomanación colaborativa.
    """

    def __init__(self, df_producte, df_ratings, df_usuaris):
        super().__init__(df_producte, df_ratings)
        self.usuaris =  df_usuaris

    def obtenir_valoracio(self, usuari):
        similaritats = {}
        for user_id, ratings in self.usuaris.items():
            similarity = self.cosine_similarity(self.usuaris[usuari], ratings)
            similaritats[user_id] = similarity

        return sorted(similaritats.items(), key=lambda x: x[1], reverse=True)

    def cosine_similarity(self, user1, user2):
        user1_series = pd.Series(user1)
        user2_series = pd.Series(user2)

        common_items = user1_series.index.intersection(user2_series.index)
        if len(common_items) == 0:
            return 0

        dot = (user1_series[common_items] * user2_series[common_items]).sum()
        mag_user1 = math.sqrt((user1_series ** 2).sum())
        mag_user2 = math.sqrt((user2_series ** 2).sum())
        
        similarity = dot / (mag_user1 * mag_user2)
        return similarity
    