from rest_framework import serializers
from .models import DietaryStyle, RestrictedFood

class RestrictedFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestrictedFood
        fields = ['id', 'name', 'category']

class DietaryStyleSerializer(serializers.ModelSerializer):
    restricted_foods = RestrictedFoodSerializer(many=True, read_only=True)
    
    class Meta:
        model = DietaryStyle
        fields = ['id', 'name', 'description', 'restricted_foods'] 