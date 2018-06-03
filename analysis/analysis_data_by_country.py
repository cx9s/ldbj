
json = [
   {
      "country":"China",
      "num":[
         [
            2008-03-19,
            2
         ]
      ],
      "amount":[
         [
            2008-03-19,
            80880
         ]
       ]
   }
]



from config import SPLIT_FLAG, INPUT_FILE, OUTPUT_FILE1
from script.config import MONGODB_URI
from script.models.mongodb import db_connection, insert_data

import ast

retList = []


def checkCountryInRetList(country_code):
    global retList
    nIndex = -1
    if retList:
        for i in range(0, len(retList)):
            if retList[i]['country'] == country_code:
                nIndex = i
    return nIndex


def checkDatetimeOfCountryInRetList(country_code, date_time):
    global retList
    nIndex = -1
    nIndex = checkCountryInRetList(country_code)
    nIndex1 = -1
    if nIndex >= 0:
        incomeList = retList[nIndex].get('num')
        if incomeList:
            for j in range(0, len(incomeList)):
                if incomeList[j][0].__str__() == date_time.__str__():
                    nIndex1 = j
    print(nIndex, nIndex1)
    return nIndex, nIndex1


def parInt(num):
    if isinstance(num, int):
        return num
    elif isinstance(num, str):
        ret_num = 0
        try:
            ret_num = int(num)
        except ValueError:
            ret_num = 0
        return ret_num


def updateRetLineWithRecord(country_code, date_time, money):
    global retList
    nIndex, nIndex1 = checkDatetimeOfCountryInRetList(country_code, date_time)

    if nIndex == -1:
        record = {}
        record['country'] = country_code

        record['num'] = []
        income_list = []
        income_list.append(date_time)
        income_list.append(1)
        record['num'].append(income_list)

        record['amount'] = []
        lifeExpectancy_list = []
        lifeExpectancy_list.append(date_time)
        lifeExpectancy_list.append(money)
        record['amount'].append(lifeExpectancy_list)
        retList.append(record)

    else:

        if nIndex1 == -1:

            income_list = []
            income_list.append(date_time)
            income_list.append(1)

            lifeExpectancy_list = []
            lifeExpectancy_list.append(date_time)
            lifeExpectancy_list.append(money)
            retList[nIndex]['num'].append(income_list)
            retList[nIndex]['amount'].append(lifeExpectancy_list)

        else:
            retList[nIndex]['num'][nIndex1][1] += 1
            retList[nIndex]['amount'][nIndex1][1] += money


def main():
    global retList
    print('~~~~~~~main start~~~~~~~')
    with open(INPUT_FILE, 'r') as infile, open(OUTPUT_FILE1, 'w') as outfile:
        i = 1
        for line in infile:
            line_str = line
            print('main:', i)

            line_str = line_str.replace('\r', '').replace('\n', '')
            column_list = line_str.split(SPLIT_FLAG)

            company_country_code, funded_at, raised_amount_usd = column_list[3], column_list[10], column_list[11]

            if company_country_code:
                company_country_code = company_country_code.replace('\"', '').replace('\'', '').strip()

            if funded_at:
                funded_at = funded_at.split('T')[0]

            raised_amount_usd = parInt(raised_amount_usd.strip())

            if raised_amount_usd != 0:
                updateRetLineWithRecord(company_country_code, funded_at, raised_amount_usd)

            i += 1

        client = db_connection(MONGODB_URI)
        for row in retList:
            insert_data(client, 'data_by_country', row)

    print('~~~~~~~main end~~~~~~~')


if __name__ == '__main__':
    main()
