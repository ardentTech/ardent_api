from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe

from .models import Product, ProductImage


class AdminImageMixin(object):

    def to_html(self, obj, height=100):
        width = obj.width / (obj.height / height)
        return mark_safe(
            '<img src="{}" width="{}" height="{}">'.format(obj.url, width, height))


class AdminImageWidget(AdminImageMixin, AdminFileWidget):

    def render(self, name, value, attrs=None):
        output = []
        if value is not None:
            output.append(self.to_html(value))
        output.append(super().render(name, value, attrs))
        return mark_safe("".join(output))


class ProductImageForm(forms.ModelForm):

    class Meta:
        fields = "__all__"
        model = ProductImage
        widgets = {"image": AdminImageWidget}


class ProductImageInline(admin.TabularInline):

    form = ProductImageForm
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                "name",
                "serial_number",
                "status",
                "etsy_id",
                "tags",
            )
        }),
        ("Meta", {
            "classes": ("grp-collapse",),
            "fields": ("created", "id", "updated",)
        })
    )
    filter_horizontal = ("tags",)
    inlines = (ProductImageInline,)
    list_display = (
        "id",
        "name",
        "serial_number",
        "status",
        "etsy_id",
        "created",
        "updated",
    )
    list_filter = ()
    readonly_fields = ("created", "id", "updated",)


class ProductImageAdmin(AdminImageMixin, admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                "image",
                "product",
            )
        }),
        ("Meta", {
            "classes": ("grp-collapse",),
            "fields": ("created", "id", "updated",)
        })
    )
    list_display = (
        "id",
        "image_preview",
        "width",
        "height",
        "filename",
        "product",
        "created",
        "updated",
    )
    list_filter = ()
    readonly_fields = ("created", "id", "updated",)

    def filename(self, obj):
        return obj.image.name

    def height(self, obj):
        return obj.image.height

    def image_preview(self, obj):
        return self.to_html(obj.image, height=75)

    def width(self, obj):
        return obj.image.width


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
