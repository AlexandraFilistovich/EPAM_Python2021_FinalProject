from market_app import db


class Item(db.Model):
    """
    Item of shop database table.

    ___Columns___
        id: primary key
        name
        price
        performer
        description
        owner: foreign key to User table

    ___Relationships___
        owned_user
    
    ___Methods___
        __repr__
        plain_password.getter
        plain_password.setter
        buy_by
    """
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), \
                    nullable=False, \
                    unique=True)
    price = db.Column(db.Integer(), \
                      nullable=False)
    performer = db.Column(db.String(length=30), \
                    nullable=False)
    description = db.Column(db.String(length=1024), \
                            nullable=False, \
                            unique=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item: {self.name}'
    
