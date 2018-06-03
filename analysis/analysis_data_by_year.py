
json = [
   {
      "year":"2012",
      "num":[
         [
            CHN,
            200
         ],
         [
            USA,
            300
         ]
      ],
      "amount":[
         [
            CHN,
            80880
         ],
         [
            USA,
            90881
         ]
      ]
   }
]



from config import SPLIT_FLAG, INPUT_FILE, OUTPUT_FILE1
from script.config import MONGODB_URI
from script.models.mongodb import db_connection, insert_data

import ast

retList = []


def checkYearInRetList(year):
    global retList
    nIndex = -1
    if retList:
        for i in range(0, len(retList)):
            if retList[i]['year'] == year:
                nIndex = i
    return nIndex


def checkCountryCodeOfYearInRetList(year, country_code):
    global retList
    nIndex = -1
    nIndex = checkYearInRetList(year)
    nIndex1 = -1
    if nIndex >= 0:
        incomeList = retList[nIndex].get('num')
        if incomeList:
            for j in range(0, len(incomeList)):
                if incomeList[j][0].__str__() == country_code.__str__():
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


def updateRetLineWithRecord(year, countrycode, money):
    global retList
    nIndex, nIndex1 = checkCountryCodeOfYearInRetList(year, countrycode)

    if nIndex == -1:
        record = {}
        record['year'] = year

        record['num'] = []
        income_list = []
        income_list.append(countrycode)
        income_list.append(1)
        record['num'].append(income_list)

        record['amount'] = []
        lifeExpectancy_list = []
        lifeExpectancy_list.append(countrycode)
        lifeExpectancy_list.append(money)
        record['amount'].append(lifeExpectancy_list)
        retList.append(record)

    else:

        if nIndex1 == -1:

            income_list = []
            income_list.append(countrycode)
            income_list.append(1)

            lifeExpectancy_list = []
            lifeExpectancy_list.append(countrycode)
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
                funded_at = funded_at.split('-')[0]

            raised_amount_usd = parInt(raised_amount_usd.strip())

            if raised_amount_usd != 0:
                updateRetLineWithRecord(funded_at, company_country_code, raised_amount_usd)

            i += 1
        print(retList)

        client = db_connection(MONGODB_URI)
        for row in retList:
            insert_data(client, 'data_by_year', row)


    print('~~~~~~~main end~~~~~~~')


if __name__ == '__main__':
    main()
