import json
from urllib.parse import urlencode

from rest_framework.test import APITestCase


class GraphTestCase(APITestCase):

    ENDPOINT = "/graph?{}"
    HEADERS = {"HTTP_ACCEPT": "application/json"}

    def data_from(self, response):
        return json.loads(response.content.decode("utf-8"))["data"]

    def mutate(self, query):
        return self.client.post(
            self.ENDPOINT.format(urlencode({"query": query})), **self.HEADERS)

    def query(self, query):
        return self.client.get(
            self.ENDPOINT.format(urlencode({"query": query})), **self.HEADERS)
