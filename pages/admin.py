from django.contrib import admin
from django.utils.html import mark_safe

from .models import GalleryImage, Service


@admin.register(GalleryImage)
class galleryImageAdmin(admin.ModelAdmin):
    list_display = ("image", "preview", "alt")

    def preview(self, obj):
        return mark_safe(
            '<img src="/media/%s" width="150" height="150" />' % (obj.image)
        )

    preview.short_description = "Предпросмотр"


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price")

    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    def has_add_permission(self, request) -> bool:
        return False
