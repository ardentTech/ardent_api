from django.contrib import admin

from .models import ContactMessage


class ContactMessageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                "body",
                "email",
                "name",
            )
        }),
        ("Meta", {
            "classes": ("grp-collapse",),
            "fields": ("created", "id",)
        })
    )
    list_display = (
        "id",
        "name",
        "email",
        "created",
    )
    list_filter = ()
    readonly_fields = ("created", "id",)


admin.site.register(ContactMessage, ContactMessageAdmin)
