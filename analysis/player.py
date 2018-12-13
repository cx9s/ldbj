json = [
   {
       "name":"陈譞",
       "num":9,
       "dob":"1983-09-18",
       "position":[
           "LWF",
           "AMF"
       ],
       "phone":13810103773,
       "email":"12730529@qq.com",
       "addr":"远洋风景小区"
   },
    {
       "name":"石伟",
       "num":15,
       "dob":"1985-03-15",
       "position":[
           "LB"
       ],
       "phone":13810103773,
       "email":"12730529@qq.com",
       "addr":"远洋风景小区"
   }
]


from analysis.config import SPLIT_FLAG, INPUT_FILE
from script.models.mongodb import Player


def wrapPlayer(name):
    record = {}
    record['name'] = name
    record['num'] = 0
    record['dob'] = ""
    record['position'] = []
    record['phone'] = 0
    record['email'] = ""
    record['addr'] = ""
    resList.append(record)


def main():
    global resList
    resList = []
    print('~~~~~~~main start~~~~~~~')
    with open(INPUT_FILE, 'r') as infile:
        i = 1
        for line in infile:
            if i == 1:

                line_str = line.replace('\r', '').replace('\n', '')
                line_list = line_str.split(SPLIT_FLAG)

                del line_list[0]
                del line_list[0]

                print(line_list)

                for k in line_list:
                    wrapPlayer(k)
            i += 1

        print(resList)


# insert mongoDB

    player = Player()
    for row in resList:
       player.insert(row)


    print('~~~~~~~main end~~~~~~~')


if __name__ == '__main__':
    main()
