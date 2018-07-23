from random import randint

from django.conf import settings
from django.core.management.base import BaseCommand

from blog.factories import PostFactory
from commerce.factories import ProductFactory, ProductImageFactory
from contact.factories import ContactMessageFactory
from taxonomy.factories import TagFactory


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        if settings.DEBUG:
            self._create("tags")
            self._create("posts")
            products = self._create("products")
            self._create("product_images", products=products)
            self._create("contact_messages")

    # PRIVATE

    def _create(self, name, **kwargs):
        records = getattr(self, "_create_" + name)(**kwargs)
        print("created {0} {1}".format(len(records), name))
        return records

    def _create_contact_messages(self, **kwargs):
        return [ContactMessageFactory.create() for n in range(randint(0, 10))]

    def _create_posts(self, **kwargs):
        return [PostFactory.create() for n in range(randint(0, 10))]

    def _create_products(self, **kwargs):
        return [ProductFactory.create() for n in range(randint(0, 10))]

    def _create_product_images(self, **kwargs):
        return [ProductImageFactory.create(product=p) for p in kwargs.get("products")]

    def _create_tags(self, **kwargs):
        return [TagFactory.create() for n in range(randint(0, 10))]
