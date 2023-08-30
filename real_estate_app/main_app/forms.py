from django import forms
from .models import House

class HouseForm(forms.ModelForm):
    Year_Built = forms.IntegerField(label="Année de construction ")
    Total_Bsmt_SF = forms.IntegerField(label="Surface de la cave ")
    first_Flr_SF = forms.IntegerField(label="Surface du premier étage ")
    Gr_Liv_Area = forms.IntegerField(label="Surface habitable au sol")
    Garage_Area = forms.IntegerField(label="Surface du garage")
    Overall_Qual = forms.IntegerField(label="Qualité générale des finitions et des matériaux ")
    Full_Bath = forms.IntegerField(label="Nombre de salles de bain ")
    Exter_Qual = forms.CharField(max_length=10, label="Qualité des matériaux extérieurs ")
    Kitchen_Qual = forms.CharField(max_length=10, label="Qualité des matérieux de la cuisine")
    Neighborhood = forms.CharField(max_length=50, label="Quartier ")
    
    class Meta:
        model = House 
        fields = '__all__'