# -*- coding: utf-8 -*-
from flask import Flask
from flask_mail import Mail
from script.config import SECRET_KEY, DEBUG
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from script.models.mongodb import User
from script.models.form import LoginForm

mail = Mail()


def create_app():
    app = Flask(__name__)
    app.debug = DEBUG

    # load config file
    app.config.from_pyfile('config.py')

    # config secret key
    app.config['SECRET_KEY'] = SECRET_KEY

    #config json output encode
    app.config['JSON_AS_ASCII'] = False

    # init app by mail
    mail.init_app(app)

    # config jinja
    # app.jinja_env.variable_start_string = '(('
    # app.jinja_env.variable_end_string = '))'
    app.jinja_env.trim_blocks = True

    # use login_manager to manage session
    login_manager = LoginManager()
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app=app)

    # 这个callback函数用于reload User object，根据session中存储的user id
    @login_manager.user_loader
    def load_user(user_id):
        return User('').get(user_id)

    # csrf protection
    csrf = CSRFProtect()
    csrf.init_app(app)

    # start register module
    from script.controllers import main as main_blueprint
    from script.api import api as api_blueprint
    from script.auth import auth as auth_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    # end register module
    return app
