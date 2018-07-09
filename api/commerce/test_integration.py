from hamcrest import assert_that, equal_to
from rest_framework.status import HTTP_200_OK

from utils.test_integration import GraphTestCase


class ProductTestCase(GraphTestCase):

    def test_get_products(self):
        response = self.query("{products{serialNumber}}")
        assert_that(response.status_code, equal_to(HTTP_200_OK))


class ProductImageTestCase(GraphTestCase):

    def test_get_product_images(self):
        response = self.query("{productImages{id,image,product{id}}}")
        assert_that(response.status_code, equal_to(HTTP_200_OK))
