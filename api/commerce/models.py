from django.db import models
from django.utils.translation import ugettext_lazy as _

from taxonomy.models import TaggedMixin
from utils.models import CreatedMixin, UpdatedMixin


class Product(CreatedMixin, TaggedMixin, UpdatedMixin):

    # description
    etsy_id = models.IntegerField(
        _("Etsy ID"),
        blank=True,
        null=True)
    name = models.CharField(
        _("name"),
        default="@todo",
        max_length=128)
    serial_number = models.CharField(
        _("serial number"),
        max_length=8)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return "Product: {}".format(self.name)

    @property
    def etsy_url(self):
        if self.etsy_id is None:
            return None
        return "https://www.etsy.com/listing/{}".format(self.etsy_id)


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
        verbose_name_plural = _("Product Images")

    def __str__(self):
        return "ProductImage: {}".format(self.id)
