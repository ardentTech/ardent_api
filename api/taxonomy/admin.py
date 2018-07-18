from django.contrib import admin

from .models import Tag


class TagAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                "name",
            )
        }),
        ("Meta", {
            "classes": ("grp-collapse",),
            "fields": ("created", "id", "updated",)
        })
    )
    list_display = (
        "id",
        "name",
        "created",
        "updated",
    )
    readonly_fields = ("created", "id", "updated",)


admin.site.register(Tag, TagAdmin)
