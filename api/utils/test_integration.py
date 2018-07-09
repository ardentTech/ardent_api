from urllib.parse import urlencode

from rest_framework.test import APITestCase


class GraphTestCase(APITestCase):

    ENDPOINT = "/graph?{}"
    HEADERS = {"HTTP_ACCEPT": "application/json"}

    def query(self, query):
        return self.client.get(
            self.ENDPOINT.format(urlencode({"query": query})), **self.HEADERS)
