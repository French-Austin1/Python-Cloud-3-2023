# pylint: disable=no-member
'''This module contains the standard veiws and route not attributed to the authentication
    proccess for Mysite.
'''

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Post, User, Comment
from . import db

veiws = Blueprint('veiws', __name__)

@veiws.route('/')
@veiws.route('/home')
def home():
    '''The basic home page.'''

    posts = Post.query.all()
    return render_template('home.html', user=current_user, posts=posts)

@veiws.route('/about')
def about():
    '''The basic about page.'''

    return render_template('about.html', user=current_user)


@veiws.route('/create-post', methods=['GET','POST'])
@login_required
def create_post():
    '''Render a page to create a new post as long as a user is logged in.'''

    if request.method == 'POST':
        text = request.form.get('text')

        if not text:
            flash('Post cannot be empty', category='error')
        else:
            post = Post(text=text, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('Post successfully created', category='success')
            return redirect(url_for('veiws.home'))
    return render_template('create-post.html', user=current_user)

@veiws.route('/delete-post/<id>')
@login_required
def delete_post(id):
    '''Takes a post id as a parameter and deletes it from the database.'''

    post=Post.query.filter_by(id=id).first()

    if not post:
        flash('Post does not exist.', category='error')
    elif current_user.id != post.author:
        flash('You do not have permission to delete this post', category='error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted.', category='success')

    return redirect(url_for('veiws.home'))

@veiws.route('/posts/<username>')
@login_required
def user_posts(username):
    '''Takes a username as a parameter and renders a template that contains
    all of the posts made connected to that user.'''

    user=User.query.filter_by(username=username).first()

    if not user:
        flash('No user with that username exists.', category='error')
        return redirect(url_for('veiws.home'))

    posts = user.posts

    return render_template('posts.html', user=current_user, posts=posts, username=username)

@veiws.route('/create-comment/<post_id>', methods=['POST'])
@login_required
def create_comment(post_id):
    '''Takes a post_id as a parameter and creates a new comment on the specified post.'''

    text = request.form.get('text')

    if not text:
        flash('Comment cannot be empty.', category='error')
    else:
        post = Post.query.filter_by(id=post_id)
        if post:
            comment = Comment(text=text, author=current_user.id, post_id=post_id)
            db.session.add(comment)
            db.session.commit()
        else:
            flash('Post does not exist.', category='error')
    return redirect(url_for('veiws.home'))

@veiws.route('/admin')
@login_required
def admin():
    '''Allows the admin to veiw all the current usernames and emails in the database.'''

    users = User.query.all()

    if not users:
        flash('There are no users', category='error')
        return redirect(url_for('veiws.home'))
    elif current_user.username != 'admin':
        flash('You are not allowed to  access this information')
        return redirect(url_for('veiws.home'))
    else:
        return render_template('admin.html', users=users, user=current_user)