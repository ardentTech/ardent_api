from django.core import mail

from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from contact.models import ContactMessage
from utils.test_integration import GraphTestCase


class ContactMessageTestCase(GraphTestCase):

    def test_post_invalid_data(self):
        query = """
mutation {
    createContactMessage(input:{}) { body email name }
}
"""
        self.assertEqual(ContactMessage.objects.count(), 0)
        response = self.mutate(query)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_post_valid_data(self):
        query = """
mutation {
    createContactMessage(input:{body: "bar", email: "foo@bar.com", name: "foo"}) { body email name }
}
"""
        self.assertEqual(ContactMessage.objects.count(), 0)
        self.assertEqual(len(mail.outbox), 0)

        response = self.mutate(query)

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(ContactMessage.objects.count(), 1)
        data = self.data_from(response)["createContactMessage"]
        self.assertEqual(data["email"], "foo@bar.com")
        self.assertEqual(data["name"], "foo")
        self.assertEqual(len(mail.outbox), 1)
