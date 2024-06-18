import numpy as np
@dataclass
class Avaluador():
    def __init__ (self,items_training={},items_test={}):
        self._train=items_training
        self._test=items_test 
        self._threshold=0.0
        self._n=0

    def mean_absolute_error(self, usuari):
    
        user_ratings = self.ratings[self.ratings['user_id'] == usuari]
        predicted_ratings = self.predictions[self.predictions['user_id'] == usuari]
        
        mae = abs(predicted_ratings['rating'] - user_ratings['rating']).mean()
        
        return mae

    def root_mean_absolute_error(self, usuari):

        rmse = np.sqrt(self.mean_absolute_error(self, usuari))
        
        return rmse

    def precision(self, usuari):

        user_predictions = self.predictions[self.predictions['user_id'] == usuari]
        relevant_predictions = user_predictions[user_predictions['rating'] >= self._threshold]  
        
        precision = len(relevant_predictions) / len(user_predictions)
        
        return precision

    def recall(self, usuari):

        user_ratings = self.ratings[self.ratings['user_id'] == usuari]
        predicted_ratings = self.predictions[self.predictions['user_id'] == usuari]
        
        relevant_items = user_ratings[user_ratings['rating'] >= self._threshold]  
        recommended_relevant_items = predicted_ratings[predicted_ratings['rating'] >= self._threshold]
        
        recall = len(recommended_relevant_items) / len(relevant_items)
        
        return recall

