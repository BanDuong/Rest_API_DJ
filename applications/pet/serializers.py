from rest_framework import serializers
from .models import Pets,Cat,Dog,Fish

#self.context.request()

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
    cats = CatSerializer(many=True)
    dogs = DogSerializer(many=True)
    fishes = FishSerializer(many=True)
    class Meta:
        model = Pets
        fields = ['id','type','cats','dogs','fishes']
        extra_kwargs = {
            'type': {'required':False,'allow_null':True}
        }

    def validate_type(self,type):  # cu phap: validated_{field_name}
        return name
