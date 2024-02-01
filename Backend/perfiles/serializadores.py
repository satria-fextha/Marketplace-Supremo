from rest_framework import serializers
from .models import Agricultor, Ganadero, Consumidor

class AgricultorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agricultor
        fields = '__all__'

class GanaderoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ganadero
        fields = '__all__'

class ConsumidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumidor
        fields = '__all__'
