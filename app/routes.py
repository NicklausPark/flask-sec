from flask import render_template, request, flash, redirect, url_for
from app import app 
from app.forms import LoginForm

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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data)) 
        return redirect(url_for('index'))
    return render_template('login.html', title="Sign In", form=form)






