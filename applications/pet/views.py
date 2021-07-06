from django.shortcuts import render
from rest_framework import generics
from .serializers import PetSerializer,DogSerializer,CatSerializer,FishSerializer
from .models import Pets,Dog,Cat,Fish
from renderers import renderPets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import authentication, permissions
import json

def index(request):
    return render(request,"homepage/base.html",{})

class PetAPI(generics.ListCreateAPIView):
    serializer_class = PetSerializer
    # renderer_classes = renderPets

    def get_queryset(self):
        return Pets.objects.prefetch_related('cats')\
            .prefetch_related('dogs')\
            .prefetch_related('fishes').all()

class CatAPI(generics.ListCreateAPIView):
    serializer_class = CatSerializer

    def get_queryset(self):
        return Cat.objects.all()

class DogAPI(generics.ListCreateAPIView):
    serializer_class = DogSerializer

    def get_queryset(self):
        return Dog.objects.all()

class FishAPI(generics.ListCreateAPIView):
    serializer_class = FishSerializer

    def get_queryset(self):
        return Fish.objects.all()

class ListUsers(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self,request):
        users = [user.username for user in User.objects.all()]
        return Response(data=users)
