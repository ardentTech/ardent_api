import factory
from factory import Faker


class ContactMessageFactory(factory.DjangoModelFactory):

    body = Faker("pystr", max_chars=256)
    email = "tester@test.com"
    name = Faker("pystr", max_chars=128)

    class Meta:
        model = "feedback.ContactMessage"
