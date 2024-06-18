from dataclasses import dataclass, field
from typing import Optional,  Dict
import numpy as np


@dataclass
class Usuari:
    _id: int
    _age: int
    _location: str = ''
    _ratings: Dict[int, float] = field(default_factory=dict, repr=False)

    @property
    def id(self):
        return self._id

    @property
    def location(self):
        return self._location

    @property
    def age(self):
        return self._age

    @property
    def ratings(self):
        return self._ratings

    @id.setter
    def id(self, id):
        self._id = id

    @location.setter
    def location(self, location):
        self._location = location

    @age.setter
    def age(self, age):
        self._age = age
    
    def add_rating(self, product_id, rating):
        self.ratings[product_id] = rating