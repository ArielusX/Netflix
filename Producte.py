# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 22:45:57 2024

@author: Lucas

"""


#Todo debe ser pasado a tratarse como objeto y no con dataframes
from typing import List
from dataclasses import dataclass

@dataclass
class Producte:

    _id: int
    _titol: str
    _rating: float

    @property
    def id(self):
        return self._id

    @property
    def titol(self):
        return self._titol

    def __str__(self):
        return f"Dades del Producte:\nID: {self.id}\tTitol: {self.titol}\tGeneres: {', '.join(self.genres)}"


@dataclass
class Llibre(Producte):
    #Book-Author,Year-Of-Publication,Publisher
    def __str__(self):
        return f"Dades del Llibre:\nID: {self.id}\tTitol: {self.titol}\tGeneres: {', '.join(self.genres)}"


@dataclass
class Pelicula(Producte):

    _genres: List[str]
    @property
    def genres(self):
        return self._genres
    
    def __str__(self):
        return f"Dades del Pelicula:\nID: {self.id}\tTitol: {self.titol}\tGeneres: {', '.join(self.genres)}"
