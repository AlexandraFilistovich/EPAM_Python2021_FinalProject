from packages_dir import app, db
from flask import render_template, redirect, url_for, flash
from packages_dir.models import Item, User
from packages_dir.forms import RegisterForm, LoginForm
from flask_login import login_user


@app.route('/')
@app.route('/home')
def home_load():
    """
    Function loads home page.

    :return: page render
    """
    return render_template('home.html')


'''
@app.route('/<username>')
def userpage_load(username):
    return f'{username}'
'''


@app.route('/market')
def market_load():
    """
    Function loads market page.

    :return: page render
    """
    items = Item.query.all()
    return render_template('market.html', args=items)
 

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
        return redirect(url_for('market_load'))
    if form.errors != {}:
        for error_message in form.errors.values():
            flash(f'Wrong data inserted: {error_message}', \
                  category='danger')
    return render_template('register.html', form=form)

@app.route('/login', methods = ['Get', 'POST'])
def login_load():
    """
    Function loads login page, checks login form validations and
    redirects user on successfull login.
    """
    form = LoginForm()
    if form.validate_on_submit():
        input_user = User.query.filter_by(username=form.username.data).first()
        if input_user and input_user.check_password_input(
                                     input_password=form.password.data):
            login_user(input_user)
            flash(f'You are successfully logged in! Hello, {input_user.username}!', \
                  category='success')
            return redirect(url_for('market_load'))
        else:
            flash('Username or password is incorrect. Please try again.', \
                  category='danger')
    return render_template('login.html', form=form)