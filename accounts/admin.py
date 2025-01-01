from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','age','email','is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None,
         {'fields':('age',)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": ("username", "email","age", "password1", "password2"),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)