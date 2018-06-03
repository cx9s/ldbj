json = [
   {
       "user":"陈譞",
       "num":"9",
       "dob":"1983-09-18",
       "position":[
           "lwf",
           "amf"
       ],
       "phone":13810103773,
       "addr":"远洋风景小区"
   },
    {
       "user":"石伟",
       "num":"15",
       "dob":"1985-03-15",
       "position":[
           "lb"
       ],
       "phone":13810103773,
       "addr":"远洋风景小区"
   }
]


from analysis.config import SPLIT_FLAG, INPUT_FILE
from script.config import MONGODB_URI
from script.models.mongodb import db_connection, insert_data


def wrapUsers(name):
    record = {}
    record['user'] = name
    record['num'] = 0
    record['dob'] = ""
    record['position'] = []
    record['phone'] = 0
    record['addr'] = ""
    resList.append(record)


def main():
    global resList
    resList = []
    print('~~~~~~~main start~~~~~~~')
    with open(INPUT_FILE, 'r') as infile:
        i = 1
        for line in infile:
            if i == 2:

                line_str = line
                line_str = line_str.replace('\r', '').replace('\n', '')
                column_list = line_str.split(SPLIT_FLAG)

                del column_list[0]
                del column_list[0]
                column_list.pop()

                print(column_list)

                for k in column_list:
                    wrapUsers(k)
            i += 1

        print(resList)


        client = db_connection(MONGODB_URI)
        for row in resList:
            insert_data(client, 'users', row)


    print('~~~~~~~main end~~~~~~~')


if __name__ == '__main__':
    main()
