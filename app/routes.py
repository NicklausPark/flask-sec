from flask import render_template, request, flash, redirect, url_for
from app import app 
from flask_login import current_user, login_user, logout_user
from app.forms import LoginForm
from app.models import User


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    user = {'username' : 'bart'}
    data = request.form
    print('form data', data)
    return render_template('index.html', title="This is a Test Page", user=user)

@app.route('/register')
def register():
    user = {'username' : 'nick'}
    return render_template('register.html', title="Sign up here", user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: 
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password') 
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)  
        return redirect(url_for('index'))
    return render_template('login.html', title="Sign In", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))









