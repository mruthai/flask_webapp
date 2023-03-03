from . import bp as main_bp
from flask import render_template

@main_bp.route('/')
def index():
    cdn={
        'soccer_fantasy':("Kick-off!"),
        'top_player': ['John Drinkwater', 'Pierce Hammerstone', 'Paul Debronson', 'Jane McGuoo']
    }
    return render_template('index.jinja', cdn=cdn, title='Home')



@main_bp.route('/about')
def about():
    return render_template('about.jinja', title='About')

