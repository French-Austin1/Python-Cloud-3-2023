# pylint: disable=no-member
'''This module contains the implementation of all of the authentication functions for Mysite.'''
import re
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    '''login routing function'''
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                if user.username != 'admin':
                    flash('logged in!', category='success')
                    login_user(user, remember=True)
                    return redirect(url_for('veiws.home'))
                
                flash('logged in as admin!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('veiws.admin'))
            else:
                flash('password is incorrect!', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template('login.html', user=current_user)

@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    '''sign_up routing function'''
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm = request.form.get("confirm-password")

        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()
        if email_exists:
            flash('Email is already in use.', category='error')
        elif username_exists:
            flash('Username is already in use.', category='error')
        elif password != confirm:
            flash('Passwords do not match.', category='error')
        elif len(username) < 2:
            flash('Username is too short.', category='error')
        elif len(password) < 6:
            flash('Password is too short.', category='error')
        elif re.fullmatch(REGEX, email):
            new_user = User(email=email, username=username,
                            password=generate_password_hash(password, method= 'sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User created!')
            return redirect(url_for('veiws.home'))
        else:
            flash('Email is not valid.', category='error')

    return render_template('signup.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('veiws.home'))
