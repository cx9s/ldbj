# -*-coding:utf-8-*-
from flask import jsonify, request, url_for
from . import api
from script.models.mongodb import db_connection, get_all_data_from_collection, get_data_from_collection_by_year, get_data_from_collection_by_country
from script.config import MONGODB_URI


@api.route('/get_dataset_by_year')
def get_dataset_by_year():
    year = request.args.get('y')
    collection_name = 'data_by_year'
    client = db_connection(MONGODB_URI)
    ret_list = get_data_from_collection_by_year(client, collection_name, year)
    for row in ret_list:
        row.__delitem__('_id')
    return jsonify(ret_list=ret_list)


@api.route('/get_dataset_by_country')
def get_dataset_by_country():
    country = request.args.get('c')
    collection_name = 'data_by_country'
    client = db_connection(MONGODB_URI)
    ret_list = get_data_from_collection_by_country(client, collection_name, country)
    for row in ret_list:
        row.__delitem__('_id')
    return jsonify(ret_list=ret_list)