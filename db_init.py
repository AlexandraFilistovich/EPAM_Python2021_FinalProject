from market_app import db
from market_app.models.user_model import User
from market_app.models.item_model import Item


db.drop_all()
db.create_all()

item1 = Item(name="Song_1", price=100, performer="G", description="1")
item2 = Item(name="Song_2", price=200, performer="G", description="2")
item3 = Item(name="Song_3", price=300, performer="G", description="3")
item4 = Item(name="Song_4", price=400, performer="G", description="4")
item5 = Item(name="Song_5", price=500, performer="G", description="-2")
item6 = Item(name="Song_6", price=600, performer="G", description="3498")
item7 = Item(name="Song_7", price=1, performer="G", description="7")
item8 = Item(name="Song_8", price=2000000, performer="G", description="8")

new_user = User(username='Sasha', email='alexafiliho@gmail.com', plain_password='13091192')

db.session.add(item1)
db.session.add(item2)
db.session.add(item3)
db.session.add(item4)
db.session.add(item5)
db.session.add(item6)
db.session.add(item7)
db.session.add(item8)
db.session.add(new_user)

db.session.commit()