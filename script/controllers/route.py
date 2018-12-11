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

@main.route('/editplayer')
@login_required
def editplayer():
    return render_template('admin/editplayer.html', username=current_user.username)

@main.route('/editfee')
@login_required
def editfee():
    return render_template('admin/editfee.html')

@main.route('/ping')
def ping():
    return 'ping ok!'