import factory
from factory import Faker


class TagFactory(factory.DjangoModelFactory):

    name = Faker("pystr", max_chars=128)

    class Meta:
        model = "taxonomy.Tag"
