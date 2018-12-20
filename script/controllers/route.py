from flask import render_template, jsonify, request, redirect, url_for
from . import main
from flask_login import login_required, current_user


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/player')
def player():
    return render_template('player.html')

@main.route('/fee')
def fee():
    return render_template('fee.html')

@main.route('/attend')
def attend():
    return render_template('attend.html')

@main.route('/video')
def video():
    return render_template('video.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/editplayer')
@login_required
def editplayer():
    return render_template('admin/editplayer.html')

@main.route('/editfee')
@login_required
def editfee():
    return render_template('admin/editfee.html')

@main.route('/ping')
def ping():
    return 'ping ok!'