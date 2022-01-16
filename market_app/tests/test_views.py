import http
from flask import url_for

from market_app.tests.test_case_base import TestCaseBase


class TestViews(TestCaseBase):
    def test_homepage(self):
        response = self.client.get(url_for('home_load'))
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_login(self):
        pass
