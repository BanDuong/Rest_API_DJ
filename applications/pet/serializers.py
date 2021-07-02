from rest_framework import serializers
from .models import Pets,Cat,Dog,Fish

class CatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cat
        fields = "__all__"

class DogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = "__all__"

class FishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fish
        fields = "__all__"

class PetSerializer(serializers.ModelSerializer):
    cat = CatSerializer(many=True)
    dog = DogSerializer(many=True)
    fish = FishSerializer(many=True)
    class Meta:
        model = Pets
        fields = ['id','type','cat','dog','fish']