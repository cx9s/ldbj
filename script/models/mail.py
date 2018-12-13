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