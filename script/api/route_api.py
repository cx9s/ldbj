# -*-coding:utf-8-*-
from flask import jsonify, request, url_for, json, redirect, render_template
from . import api
from script.models.mongodb import db_connection, get_all_data_from_collection, get_user_from_collection_by_name, \
    get_data_from_collection_by_country, get_feeList_from_collection_by_name, get_name_list_from_collection, \
    get_user_detail_by_name, edit_user_detail_by_name, edit_fee_list
from script.config import MONGODB_URI


@api.route('/get_name_list')
def get_name_list():
    collection_name = 'users'
    client = db_connection(MONGODB_URI)
    res_list = get_name_list_from_collection(client, collection_name)
    return jsonify(res_list)


@api.route('/get_user_by_name')
def get_user_by_name():
    name = request.args.get('n')
    collection_name = 'users'
    client = db_connection(MONGODB_URI)
    res_list = get_user_from_collection_by_name(client, collection_name, name)
    for row in res_list:
        row.__delitem__('_id')
    return jsonify(res_list)


@api.route('/get_user_detail')
def get_user_detail():
    name = request.args.get('n')
    collection_name = 'users'
    client = db_connection(MONGODB_URI)
    res_list = get_user_detail_by_name(client, collection_name, name)
    for row in res_list:
        row.__delitem__('_id')
    return jsonify(res_list)


@api.route('/get_feeList_by_name')
def get_feeList_by_name():
    name = request.args.get('n')
    collection_name = 'fee'
    client = db_connection(MONGODB_URI)
    res_list = get_feeList_from_collection_by_name(client, collection_name, name)
    for row in res_list:
        row.__delitem__('_id')
    return jsonify(res_list)


@api.route('/edit_user', methods=['POST'])
def edit_user():
    query_json = {key: dict(request.form)[key][0] for key in dict(request.form)}
    name = query_json['user']

    query_json['num'] = int(query_json['num'])
    query_json['phone'] = int(query_json['phone'])

    collection_name = 'users'
    client = db_connection(MONGODB_URI)
    edit_user_detail_by_name(client, collection_name, name, query_json)
    return render_template('admin/editplayer.html')


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
    print(insert_json)

    collection_name = 'fee'
    client = db_connection(MONGODB_URI)
    edit_fee_list(client, collection_name, insert_json)
    return render_template('admin/editfee.html')