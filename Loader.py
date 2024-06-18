# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 21:05:54 2022

@author: User
"""

from dataclasses import dataclass
import pandas as pd
import Usuari
import Producte

@dataclass
class Loader:
    """
    Clase para cargar datos de un archivo CSV.
    """
    def __init__(self, _name=None):
        self._name = _name

    def load(self, name: str):
        """
        Load a CSV file 
        """
        df = pd.read_csv(name)
        return df


    def load_users(self, name: str) -> pd.DataFrame:
        """
        Load the users CSV file.
        """
        df = self.load(name)  

        column_mapping = {
            'user_id': ['userId', 'User-ID'],
            'location': ['Location'],
            'age': ['Age']
        }

        for standard_name, possible_names in column_mapping.items():
            for possible_name in possible_names:
                if possible_name in df.columns:
                    df = df.rename(columns={possible_name: standard_name})
                    break

        usuaris = []
        for _, row in df.iterrows():
            user = Usuari.Usuari(row['user_id'], row['location'], row['age'])
            usuaris.append(user)

        return usuaris

    #Forma simple
    def load_ratings(self, name: str) -> pd.DataFrame:
        """
        Load the ratings CSV file.
        """
        df = self.load(name)  

        column_mapping = {
            'user_id': ['userId', 'User-ID'],
            'product_id': ['movieId', 'ISBN'],
            'rating': ['rating', 'Book-Rating']
        }

        for standard_name, possible_names in column_mapping.items():
            for possible_name in possible_names:
                if possible_name in df.columns:
                    df = df.rename(columns={possible_name: standard_name})
                    break
                
        return df[["user_id","product_id","rating"]]
    
    def load_ratings_pro(self, name: str, usuaris: list):
        """
        Load the ratings CSV file and assign ratings to each user.
        """
        df = self.load(name)  

        column_mapping = {
            'user_id': ['userId', 'User-ID'],
            'product_id': ['movieId', 'ISBN'],
            'rating': ['rating', 'Book-Rating']
        }

        for standard_name, possible_names in column_mapping.items():
            for possible_name in possible_names:
                if possible_name in df.columns:
                    df = df.rename(columns={possible_name: standard_name})
                    break

        ratings_df = df[["user_id", "product_id", "rating"]]
        
        user_dict = {user.id: user for user in usuaris}
        
        for _, row in ratings_df.iterrows():
            user_id = row['user_id']
            product_id = row['product_id']
            rating = row['rating']
            if user_id in user_dict:
                user_dict[user_id].add_rating(product_id, rating)
        
        return df

    def load_products(self, name: str) -> pd.DataFrame:
        """
        Load the products CSV file.
        """
        df = self.load(name)

        column_mapping = {
            'id': ['ISBN', 'movieId'],
            'name': ['title', 'Book-Title']
        }

        for standard_name, possible_names in column_mapping.items():
            for name in possible_names:
                if name in df.columns:
                    df = df.rename(columns={name: standard_name})
                    break

        return df
    def load_products_pro(self, name: str) -> list:
        """
        Load the products CSV file and create Producte objects.
        """
        df = self.load(name)

        column_mapping = {
            'id': ['ISBN', 'movieId'],
            'name': ['title', 'Book-Title']
        }

        for standard_name, possible_names in column_mapping.items():
            for possible_name in possible_names:
                if possible_name in df.columns:
                    df = df.rename(columns={possible_name: standard_name})
                    break

        productes = []
        for _, row in df.iterrows():
            product = Producte(row['id'], row['name'])
            productes.append(product)

        return productes
'''
# Example usage
loader = Loader(_name="example")
users_df = loader.load_users("path/to/users.csv")
ratings_df = loader.load_ratings("path/to/ratings.csv")
products_df = loader.load_products("path/to/products.csv")'''