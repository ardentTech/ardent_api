from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import CreatedMixin, UpdatedMixin


class Product(CreatedMixin, UpdatedMixin):

    # description
    serial_number = models.CharField(
        _("serial number"),
        max_length=8)
    # etsy id? etsy_url @property

    class Meta:
        ordering = ["serial_number"]

    def __str__(self):
        return "Product: {}".format(self.serial_number)


class ProductImage(CreatedMixin, UpdatedMixin):

    image = models.ImageField(
        _("image"),
        upload_to="commerce/product_image")
    product = models.ForeignKey(
        "commerce.Product",
        on_delete=models.CASCADE,
        related_name="images")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return "ProductImage: {}".format(self.id)
