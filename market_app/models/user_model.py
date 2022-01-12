from market_app import db, bcrypt,login_manager
from sqlalchemy.orm import backref
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """
    User database table.

    ___Columns___
        id: primary key
        username
        email
        password
        budget
        items: foreign key to Items table
    
    ___Relationships___
        items

    ___Methods___
        __repr__
        plain_password.getter
        plain_password.setter
        check_password_input
        budget_check
    """
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), \
                          nullable=False, \
                          unique=True)
    email = db.Column(db.String(length=50), \
                      nullable=False, \
                      unique=True)
    password = db.Column(db.String(length=60), \
                         nullable=False)
    budget = db.Column(db.Integer(), \
                       nullable=False, \
                       default=1000)
    items = db.relationship('Item', \
                            backref='owned_user', \
                            lazy=True)
 
    def __repr__(self):
        return f'User: {self.username}'
    
    def budget_repr(self):
        """
        Represents budget data with thousand whitespases.
        """
        budget = str(self.budget)
        budget_normalized = ''
        length = len(budget)
        if length >= 4:
            for i in range(length):
                if (i - length % 3) % 3 == 2:
                    budget_normalized += budget[i] + ' '
                else:
                    budget_normalized += budget[i]
            return f"{budget_normalized.rstrip()}$"
        else:
            return f"{budget}$"

    @property
    def plain_password(self):
        """
        Getter of plain_password.

        :return: plain_password
        """
        return self.plain_password
    
    @plain_password.setter
    def plain_password(self, plain_text_password):
        """
        Setter of plain_password. On set encrypts password and ads it to instance.

        :param plain_text_password: Password entered by user.
        :return: None
        """
        self.password = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
