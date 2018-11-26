#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from bottle import *
import pymysql.cursors

# Connect to the database
"""
connection = pymysql.connect(host='tsuts.tskoli.is',
                             user='kt',
                             password='mypassword',
                             db='kt_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

"""
connection = pymysql.connect(host='tsuts.tskoli.is',
                             user='gus',
                             password='db1012',
                             db='gus_vefforritun1h18',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


@route('/')
def index():

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`,`email`,`password` FROM `users` WHERE `email`=%s"
            cursor.execute(sql, ('gus@tskoli.is'))
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close()

    return template('index', user=result)

# run(Debug=True)
run(host='0.0.0.0', port=argv[1])


