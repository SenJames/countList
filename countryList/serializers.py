from rest_framework import serializers
from .models import CountryModel

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        fields = ['country', 'created', 'continent', 'iso2', 'long', 'lat']


