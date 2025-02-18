from django.db import models

# Create your models here.
class Calorie(models.Model):
    food_name = models.CharField(max_length=100)
    amount_of_calories = models.DecimalField(max_digits=7,decimal_places=1)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.food_name