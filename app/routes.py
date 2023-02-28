from flask import render_template
from app import app
from app.forms import RegisterForm

@app.route('/')
def index():
    cdn={
        'welcome_to_wild_app':"Let's get started!",
        'meet_our_team': ['Ron', 'Mike', 'Jim', 'Jane']
    }
    return render_template('index.jinja', cdn=cdn, title='Home')

@app.route('/login')
def login():
    return render_template('login.jinja', title='Login')

@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.jinja', form=form, title='Register')

@app.route('/about')
def about():
    return render_template('about.jinja', title='About')

@app.route('/blog')
def blog():
    return render_template('blog.jinja', title='Blog')