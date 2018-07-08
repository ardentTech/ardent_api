from django.db import models
from django.utils.translation import ugettext_lazy as _


class CreatedMixin(models.Model):

    created = models.DateTimeField(
        _("created"),
        auto_now_add=True)

    class Meta:
        abstract = True


class UpdatedMixin(models.Model):

    updated = models.DateTimeField(
        _("updated"),
        auto_now=True)

    class Meta:
        abstract = True


class Product(CreatedMixin, UpdatedMixin):

    # description
    serial_number = models.CharField(_("name"), max_length=64)
    # etsy url

    class Meta:
        ordering = ["serial_number"]

    def __str__(self):
        return "Product: {}".format(self.serial_number)
