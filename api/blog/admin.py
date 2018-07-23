from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                "title",
                "is_public",
                "body",
                "tags",
            )
        }),
        ("Meta", {
            "classes": ("grp-collapse",),
            "fields": ("created", "id", "updated",)
        })
    )
    filter_horizontal = ("tags",)
    list_display = (
        "id",
        "title",
        "is_public",
        "created",
        "updated",
    )
    list_filter = ()
    readonly_fields = ("created", "id", "updated",)


admin.site.register(Post, PostAdmin)
