from hamcrest import assert_that, equal_to
from rest_framework.status import HTTP_200_OK

from utils.test_integration import GraphTestCase


class PostTestCase(GraphTestCase):

    def test_get_posts(self):
        response = self.query("{posts{title}}")
        assert_that(response.status_code, equal_to(HTTP_200_OK))

    # @todo `is_public` and post count
