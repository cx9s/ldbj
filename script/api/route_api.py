# -*-coding:utf-8-*-
from flask import jsonify, request, url_for, json, redirect, abort
from . import api
from script.models.mongodb import Player, Fee
import re


# restful api
#players
@api.route('/players', methods = ['GET'])
def get_players():
    if request.method == 'GET':
        player = Player()
        res_list = player.getAndSort({},'num')
        for row in res_list:
            row.__delitem__('_id')
        return jsonify({'players':res_list}), 200


@api.route('/players', methods=['POST'])
def add_player():
    if not request.json or not 'name' in request.json:
        abort(400)
    player = Player()
    insExp = {
            "name": request.json['name'],
            "num": int(request.json['num']),
            "dob": request.json['dob'],
            "position": request.json['position'],
            "phone": int(request.json['phone']),
            "addr": request.json['addr']
#            "addr": request.json.get('addr', "")
        }
    data = player.insertOne(insExp)
    return jsonify(data), 201


@api.route('/players/<string:pName>', methods=['GET'])
def get_player(pName):
    player = Player()
    res_list = player.get({'name':pName})
    if len(res_list) == 0:
        abort(404)
    for row in res_list:
        row.__delitem__('_id')
    return jsonify({'player':res_list[0]}), 200


@api.route('/players/<string:pName>', methods=['PUT'])
def update_player(pName):
    player = Player()
    res_list = player.get({'name':pName})
    if len(res_list) == 0:
        abort(404)
    for row in res_list:
        row.__delitem__('_id')
    p = res_list[0]

    if not request.json:
        abort(400)
    if 'name' not in request.json or type(request.json['name']) != str:
        abort(400)
    if 'num' not in request.json or type(request.json['num']) != int:
        abort(400)
    if 'dob' not in request.json or type(request.json['dob']) != str:
        abort(400)
    if 'position' not in request.json or type(request.json['position']) != list:
        abort(400)
    if 'phone' not in request.json or type(request.json['phone']) != int:
        abort(400)
    if 'addr' not in request.json or type(request.json['addr']) != str:
        abort(400)

    p['name'] = request.json['name']
    p['num'] = request.json['num']
    p['dob'] = request.json['dob']
    p['position'] = request.json['position']
    p['phone'] = request.json['phone']
    p['addr'] = request.json['addr']
    player.update({'name': p['name']}, p)
    return jsonify({'player':p}), 200


@api.route('/players/<string:pName>', methods=['DELETE'])
def del_player(pName):
    player = Player()
    res_list = player.get({'name':pName})
    if len(res_list) == 0:
        abort(404)
    player.delete({'name':pName})
    return jsonify(success=True), 204


#fees
@api.route('/fees/<string:name>', methods = ['GET'])
def get_fees_by_name(name):
    fee = Fee()
    res_list = fee.getAndSort({"name":name}, [('date', -1)])
    for row in res_list:
        row.__delitem__('_id')
        row['amount'] = int(row['amount'])
    return jsonify({'fees':res_list}), 200


@api.route('/fees/<string:name>/<string:date>', methods = ['GET'])
def get_fees_by_name_and_date(name,date):
    fee = Fee()
    res_list = fee.getAndSort({"name":name,"date":date}, '_id')
    for row in res_list:
        row.__delitem__('_id')
        row['amount'] = int(row['amount'])
    return jsonify({'fees':res_list}), 200


@api.route('/fees', methods=['POST'])
def add_fee():
    if not request.json:
        abort(400)
    if 'name' not in request.json or type(request.json['name']) != str:
        abort(400)
    if 'date' not in request.json or type(request.json['date']) != str:
        abort(400)
    if 'loc' not in request.json or type(request.json['loc']) != str:
        abort(400)
    if 'amount' not in request.json or type(request.json['amount']) != int:
        abort(400)
    fee = Fee()
    insExp = [{
            "name": request.json['name'],
            "date": request.json['date'],
            "loc": request.json['loc'],
            "amount": int(request.json['amount'])
        }]
    data = fee.insert(insExp)
    return jsonify(data[0]), 201


@api.route('/fees/<string:name>/<string:date>', methods=['PUT'])
def update_fee(name, date):
    loc = request.args.get('loc')
    amount = request.args.get('amount')
    queryExp = {"name":name,"date":date,"loc":loc,"amount":int(amount)}
    fee = Fee()
    res_list = fee.getAndSort(queryExp, '_id')
    if len(res_list) == 0:
        abort(404)
    for row in res_list:
        row.__delitem__('_id')
    f = res_list[0]

    if not request.json:
        abort(400)
    if 'name' not in request.json or type(request.json['name']) != str:
        abort(400)
    if 'date' not in request.json or type(request.json['date']) != str:
        abort(400)
    if 'loc' not in request.json or type(request.json['loc']) != str:
        abort(400)
    if 'amount' not in request.json or type(request.json['amount']) != int:
        abort(400)

    f['name'] = request.json['name']
    f['date'] = request.json['date']
    f['loc'] = request.json['loc']
    f['amount'] = request.json['amount']
    fee.update(queryExp, f)
    return jsonify({'fee':f}), 200


@api.route('/fees/<string:name>/<string:date>', methods=['DELETE'])
def del_fee(name, date):
    loc = request.args.get('loc')
    amount = request.args.get('amount')
    queryExp = {"name": name, "date": date, "loc": loc, "amount": int(amount)}
    fee = Fee()
    res_list = fee.getAndSort(queryExp, '_id')
    if len(res_list) == 0:
        abort(404)
    fee.delete(queryExp)
    return jsonify(success=True), 204

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
    res_list = player.getAndSort({'name':re.compile(name)}, 'num')
    for row in res_list:
        row.__delitem__('_id')
    return jsonify(res_list)




@api.route('/get_feeList_by_name')
def get_feeList_by_name():
    name = request.args.get('n')
    fee = Fee()
    res_list = fee.getAndSort({"name":name}, [('date', -1)])
    for row in res_list:
        row.__delitem__('_id')
    return jsonify(res_list)


@api.route('/edit_player', methods=['POST'])
def edit_player():
    query_json = {key: dict(request.form)[key][0] for key in dict(request.form)}
    name = query_json['name']
    query_json['num'] = int(query_json['num'])
    query_json['phone'] = int(query_json['phone'])

    posList = request.form.getlist('position')
    position = []
    for index, item in enumerate(posList):
        position.append(item)
    query_json['position'] = position

    player = Player()
    player.update({'name': name}, query_json)
    return redirect("/editplayer")


@api.route('/edit_fee', methods=['POST'])
def edit_fee():
    query_json = {key: dict(request.form)[key][0] for key in dict(request.form)}
    date = query_json['date']
    loc = query_json['loc']
    totalAmount = float(query_json['totalAmount'])
    playerList=request.form.getlist('playerList')

    i = len(playerList)
    amount = round(totalAmount/i)
    insExp = []

    for index, item in enumerate(playerList):
        fee = {"name":item, "date":date, "loc":loc, "amount":amount}
        insExp.append(fee)

    fee = Fee()
    data = fee.insert(insExp)
    return redirect("/editfee")