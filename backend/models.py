from django.db import models

class DietaryStyle(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class RestrictedFood(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    dietary_style = models.ForeignKey(DietaryStyle, on_delete=models.CASCADE, related_name='restricted_foods')