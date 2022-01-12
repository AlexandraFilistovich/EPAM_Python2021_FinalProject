from flask import render_template, redirect, url_for, flash
from flask_login import login_user

from market_app import app
from market_app.models.user_model import User
from market_app.service.user_service import check_password_input
from market_app.forms.login_form import LoginForm


@app.route('/login', methods = ['Get', 'POST'])
def login_load():
    """
    Function loads login page, checks login form validations and
    redirects user on successfull login.
    """
    form = LoginForm()
    if form.validate_on_submit():
        input_user = User.query.filter_by(username=form.username.data).first()
        if input_user and check_password_input(user=input_user,
                                     input_password=form.password.data):
            login_user(input_user)
            flash(f'You are successfully logged in! Hello, {input_user.username}!', \
                  category='success')
            return redirect(url_for('market_load'))
        else:
            flash('Username or password is incorrect. Please try again.', \
                  category='danger')
    return render_template('login.html', form=form)