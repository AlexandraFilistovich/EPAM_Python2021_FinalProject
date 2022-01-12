from flask import render_template, redirect, url_for, flash
from flask_login import login_user

from market_app import app, db
from market_app.models.user_model import User
from market_app.forms.register_form import RegisterForm


@app.route('/register', methods = ['GET', 'POST'])
def register_load():
    """
    Function loads register page, checks register form validations and
    redirects user on successfull registration.

    :return: page render
    """
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, \
                        email=form.email.data, \
                        plain_password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash(f'You are successfully registered! Hello, {new_user.username}!', \
                  category='success')
        return redirect(url_for('market_load'))
    if form.errors != {}:
        for error_message in form.errors.values():
            flash(f'Wrong data inserted: {error_message}', \
                  category='danger')
    return render_template('register.html', form=form)