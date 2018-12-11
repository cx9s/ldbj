#!/bin/env python
from script import create_app

app = create_app()


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)

'''
web: gunicorn -b 0.0.0.0:$PORT app:app
'''
