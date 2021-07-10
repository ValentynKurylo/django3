from rest_framework.serializers import ModelSerializer
from .models import CountryModel

class CountrySerializer(ModelSerializer):
    class Meta:
        model = CountryModel
        fields = '__all__'
