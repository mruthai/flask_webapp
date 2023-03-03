from . import bp as social_bp
from app.blueprints.social.models import User, Player, Post
from app.forms import BlogForm, PlayerForm
from flask import render_template, redirect, flash
from flask_login import login_required, current_user

@social_bp.route('/user/<username>')
def user(username):
    user_match = User.query.filter_by(username=username).first()
    if not user_match:
        redirect('/')
    player_post = user_match.player_post
    user_post = user_match.user_posts
    return render_template('user.jinja', user=user_match, player_post=player_post, user_post=user_post)


@social_bp.route('/blog', methods=['GET', 'POST'])
@login_required
def blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        b = Post(title=title, body=body, user_id=current_user.id)
        b.commit()
        flash (f'Post successful: {title} {body}')
        return redirect('/')
    return render_template('blog.jinja', blog=form, title='Blog')

@social_bp.route('/player', methods=['GET', 'POST'])
@login_required
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
        p = Player(first_name=first_name, last_name=last_name, team_name=team_name, position=position, age=age, nationality=nationality, date_created=date_created, price=price, user_id=current_user.id)
        p.commit()
        flash (f'Player added {first_name} {last_name} {team_name} {position}!', 'successfully')
        return redirect('/')
    return render_template('player.jinja', player=form, title='Player')

