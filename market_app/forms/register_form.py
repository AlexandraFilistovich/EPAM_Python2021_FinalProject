from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

from market_app.models.user_model import User


class RegisterForm(FlaskForm):
    """
    Class RegisterForm defines form fields with their data requirements
    and form validators.

    ___Fields___
        username
        email
        password
        password_check
        submit
    
    ___Methods___
        validate_username
        validate_email
    """
    
    username = StringField(label='Username:', \
                        validators=[Length(min=2, max=30), \
                                    DataRequired()])
    email = StringField(label='Email Adress:', \
                        validators=[Email(), \
                                    DataRequired()])
    password = PasswordField(label='Password:', \
                        validators=[Length(min=6, max=60), \
                                    DataRequired()])
    password_check = PasswordField(label='Confirm Password:', \
                        validators=[EqualTo('password'), \
                                    DataRequired()])
    submit = SubmitField(label='Create account')

    def validate_username(self, username_to_check):
        """
        Username validator. Checks if username already exists.

        :param username_to_check: username user input
        :return: None
        """
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists.')
    
    def validate_email(self, email_to_check):
        """
        Email adress validator. Checks if email already exists.

        :param email_to_check: adress user input
        :return: None
        """
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('Email already exists.')
