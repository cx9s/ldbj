# -*- coding: utf-8 -*-
# Project Name
PROJECT_NAME = '绿动北京足球俱乐部'

# Determine system whether start with debug mode
DEBUG = True

# Cookie security key
#SECRET_KEY = 'AIzaSyAlpjgnmPOM99xvTK_KzGCvVWLMXC_MaA0'
SECRET_KEY = 'lvdongshiguanjun'

# Use google cloud or not
SQLALCHEMY_DATABASE_URI = 'sqlite:///projdb.sqlite'
PAGESIZE = 50

# $heroku config:get MONGODB_URI
MONGODB_URI = 'mongodb://heroku_m90g1d47:jc639222qm88pkui341ek34ser@ds147190.mlab.com:47190/heroku_m90g1d47'

SECONDS = 900

# the flag whether open email notification
ENABLE_MAIL_NOTICE = False
# the host of mail server
MAIL_SERVER = 'smtp.qq.com'
# default sender
MAIL_DEFAULT_SENDER = 'ldbjfc@qq.com'
MAIL_USERNAME = 'ldbjfc@qq.com'
# the password of default sender
MAIL_PASSWORD = 'iysumtueunjedbjj'
MAIL_FROM_NAME = '绿动北京足球俱乐部'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
