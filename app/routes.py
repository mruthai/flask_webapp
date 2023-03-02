from flask import render_template, flash, redirect
from app import app, db
from app.forms import RegisterForm, LoginForm, PlayerForm, BlogForm
from app.models import User, Player
from flask_login import current_user, login_user

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
        username = form.username.data
        password = form.password.data
        user_match = User.query.filter_by(username=username).first()
        if not user_match or not user_match.check_password(password):
            flash(f'Username or Password was incorrect', 'try again')
            return redirect('/login')
        flash (f'Request to login {form.password}!', 'successful')
        return redirect('/')
    return render_template('login.jinja', login=form, title='Login')

@app.route('/register',  methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        u = User(username=username, email=email, password_hash='')
        user_match = User.query.filter_by(username=username).first()
        email_match = User.query.filter_by(email=email).first()
        if user_match or email_match:
            flash (f'User {username} already exists!', 'try again')
            return redirect('/register')
        elif email_match:
            flash (f'Request to register {username}!', 'successful')
            return redirect('/register')
        else:
            u.hash_password(password)
            u.commit()
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
        first_name = form.first_name.data
        last_name = form.last_name.data
        team_name = form.team_name.data
        position = form.position.data
        age = form.age.data
        nationality = form.nationality.data
        price = form.price.data
        date_created = form.date_created.data
        p = Player(first_name=first_name, last_name=last_name, team_name=team_name, position=position, age=age, nationality=nationality, date_created=date_created, price=price)
        p.commit()
        flash (f'Player added {first_name} {last_name} {team_name} {position}!', 'successfully')
        return redirect('/')
    return render_template('player.jinja', player=form, title='Player')