from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from . import models

class CustomeUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = models.CustomeUser
        fields = UserCreationForm.Meta.fields + ('email',)

class CustomeUserUserChangeForm(UserChangeForm):

    class Meta:
        model = models.CustomeUser
        fields = UserChangeForm.Meta.fields