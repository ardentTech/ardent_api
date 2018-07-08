from factory import Faker


class ProductFactory():

    serial_number = Faker("pystr", max_chars=8)

    class Meta:
        model = "commerce.Product"
