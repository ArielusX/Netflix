# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 22:45:57 2024

@author: Lucas

"""

from typing import List
from dataclasses import dataclass

@dataclass
class Producte:

    _id: int
    _titol: str
    _genres: List[str]
    _rating: float

    @property
    def id(self):
        return self._id

    @property
    def titol(self):
        return self._titol

    @property
    def genres(self):
        return self._genres

    @property
    def rating(self):
        return self._rating

    def __str__(self):
        return f"Dades del Producte:\nID: {self.id}\tTitol: {self.titol}\tGeneres: {', '.join(self.genres)}"


@dataclass
class Llibre(Producte):
    def __str__(self):
        return f"Dades del Llibre:\nID: {self.id}\tTitol: {self.titol}\tGeneres: {', '.join(self.genres)}"


@dataclass
class Pelicula(Producte):
    def __str__(self):
        return f"Dades del Pelicula:\nID: {self.id}\tTitol: {self.titol}\tGeneres: {', '.join(self.genres)}"


@dataclass
class Joc(Producte):
    def __str__(self):
        return f"Dades del Joc:\nID: {self.id}\tTitol: {self.titol}\tGeneres: {', '.join(self.genres)}"