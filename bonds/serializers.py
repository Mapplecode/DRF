from rest_framework import serializers
from .models import Bonds


# Bonds Serializer
class BondSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonds
        fields = '__all__'

    def get_serializer_class(self,queryset):
        qs = Bonds.objects.all()
        qs_json = Bonds.serialize('json', qs)
        print(qs_json)

        return qs_json

class BondCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bonds
        fields = '__all__'

    def create(self, validated_data):
        bond = Bonds.objects.create(validated_data['name'], validated_data['symbol'], validated_data['price'])
        return bond