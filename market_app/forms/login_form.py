from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired


class LoginForm(FlaskForm):
    """
    Class LoginForm defines form fields with their data requirements
    and form validators.

    ___Fields___
        username
        password
        submit
    
    ___Methods___
        validate_username
        validate_password
    """
    
    username = StringField(label='Username:', \
                        validators=[Length(min=2, max=30), \
                                    DataRequired()])
    password = PasswordField(label='Password:', \
                        validators=[DataRequired()])
    submit = SubmitField(label='Log in')