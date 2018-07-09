import factory
from factory import Faker


class ProductFactory():

    serial_number = Faker("pystr", max_chars=8)

    class Meta:
        model = "commerce.Product"


class ProductImageFactory():

    image = factory.django.ImageField(color="blue", height=400, width=400)
    product = factory.SubFactory(ProductFactory)

    class Meta:
        model = "commerce.ProductImage"
