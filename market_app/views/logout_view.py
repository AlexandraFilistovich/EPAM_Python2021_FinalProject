from flask import redirect, url_for
from flask_login import logout_user

from market_app import app


@app.route('/logout')
def logout_load():
    logout_user()
    return redirect(url_for('home_load'))