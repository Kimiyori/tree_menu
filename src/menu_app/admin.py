from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Menu, Item


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Menu admin"""

    fields = ("name",)


@admin.register(Item)
class MenuItemAdmin(MPTTModelAdmin):
    """Item admin"""

    list_display = ("id", "menu", "url", "parent")
