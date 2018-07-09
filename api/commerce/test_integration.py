from hamcrest import assert_that, equal_to
from rest_framework.status import HTTP_200_OK

from commerce.factories import ProductFactory
from utils.test_integration import GraphTestCase


class ProductTestCase(GraphTestCase):

    def test_get_products(self):
        response = self.query("{products{serialNumber}}")
        assert_that(response.status_code, equal_to(HTTP_200_OK))
