from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomeUser(AbstractUser):
    email = models.EmailField('ایمیل', blank=False,null=False,unique=True)