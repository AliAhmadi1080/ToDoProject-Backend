from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Status, Tag
from django.contrib.auth import get_user_model
import uuid
User = get_user_model()

@receiver(post_save, sender=User)
def createstatus(instance, created:bool, **kwargs):
    if created:
        Status.objects.create(user=instance,name='انجام نشده')
        Status.objects.create(user=instance,name='درحال انجام')
        Status.objects.create(user=instance,name='انجام شده')

def create_slug(instance:Tag):
    slug = 'this-is-slug'
    slug += '-'+str(instance.id)
    return slug

@receiver(post_save, sender=Tag)
def createstatus(instance:Tag, created:bool, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
        instance.save()
        