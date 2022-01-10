from sqlalchemy.orm import backref
from packages_dir import db, bcrypt, login_manager
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
    
    def check_password_input(self, input_password):
        """
        Function checks entered in login form password is 
        same to stored in table encrypted password.

        :param input_password: password entered by user
        :return: True if password is correct, otherwise returns False.
        """
        return bcrypt.check_password_hash(self.password, input_password)


class Item(db.Model):
    """
    Item of shop database table.

    ___Columns___
        id: primary key
        name
        price
        barcode
        description
        owner: foreign key to User table

    ___Relationships___
        owned_used
    
    ___Methods___
        __repr__
        plain_password.getter
        plain_password.setter
    """
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), \
                    nullable=False, \
                    unique=True)
    price = db.Column(db.Integer(), \
                      nullable=False)
    barcode = db.Column(db.String(length=12), \
                        nullable=False, \
                        unique=True)
    description = db.Column(db.String(length=1024), \
                            nullable=False, \
                            unique=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item: {self.name}'
