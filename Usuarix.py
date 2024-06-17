
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Usuari:

    _id: int


    @property
    def id (self):
        return self._id

