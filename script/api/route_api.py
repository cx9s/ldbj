# -*-coding:utf-8-*-
from flask import jsonify, request, url_for, json
from . import api
from script.models.mongodb import db_connection, get_all_data_from_collection, get_user_from_collection_by_name, \
    get_data_from_collection_by_country, get_feeList_from_collection_by_name, get_name_list_from_collection
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


@api.route('/get_feeList_by_name')
def get_feeList_by_name():
    name = request.args.get('n')
    collection_name = 'fee'
    client = db_connection(MONGODB_URI)
    res_list = get_feeList_from_collection_by_name(client, collection_name, name)
    for row in res_list:
        row.__delitem__('_id')
    return jsonify(res_list)


@api.route('/get_dataset_by_country')
def get_dataset_by_country():
    country = request.args.get('c')
    collection_name = 'data_by_country'
    client = db_connection(MONGODB_URI)
    ret_list = get_data_from_collection_by_country(client, collection_name, country)
    for row in ret_list:
        row.__delitem__('_id')
    return jsonify(ret_list=ret_list)