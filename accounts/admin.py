from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'phone_number', 'is_botanist')

    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'full_name', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'is_botanist', 'last_login')}),
    )

    add_fieldsets = (
        (None, {'fields':('email','phone_number','full_name','is_botanist', 'password1', 'password2')}),
    )

    search_fields = ('email',)
    ordering = ('full_name',)
    list_filter = ('is_botanist',)
    filter_horizontal = ()

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)