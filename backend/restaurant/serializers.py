from rest_framework import serializers
from .models import Restaurant

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'