# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 22:45:57 2024

@author: Lucas

"""
from typing import List, Dict
from dataclasses import dataclass, field

@dataclass
class Producte:
    _id: int
    _titol: str
    _rating: Dict = field(default_factory=dict)

    @property
    def id(self):
        return self._id

    @property
    def titol(self):
        return self._titol

    @property
    def rating(self):
        return self._rating

    @id.setter
    def id(self, id):
        self._id = id

    @titol.setter
    def titol(self, titol):
        self._titol = titol

    def ratings(self, rating, nom_usuari):
        self._rating[nom_usuari] = rating

    def __str__(self):
        return f"Dades del Producte:\nID: {self.id}\tTitol: {self.titol}"

@dataclass
class Llibre(Producte):
    _author: str = ''
    _fecha: str = ''
    _publicador: str = ''
    # Book-Author, Year-Of-Publication, Publisher

    @property
    def author(self):
        return self._author

    @property
    def fecha(self):
        return self._fecha

    @property
    def publicador(self):
        return self._publicador

    @author.setter
    def author(self, author):
        self._author = author

    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @publicador.setter
    def publicador(self, publicador):
        self._publicador = publicador

    def __str__(self):
        return f"Dades del Llibre:\nID: {self.id}\tTitol: {self.titol}"

@dataclass
class Pelicula(Producte):
    '''_genres: List[str]

    @property
    def genres(self):
        return self._genres

    @genres.setter
    def genres(self, genres):
        self._genres = genres
'''
    def __str__(self):
        return f"Dades del Pelicula:\nID: {self.id}\tTitol: {self.titol}\tGeneres: {', '.join(self.genres)}"
