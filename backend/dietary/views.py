from rest_framework import viewsets
from .models import DietaryStyle, RestrictedFood
from .serializers import DietaryStyleSerializer, RestrictedFoodSerializer

class DietaryStyleViewSet(viewsets.ModelViewSet):
    queryset = DietaryStyle.objects.all()
    serializer_class = DietaryStyleSerializer

class RestrictedFoodViewSet(viewsets.ModelViewSet):
    queryset = RestrictedFood.objects.all()
    serializer_class = RestrictedFoodSerializer 