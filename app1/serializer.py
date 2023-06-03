from rest_framework import serializers
from .models import (Product,PackingMaterial,
                     RawMaterial,ManPower, Energycost)

from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    ins = Product()
    def validate_ingredients_list(self, value):
        content = value[0]['content']
        quantity = value[0]['quantity']
        is_product = bool(value[0]['is_product'])
        self.ins.add_ingredients(content, quantity, is_product)
        return value

class ManPowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManPower
        fields = "__all__"

    instance = ManPower()
    def validate_add_packing(self, value):
        quantity = value[0]['quantity']
        unit = value[0]['unit']
        amount = value[0]['amount']
        self.instance.add_packing(quantity,unit,amount)
        return value

class PackingMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackingMaterial
        fields = "__all__"

class RawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = "__all__"

class EnergycostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Energycost
        fields = "__all__"

#user creation
class SuperUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if User.objects.count() >= 10:
            raise serializers.ValidationError('User Creation Limit Reached')

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
        )
        return user

class LoginViewSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 500)
    password = serializers.CharField(write_only = True)