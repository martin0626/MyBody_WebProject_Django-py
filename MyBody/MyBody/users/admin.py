from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from MyBody.users.models import Profile, MyBodyUser


@admin.register(MyBodyUser)
class MyBodyUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    search_fields = ('username', 'email')
    ordering = ('username', 'email',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login',)}),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
