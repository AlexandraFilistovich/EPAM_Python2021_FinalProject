from flask import render_template

from market_app import app


@app.route('/')
@app.route('/home')
def home_load():
    """
    Function loads home page.

    :return: page render
    """
    return render_template('home.html')