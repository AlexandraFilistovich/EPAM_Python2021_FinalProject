from market_app import app, db
from flask import render_template, redirect, url_for, flash, request
from market_app.models.user_model import User
from market_app.models.item_model import Item
from market_app.service.user_service import budget_check, check_password_input
from market_app.service.item_service import buy_by, sell_by
from market_app.forms import RegisterForm, LoginForm, PurchaseForm, SellForm
from flask_login import login_user, logout_user, login_required, current_user


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


@app.route('/market', methods = ['GET', 'POST'])
@login_required
def market_load():
    """
    Function loads market page.

    :return: page render
    """
    sell_form = SellForm()
    purchase_form = PurchaseForm()

    if request.method == "POST":
        # Purchase item.
        purchased_item = request.form.get('purchased_item')
        item_instance = Item.query.filter_by(name=purchased_item).first()
        if item_instance:
            if budget_check(current_user, item_instance):
                buy_by(item_instance, current_user)
                flash(f'Successfully purchased!', \
                        category='success')
            else:
                flash(f'You do not have enough money to buy this item!', \
                        category='danger')
        
        # Sell item.
        sold_item = request.form.get('sell_item')
        item_instance = Item.query.filter_by(name=sold_item).first()
        if item_instance:
            sell_by(item_instance, current_user)
            flash(f'Successfully sold!', \
                        category='success')
        return redirect(url_for('market_load'))
    
    if request.method == "GET":
        items = Item.query.filter_by(owner=None)
        items_owned = Item.query.filter_by(owner=current_user.id)
        return render_template('market.html', items=items, \
                                items_owned=items_owned, \
                                purchase_form=purchase_form, \
                                sell_form=sell_form)
 

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


@app.route('/logout')
def logout_load():
    logout_user()
    return redirect(url_for('home_load'))

@app.route('/m')
def money_load():
    current_user.budget += 1000
    db.session.commit()
    return redirect(url_for('market_load'))