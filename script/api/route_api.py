# -*-coding:utf-8-*-
from flask import jsonify, request, url_for, json, redirect
from . import api
from script.models.mongodb import Player, Fee
import re


# restful api

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@api.route('/todo/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@api.route('/users', methods=['GET'])
def get_users():

    return ''


# restful api end

@api.route('/get_name_list')
def get_name_list():
    player = Player()
    res_list = player.getItems('name','num')
    return jsonify(res_list)


@api.route('/get_player_by_name')
def get_player_by_name():
    name = request.args.get('n')
    player = Player()
    res_list = player.get({'name':re.compile(name)}, 'num')
    for row in res_list:
        row.__delitem__('_id')
    return jsonify(res_list)




@api.route('/get_feeList_by_name')
def get_feeList_by_name():
    name = request.args.get('n')
    fee = Fee()
    res_list = fee.get({"name":name}, [('date', -1)])
    for row in res_list:
        row.__delitem__('_id')
    return jsonify(res_list)


@api.route('/edit_player', methods=['POST'])
def edit_player():
    query_json = {key: dict(request.form)[key][0] for key in dict(request.form)}
    name = query_json['name']
    query_json['num'] = int(query_json['num'])
    query_json['phone'] = int(query_json['phone'])

    player = Player()
    player.update({'name': name}, {'$set': query_json})

    return redirect("/editplayer")


@api.route('/edit_fee', methods=['POST'])
def edit_fee():
    query_json = {key: dict(request.form)[key][0] for key in dict(request.form)}
    date = query_json['date']
    loc = query_json['loc']
    totalAmount = int(query_json['totalAmount'])
    playerList=request.form.getlist('playerList')

    i = len(playerList)
    amount = round(totalAmount/i,1)
    insert_json = []

    for index, item in enumerate(playerList):
        fee = {"name":item, "date":date, "loc":loc, "amount":amount}
        insert_json.append(fee)

    fee = Fee()
    fee.insert(insert_json)
    return redirect("/editfee")