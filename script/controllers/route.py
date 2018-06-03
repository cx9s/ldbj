from flask import render_template, jsonify
from script.models.mongodb import get_all_data_from_collection
from script.config import MONGODB_URI
from . import main


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/activity')
def year():
    return render_template('activity.html')

@main.route('/ping')
def ping():
    return 'ping ok!'


