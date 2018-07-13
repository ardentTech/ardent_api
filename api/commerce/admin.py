from django.contrib import admin

from .models import Product, ProductImage


class ProductImageInline(admin.TabularInline):

    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                "serial_number",
                "etsy_id",
            )
        }),
        ("Meta", {
            "classes": ("grp-collapse",),
            "fields": ("created", "id", "updated",)
        })
    )
    inlines = (ProductImageInline,)
    list_display = (
        "id",
        "serial_number",
        "etsy_id",
        "created",
        "updated",
    )
    list_filter = ()
    readonly_fields = ("created", "id", "updated",)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
