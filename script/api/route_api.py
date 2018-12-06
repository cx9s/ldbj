# -*-coding:utf-8-*-
from flask import jsonify, request, url_for, json, redirect
from . import api
from script.models.mongodb import User, Fee
import re


@api.route('/get_name_list')
def get_name_list():
    user = User()
    res_list = user.getItems('user','num')
    return jsonify(res_list)


@api.route('/get_user_by_name')
def get_user_by_name():
    name = request.args.get('n')
    user = User()
    res_list = user.get({'user':re.compile(name)}, 'num')
    for row in res_list:
        row.__delitem__('_id')
    return jsonify(res_list)




@api.route('/get_feeList_by_name')
def get_feeList_by_name():
    name = request.args.get('n')
    fee = Fee()
    res_list = fee.get({"user":name}, [('date', -1)])
    for row in res_list:
        row.__delitem__('_id')
    return jsonify(res_list)


@api.route('/edit_user', methods=['POST'])
def edit_user():
    query_json = {key: dict(request.form)[key][0] for key in dict(request.form)}
    name = query_json['user']
    query_json['num'] = int(query_json['num'])
    query_json['phone'] = int(query_json['phone'])

    user = User()
    user.update({'user': name}, {'$set': query_json})

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
        fee = {"user":item, "date":date, "loc":loc, "amount":amount}
        insert_json.append(fee)

    fee = Fee()
    fee.insert(insert_json)
    return redirect("/editfee")