from flask import Blueprint

main = Blueprint('main', __name__)
admin = Blueprint('admin', __name__)

from . import route
