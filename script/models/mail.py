from flask_mail import Mail, Message
from script.config import MAIL_USERNAME

"""
msgExp = [
    {
        "subject":"",
        "addr":"",
        "msgHTML":""
    },
    {
        "subject":"",
        "addr":"",
        "msgHTML":""
    }
]
"""

def sendMail(msgExp):
    mail = Mail()
    with mail.connect() as conn:
        for item in msgExp:
            msg = Message(
                sender = MAIL_USERNAME,
                subject = item['subject'],
                recipients = [item['addr']],
                html = item['msgHTML']
            )
            conn.send(msg)



    """
    使用 $in
    res_list = fee.getNameAndTotalUndue()
    if len(res_list) != 0:
        print(res_list)
        msgExp = []
        msgFlash = '已向欠费队员：'
        player = Player()
        for item in res_list:
            p = player.get({'name':item['_id']})
            p = p[0]
            if type(p['email']) != None and p['email'] != '':
                msgExp.append({
                    "subject": "队费提醒",
                    "addr": p['email'],
                    "msgHTML": "<p>亲爱的 "+p['name']+"，该交费了哦</p>"
                })
                msgFlash += p['name']
        if len(msgExp) != 0:
            print('send mail')
            flash(msgFlash, 'success')

        msgExp = [
            {
                "subject": "队费提醒",
                "addr": "12730529@qq.com",
                "msgHTML": "<h2>亲爱的 "+playerList[0]+"</h2><p>该交费了哦</p>"
            }
        ]
        sendMail(msgExp)
        """