from django.db import models

# Create your models here.
class TimeAutomatic(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="create")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="update")

    class Meta:
        abstract = True

    def __str__(self):
        return ""

class Pets(TimeAutomatic):
    type = models.CharField(max_length=255,null=True,blank=True,help_text="choose type of pet",verbose_name="type name")

    class Meta:
        db_table = "tbl_pets"
        # verbose_name = "laaaaa"
        verbose_name_plural = "pet"

    def __str__(self):
        return self.type

class Cat(TimeAutomatic):
    type = models.ForeignKey(Pets,null=True,blank=True,on_delete=models.DO_NOTHING,related_name="cat")
    country = models.CharField(max_length=255,null=True,blank=True,help_text="country's cat")
    name = models.CharField(max_length=255,null=True,blank=True,help_text="cat's name")
    birthday = models.DateField(null=True,blank=True,help_text="birth of day")
    color = models.CharField(max_length=255,null=True,blank=True,help_text="cat's color")
    price = models.FloatField(null=True,blank=True,default=0.0,help_text="cat's price")

    class Meta:
        db_table = "tbl_cat"
        verbose_name_plural = "cat"

    def __str__(self):
        return "cat_"+self.name

class Dog(TimeAutomatic):
    type = models.ForeignKey(Pets,null=True,blank=True,on_delete=models.DO_NOTHING,related_name="dog")
    country = models.CharField(max_length=255,null=True,blank=True,help_text="country's dog")
    name = models.CharField(max_length=255,null=True,blank=True,help_text="dog's name")
    birthday = models.DateField(null=True,blank=True,help_text="birth of day")
    color = models.CharField(max_length=255,null=True,blank=True,help_text="dog's color")
    price = models.FloatField(null=True,blank=True,default=0.0,help_text="dog's price")

    class Meta:
        db_table = "tbl_dog"
        verbose_name_plural = "dog"

    def __str__(self):
        return "dog_"+self.name

class Fish(TimeAutomatic):
    type = models.ForeignKey(Pets,null=True,blank=True,on_delete=models.DO_NOTHING,related_name="fish")
    country = models.CharField(max_length=255,null=True,blank=True,help_text="country's fish")
    name = models.CharField(max_length=255,null=True,blank=True,help_text="fish's name")
    birthday = models.DateField(null=True,blank=True,help_text="birth of day")
    color = models.CharField(max_length=255,null=True,blank=True,help_text="fish's color")
    price = models.FloatField(null=True,blank=True,default=0.0,help_text="fish's price")

    class Meta:
        db_table = "tbl_fish"
        verbose_name_plural = "fish"

    def __str__(self):
        return "fish_"+self.name