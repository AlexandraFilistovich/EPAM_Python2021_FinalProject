import unittest
from importlib_metadata import email

from market_app import app, db
from market_app.models.user_model import User
from market_app.models.item_model import Item


class TestCaseBase(unittest.TestCase):
    def setUp(self):
        """
        Will be called before every test.
        """
        app.config['TESTING'] = True
        self.client = app.test_client()

        db.create_all()
        
        user = User(username='test_user', email='test_user@gmail.com', plain_password='qwerty1')
        item1 = Item(name='Song1', performer='Performer1', price=500, description='Description of song1.')
        item2 = Item(name='Song2', performer='Performer2', price=1100, description='Description of song2.')

        db.session.add(user)
        db.session.add(item1)
        db.session.add(item2)
        
        db.session.commit()
    
    def tearDown(self):
        """
        Will be called after every test.
        """
        db.session.remove()
        db.drop_all()
