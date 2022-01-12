from market_app import bcrypt, login_manager
from market_app.models.user_model import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def check_password_input(user, input_password):
    """
    Function checks entered in login form password is 
    same to stored in table encrypted password.
    :param input_password: password entered by user
    :return: True if password is correct, otherwise returns False.
    """
    return bcrypt.check_password_hash(user.password, input_password)

def budget_check(user, item):
    return user.budget - item.price >= 0