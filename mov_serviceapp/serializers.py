from rest_framework import serializers
from .models import Film, Projekcija, Sala



class filmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


class projekcijaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projekcija
        fields = '__all__'


class salaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'
