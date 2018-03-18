from flask import render_template, request
from app import app 

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    user = {'username' : 'bart'}
    data = request.form
    print('form data', data)
    return render_template('index.html', title="Welcome to hell", user=user)

@app.route('/register')
def register():
    user = {'username' : 'nick'}
    return render_template('register.html', title="Sign up here", user=user)
