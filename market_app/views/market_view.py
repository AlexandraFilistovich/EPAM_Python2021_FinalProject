from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user

from market_app import app, db
from market_app.models.item_model import Item
from market_app.service.user_service import budget_check
from market_app.service.item_service import buy_by, sell_by
from market_app.forms.buy_form import PurchaseForm
from market_app.forms.sell_form import SellForm


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
 
@app.route('/m')
def money_load():
    current_user.budget += 1000
    db.session.commit()
    return redirect(url_for('market_load'))
