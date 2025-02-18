from django import forms
from .models import Calorie

class CalorieForm(forms.ModelForm):
    class Meta:
        model = Calorie
        fields = ['food_name','amount_of_calories']
        