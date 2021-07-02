from django.contrib import admin
from .models import Pets,Cat,Dog,Fish

# Register your models here.

@admin.register(Pets)
class PetsAdmin(admin.ModelAdmin):
    list_display = ('id','type','created_at','updated_at')
    list_filter = ('id','type','created_at','updated_at')
    search_fields = ('id','type','created_at','updated_at')

@admin.register(Cat)
class PetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'country' , 'name' , 'birthday' , 'color' , 'price' , 'created_at', 'updated_at')
    list_filter = ('id', 'type', 'country' , 'name' , 'birthday' , 'color' , 'price' , 'created_at', 'updated_at')
    search_fields = ('id', 'type', 'country' , 'name' , 'birthday' , 'color' , 'price' , 'created_at', 'updated_at')

@admin.register(Dog)
class PetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'country', 'name', 'birthday', 'color', 'price', 'created_at', 'updated_at')
    list_filter = ('id', 'type', 'country', 'name', 'birthday', 'color', 'price', 'created_at', 'updated_at')
    search_fields = ('id', 'type', 'country', 'name', 'birthday', 'color', 'price', 'created_at', 'updated_at')

@admin.register(Fish)
class PetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'country', 'name', 'birthday', 'color', 'price', 'created_at', 'updated_at')
    list_filter = ('id', 'type', 'country', 'name', 'birthday', 'color', 'price', 'created_at', 'updated_at')
    search_fields = ('id', 'type', 'country', 'name', 'birthday', 'color', 'price', 'created_at', 'updated_at')