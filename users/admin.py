from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm,CustomUserCreationForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = UserAdmin.fieldsets 
    add_fieldsets = UserAdmin.add_fieldsets 

    list_display = (
        'username',
        'email',
        'is_staff',
    )


admin.site.register(CustomUser,CustomUserAdmin)