from flask import Blueprint
from script.models.database import db_session

auth = Blueprint('auth', __name__)

from . import route_auth


@auth.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    response.headers.add('Access-Control-Allow-Domain', '*')

    return response


"""
@api.after_request
def close_session_after_request(response):
    db_session.remove()
    return response
"""