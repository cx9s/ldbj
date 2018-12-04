from flask import render_template, jsonify
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

@main.route('/editplayer')
def editplayer():
    return render_template('admin/editplayer.html')

@main.route('/editfee')
def editfee():
    return render_template('admin/editfee.html')

@main.route('/ping')
def ping():
    return 'ping ok!'


