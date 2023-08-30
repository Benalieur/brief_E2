from django.db import models
from .utils import make_prediction


class House(models.Model):
    Year_Built = models.IntegerField()
    Total_Bsmt_SF = models.IntegerField()
    first_Flr_SF = models.IntegerField()
    Gr_Liv_Area = models.IntegerField()
    Garage_Area = models.IntegerField()
    Overall_Qual = models.IntegerField()
    Full_Bath = models.IntegerField()
    Exter_Qual = models.CharField(max_length=10)
    Kitchen_Qual = models.CharField(max_length=10)
    Neighborhood = models.CharField(max_length=50)

    def predict_model (self):
        
        X_predict = {
            'Year_Built': self.Year_Built,
            'Total_Bsmt_SF': self.Total_Bsmt_SF,
            '1st_Flr_SF': self.first_Flr_SF,
            'Gr_Liv_Area': self.Gr_Liv_Area,
            'Garage_Area': self.Garage_Area,
            'Overall_Qual': self.Overall_Qual,
            'Full_Bath': self.Full_Bath,
            'Exter_Qual': self.Exter_Qual,
            'Kitchen_Qual': self.Kitchen_Qual,
            'Neighborhood': self.Neighborhood,
        }
        pred = make_prediction(X_predict)
        
        return pred
    
    
    
    
    