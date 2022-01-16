import http
from urllib import response

from market_app.tests.test_case_base import TestCaseBase


class TestViews(TestCaseBase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
