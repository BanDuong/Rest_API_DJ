from django.shortcuts import render
from rest_framework import generics
from .serializers import PetSerializer,DogSerializer,CatSerializer,FishSerializer
from .models import Pets,Dog,Cat,Fish
from rest_framework import status
from rest_framework.response import Response
from common.errors import *
from django.views.generic import ListView
from .models import Fish

class index(ListView):

    def get(self,request):
        objs = Fish.objects.all()

        return render(request=request,template_name="homepage/base.html",context={"objs":objs})

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
    queryset = Fish.objects.all()
    serializer_class = FishSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            raise ErrCannotCreateEntity(entity="New Fish",err=e)


class getRetrieveFish(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

