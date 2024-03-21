from rest_framework import serializers
from .models import Equipment, Brand, Type


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = 'name',

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = 'name',


class EquipmentSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    type = TypeSerializer(read_only=True)

    class Meta:
        model = Equipment
        fields = (
            'id',
            'reference',
            'memory',
            'disk',
            'brand',
            'type',

        )
