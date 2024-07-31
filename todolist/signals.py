from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Status  
from django.contrib.auth import get_user_model
User = get_user_model()

@receiver(post_save, sender=User)
def createstatus(instance, created:bool, **kwargs):
    if created:
        Status.objects.create(user=instance,name='انجام نشده')
        Status.objects.create(user=instance,name='درحال انجام')
        Status.objects.create(user=instance,name='انجام شده')