from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from MyBody.navigation.models import Navigation


@admin.register(Navigation)
class NavAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['url_name']
