from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Pets,Cat,Dog,Fish
from django.db.models import Q


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
        fields = ['id','country','name','color','price']
        extra_kwargs = {
            'name': {'required':False,'allow_null':True}
        }
    #--------------display_exception_in_log_tag(API_interface/Postman)----------------#
    def validate_name(self,name):
        try:
            Fish.objects.get(name=name)
            raise ValidationError(detail="Name đã tồn tại", code="name_existed")
        except Fish.DoesNotExist:
            return name
        except Fish.MultipleObjectsReturned:
            raise ValidationError(detail="Thís name already exists!", code="name_existed")
        except Exception as e:
            raise e


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
        pass
