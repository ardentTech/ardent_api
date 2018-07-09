from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import CreatedMixin, UpdatedMixin


class Product(CreatedMixin, UpdatedMixin):

    # description
    serial_number = models.CharField(_("serial number"), max_length=8)
    # etsy url

    class Meta:
        ordering = ["serial_number"]

    def __str__(self):
        return "Product: {}".format(self.serial_number)
