from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                "serial_number",
            )
        }),
        ("Meta", {
            "classes": ("grp-collapse",),
            "fields": ("created", "id", "updated",)
        })
    )
    list_display = (
        "id",
        "serial_number",
        "created",
        "updated",
    )
    list_filter = ()
    readonly_fields = ("created", "id", "updated",)


admin.site.register(Product, ProductAdmin)
