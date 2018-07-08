from urllib.parse import urlencode

from hamcrest import assert_that, equal_to
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase

from commerce.factories import ProductFactory


class ProductTestCase(APITestCase):

    def test_get_products(self):
        query = "{products{serialNumber}}"
        response = self.client.get("/graph?{}".format(urlencode({"query": query})), HTTP_ACCEPT="application/json")

        assert_that(response.status_code, equal_to(HTTP_200_OK))
