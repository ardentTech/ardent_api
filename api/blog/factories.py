import factory
from factory import Faker


class PostFactory(factory.DjangoModelFactory):

    title = Faker("pystr", max_chars=128)

    class Meta:
        model = "blog.Post"
