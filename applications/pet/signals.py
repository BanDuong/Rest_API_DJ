from django.db.models.signals import  pre_save,post_save
from django.dispatch import receiver
from .models import Fish

# register in apps.py

@receiver(signal=pre_save,sender=Fish)
def ResponseCreat(sender,**kwargs):
    print(222)

@receiver(signal=post_save,sender=Fish)
def ResponsePost(sender,**kwargs):
    print(111)
