# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 21:05:54 2022

@author: User
"""
from dataclasses import dataclass
import pandas as pd

@dataclass
class Loader:
    """
    Clase para cargar datos de un archivo CSV.
    """
    _name: str

    def __init__(self, name: str):
        self._name = name

    def load(self):
        # self._productes.update({str(cont):Joc(cont, joc[0], joc[2].split('|'), joc[1])})
        df = pd.read_csv(f"{self._name}.csv")
        print(df)
        return df