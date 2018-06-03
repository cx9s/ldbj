from .config import INPUT_FILE, OUTPUT_FILE, SPLIT_FLAG
from script.models.mongodb import insert_data
from script.config import MONGODB_URI

import json
import ast

record_json = {}
location_dict = {}


def initial_location_dict_from_file():
    global location_dict
    with open(LOCATION_OLD_FILE, 'r') as infile:
        for line in infile:
            line = line.replace('\n','')
            json_data = ast.literal_eval(line)
            json_data = json.loads(json.dumps(json_data))
            location_dict.update(json_data)
            print(len(location_dict))


def get_location_from_list(city_name):
    global location_dict
    if city_name in location_dict.keys():
        return location_dict[city_name]
    else:
        return {}


def insert_location_into_dict(city_name, lat, lng):
    global location_dict
    if city_name not in location_dict.keys():
        location_dict[city_name] = {'lat': lat, 'lng': lng}
        print('length of location dict:', len(location_dict))


def init_record_json():
    global record_json
    record_json = {
        "geometry": {"coordinates": [], "type": "Point"},
        "id": "",
        "type": "Feature",
        "properties": {"company_name": "8.00",
                       "company_category_list": "",
                       "company_country_code": "",
                       "company_city": "",
                       "funding_round_type": "",
                       "funded_at": "",
                       "raised_amount_usd": ""

                       }
    }


def generate_location_list():
    print('~~~~~~~generate_location_list start~~~~~~~')
    with open(INPUT_FILE, 'r') as infile, open(LOCATION_OUTPUT_FILE, 'w') as outfile:
        i = 1
        for line in infile:
            print('generate_location_list:', i)
            line = line.replace('\r', '').replace('\n', '')
            column_list = line.split(SPLIT_FLAG)
            company_country_code, company_city = column_list[3], column_list[6]

            location_name = company_city or company_country_code
            location_name = location_name.replace('\"', '').strip()
            location_name = location_name.replace('\'', '').strip()

            if location_name:
                lat_lng_json = get_location_from_list(location_name)
                if not lat_lng_json:
                    lat_lng_json = get_location_by_city(location_name)
                    insert_location_into_dict(location_name,
                                              lat_lng_json['lat'] if lat_lng_json else -1,
                                              lat_lng_json['lng'] if lat_lng_json else -1)
                    location_lat_lng = {}
                    location_lat_lng[location_name] = lat_lng_json
                    outfile.write(location_lat_lng.__str__() + '\n')

            i += 1
    print('~~~~~~~generate_location_list end~~~~~~~')


def main():
    print('~~~~~~~main start~~~~~~~')
    with open(INPUT_FILE, 'r') as infile, open(OUTPUT_FILE, 'w') as outfile:
        i = 1
        for line in infile:
            line_str = line
            print('main:', i)

            line_str = line_str.replace('\r', '').replace('\n', '')
            column_list = line_str.split(SPLIT_FLAG)


            company_name, company_category_list, company_country_code, company_city, id, funding_round_type, funded_at, raised_amount_usd = \
                column_list[1], column_list[2], column_list[3], column_list[6], column_list[7], column_list[8], \
                column_list[10], column_list[11]

            if company_name:
                company_name = company_name.replace('\"', '').replace('\'', '').strip()
            if company_category_list:
                company_category_list = company_name.replace('\"', '').replace('\'', '').strip()
            if company_country_code:
                company_country_code = company_country_code.replace('\"', '').replace('\'', '').strip()
            if company_city:
                company_city = company_city.replace('\"', '').replace('\'', '').strip()
            if id and id.find('/') != -1:
                id = id.split('/')[-1]

            if funded_at:
                funded_at = '-'.join(funded_at.split('T')[0])

            location_name = company_city or company_country_code

            if location_name:
                lat_lng_json = get_location_from_list(location_name)
            else:
                lat_lng_json = {}

            lat = lat_lng_json['lat'] if lat_lng_json else -1
            lng = lat_lng_json['lng'] if lat_lng_json else -1
            print(location_name, lat, lng)
            if lat != -1 and lng != -1:
                init_record_json()
                record_json = {
                    "geometry": {"coordinates": [lng, lat], "type": "Point"},
                    "id": id,
                    "type": "Feature",
                    "properties": {"company_name": company_name,
                                   "company_category_list": company_category_list,
                                   "company_country_code": company_country_code,
                                   "company_city": company_city,
                                   "funding_round_type": funding_round_type,
                                   "funded_at": funded_at,
                                   "raised_amount_usd": raised_amount_usd
                                   }
                }

                outfile.write(record_json.__str__() + ',\n')

            i += 1
    print('~~~~~~~main end~~~~~~~')


if __name__ == '__main__':
    initial_location_dict_from_file()
    generate_location_list()
    main()
