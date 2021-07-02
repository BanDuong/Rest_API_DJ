from django.urls import path
from . import views

urlpatterns = [
    path('pet/',views.PetAPI.as_view(),name="pet_api"),
    path('cat/',views.CatAPI.as_view(),name="cat_api"),
    path('dog/',views.DogAPI.as_view(),name="dog_api"),
    path('fish/',views.FishAPI.as_view(),name="fish_api"),
]
