from django.db import models

class DietaryStyle(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class RestrictedFood(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    dietary_style = models.ForeignKey(DietaryStyle, related_name='restricted_foods', on_delete=models.CASCADE)

    def __str__(self):
        return self.name