from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Status  # مدل خود را وارد کنید

@receiver(post_migrate)
def create_initial_instances(sender, **kwargs):
    if sender.name == 'todolist':
        
        if not Status.objects.exists():
            Status.objects.create(name='انجام نشده')
            Status.objects.create(name='درحال انجام')
            Status.objects.create(name='انجام شده')
