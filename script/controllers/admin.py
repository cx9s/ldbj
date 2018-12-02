from flask import render_template, jsonify, request
from script.models.mongodb import get_all_data_from_collection
from script.config import MONGODB_URI
from . import admin


@admin.route('/edit/user')
def edit_user():
    loc_str = request.args.get('location')
    price_flag = request.args.get('price-selection')
    date_flag = request.args.get('daterange-selection')

    bexist, ptype, poutput = hpp_search(loc_str, price_flag, date_flag)
    qry_str = {
        'loc': loc_str,
        'price': price_flag,
        'date': date_flag
    }

    if bexist and poutput['district_list'] and poutput['district_hpp_analysis']:
        return render_template('/hpp/details.html', qry_str=qry_str, bexist=bexist, ptype=ptype, poutput=poutput)
    else:
        return render_template('hpp/search.html')


