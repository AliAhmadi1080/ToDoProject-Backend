from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomeUserCreationForm, CustomeUserUserChangeForm
from django.utils.translation import gettext_lazy as _
from . import models


class CustomeUserAdmin(UserAdmin):
    add_form = CustomeUserCreationForm
    form = CustomeUserUserChangeForm
    model = models.CustomeUser
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "email"),
            },
        ),
    )
admin.site.register(models.CustomeUser, CustomeUserAdmin)