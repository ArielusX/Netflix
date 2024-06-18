import pandas as pd

class Loader:
    """
    Clase base para cargar datos de un archivo CSV.
    """
    
    def load(self, name: str) -> pd.DataFrame:
        """
        Cargar un archivo CSV.
        """
        df = pd.read_csv(name)
        return df


class UsersLoader(Loader):
    """
    Clase para cargar usuarios desde un archivo CSV.
    """
    
    def load_users(self, name: str) -> pd.DataFrame:
        """
        Cargar el archivo CSV de usuarios.
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
        
        return df[['user_id', 'location', 'age']]


class RatingsLoader(Loader):
    """
    Clase para cargar ratings desde un archivo CSV.
    """
    
    def load_ratings(self, name: str) -> pd.DataFrame:
        """
        Cargar el archivo CSV de ratings.
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
        
        return df[['user_id', 'product_id', 'rating']]


class ProductsLoader(Loader):
    """
    Clase para cargar productos desde un archivo CSV.
    """
    
    def load_products(self, name: str) -> pd.DataFrame:
        """
        Cargar el archivo CSV de productos.
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
        
        return df
