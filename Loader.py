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

    def __init__(self):
        pass

    def load(self, name: str):
        #df = pd.read_csv(f"{name}.csv")
        df = pd.read_csv(f"{name}")
        return df