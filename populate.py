from market_app import db
from market_app.models.user_model import User
from market_app.models.item_model import Item


db.drop_all()
db.create_all()

item1 = Item(name="Two Feet", price=150, performer="Two Feet", description="Genre: Electronic music. 2021 year.")
item2 = Item(name="Break Stuff", price=200, performer="Limp Bizkit", description="Genre: Nu metal. 2000 year.")
item3 = Item(name="Something", price=100, performer="The Beatles", description="Genre: Rock. 1969 year.")
item4 = Item(name="Yellow Submarine", price=80, performer="The Beatles", description="Genre: Folk, pop. 1968 year.")
item5 = Item(name="Californication", price=220, performer="Red Hot Chili Peppers", description="Genre: Alternative rock. 1999 year.")
item6 = Item(name="Crash", price=300, performer="Neovaii", description="Genre: Dance/electronic music. 2018 year.")
item7 = Item(name="Diry", price=160, performer="grandson", description="Genre: Alternative/Indie. 2020 year.")
item8 = Item(name="My Type", price=110, performer="Saint Motel", description="Genre: Alternative/Indie, Pop. 2014 year.")
item9 = Item(name="A Good Song Never Dies", price=250, performer="Saint Motel", description="Genre: Alternative/Indie, Pop. 2021 year.")
item10 = Item(name="Dangerous", price=50, performer="Big Data", description="Genre: Alternative/Indie. 2014 year.")

new_user = User(username='test_user', email='test_user@gmail.com', plain_password='qwerty1')

db.session.add(item1)
db.session.add(item2)
db.session.add(item3)
db.session.add(item4)
db.session.add(item5)
db.session.add(item6)
db.session.add(item7)
db.session.add(item8)
db.session.add(item9)
db.session.add(item10)
db.session.add(new_user)

db.session.commit()