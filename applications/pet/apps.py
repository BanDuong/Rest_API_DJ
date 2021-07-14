from django.apps import AppConfig


class PetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.pet'
    verbose_name = "PET"
    
    def ready(self):
        import applications.pet.signals