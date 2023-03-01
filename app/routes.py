from flask import render_template, flash, redirect
from app import app
from app.forms import RegisterForm, LoginForm, PlayerForm, BlogForm

@app.route('/')
def index():
    cdn={
        'soccer_fantasy':("Kick-off!"),
        'top_player': ['John Drinkwater', 'Pierce Hammerstone', 'Paul Debronson', 'Jane McGuoo']
    }
    return render_template('index.jinja', cdn=cdn, title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash (f'Request to login {form.password}!', 'successful')
        return redirect('/')
    return render_template('login.jinja', login=form, title='Login')

@app.route('/register',  methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash (f'Request to register {form.username}!', 'successful')
        return redirect('/')
    return render_template('register.jinja', form=form, title='Register')

@app.route('/about')
def about():
    return render_template('about.jinja', title='About')

@app.route('/blog', methods=['GET', 'POST'])
def blog():
    form = BlogForm()
    if form.validate_on_submit():
        flash (f'Request to submit post {form.submit}!', 'successful')
        return redirect('/')
    return render_template('blog.jinja', blog=form, title='Blog')

@app.route('/player', methods=['GET', 'POST'])
def player():
    form = PlayerForm()
    if form.validate_on_submit():
        flash (f'Player added {form.submit}!', 'successfully')
        return redirect('/')
    return render_template('player.jinja', player=form, title='Player')