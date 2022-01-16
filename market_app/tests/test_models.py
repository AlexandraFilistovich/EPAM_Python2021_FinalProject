from market_app.tests.test_case_base import TestCaseBase
from market_app.models.user_model import User
from market_app.models.item_model import Item


class TestModules(TestCaseBase):
    """
    Checks rows added by initialising test script.
    """
    def test_user_model(self):
        self.assertEqual(User.query.filter_by(username='Sasha').count(), 1)
    
    def test_item_model(self):
        self.assertEqual(User.query.filter_by(name='Song1').count(), 1)
        self.assertEqual(User.query.filter_by(name='Song2').count(), 1)