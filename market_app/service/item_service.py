from market_app import db


def buy_by(item, user):
    item.owner = user.id
    user.budget -= item.price
    item.price -= item.price // 10
    db.session.commit()

def sell_by(item, user):
    user.budget += item.price
    item.owner = None
    db.session.commit()