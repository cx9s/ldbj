from flask import request, redirect, render_template, url_for
from script.models.mongodb import User
from script.models.form import LoginForm
from flask_login import login_user, logout_user, login_required, current_user
from . import auth


#login
"""
@auth.route('/initAdmin')
def init():
    user = User('admin')
    p = user.password('admin')
    print(p)
    return jsonify({user.username:'Success'})
"""

@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_name = request.form.get('username', None)
        password = request.form.get('password', None)
        remember_me = request.form.get('remember_me', False)
        user = User(user_name)
        if user.verify_password(password):
            login_user(user)
            return redirect(request.args.get('next') or url_for('main.index'))
    return render_template('admin/login.html', title="Sign In", form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))