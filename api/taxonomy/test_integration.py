from hamcrest import assert_that, equal_to
from rest_framework.status import HTTP_200_OK

from utils.test_integration import GraphTestCase


class TagTestCase(GraphTestCase):

    def test_get_products(self):
        response = self.query("{tags{name}}")
        assert_that(response.status_code, equal_to(HTTP_200_OK))
