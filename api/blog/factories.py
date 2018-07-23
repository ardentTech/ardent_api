import factory
from factory import Faker


class PostFactory(factory.DjangoModelFactory):

    body = Faker("pystr", max_chars=256)
    is_public = Faker("pybool")
    title = Faker("pystr", max_chars=128)

    class Meta:
        model = "blog.Post"
