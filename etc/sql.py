#! /usr/bin/python3

import pymysql

con = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='customer', charset='utf8', cursorclass=pymysql.cursors.DictCursor)


with con.cursor() as cur:

  cur.execute('SELECT * FROM cust')
  rows = cur.fetchall()
  print(rows)
