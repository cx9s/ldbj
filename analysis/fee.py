json = [
   {
      "user":"陈譞",
      "date":"2012-03-10",
      "loc":"奥利匹克森林公园",
      "amount":100
   },
    {
        "user": "石伟",
        "date": "2012-03-10",
        "loc": "奥利匹克森林公园",
        "amount": -35
    }
]



from analysis.config import SPLIT_FLAG, INPUT_FILE
from script.config import MONGODB_URI
from script.models.mongodb import db_connection, insert_data

from decimal import Decimal


def wrapFee(index, list):
    record = {}
    record['user'] = nameList[index]
    record['date'] = list[0]
    record['loc'] = list[1]
    record['amount'] = float(list[index])
    resList.append(record)



def main():
    global resList, nameList
    resList = []
    nameList = []
    print('~~~~~~~main start~~~~~~~')
    with open(INPUT_FILE, 'r') as infile:
        i = 1
        for line in infile:
            if i == 1:

                line_str = line.replace('\r', '').replace('\n', '')
                nameList = line_str.split(SPLIT_FLAG)
                print(nameList)

            else:

                line_str = line.replace('\r', '').replace('\n', '')
                rowList = line_str.split(SPLIT_FLAG)
                print(rowList)

                for j in range(len(rowList)):
                    if j > 1:
                        if rowList[j] != '':
                            wrapFee(j,rowList)

            i += 1

    print(resList)


# insert mongoDB
    """
    client = db_connection(MONGODB_URI)
    for row in resList:
        insert_data(client, 'fee', row)
    """

    print('~~~~~~~main end~~~~~~~')


if __name__ == '__main__':
    main()
