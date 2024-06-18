
from dataclasses import dataclass, field
from typing import Optional
import numpy as np

@dataclass
class Usuari:

    _id: int
    _location: str=''
    _age: int
    _tfidf_matrix: Optional[np.ndarray] = field(default=None, repr=False)

    @property
    def id (self):
        return self._id
    @property
    def location (self):
        return self._location
    
    @property
    def age (self):
        return self._age
    @property
    def tfidf_matrix(self):
        return self._tfidf_matrix
    
    @tfidf_matrix.setter
    def matrix_setter (self, matrix):
        if matrix is not None and not isinstance(matrix, np.ndarray):
            raise ValueError("optional_matrix debe ser una matriz de NumPy")
        self._tfidf_matrix = matrix
        
    @id.setter
    def ids (self, id):
        self._id = id
    
    @location.setter
    def locations (self,location):
        self._location = location
    
    @age.setter
    def ages (self, age):
        self._age = age