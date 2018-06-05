from flask import render_template, jsonify
from script.models.mongodb import get_all_data_from_collection
from script.config import MONGODB_URI
from . import main


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/player')
def player():
    return render_template('player.html')

@main.route('/fee')
def fee():
    return render_template('fee.html')

@main.route('/ping')
def ping():
    return 'ping ok!'


