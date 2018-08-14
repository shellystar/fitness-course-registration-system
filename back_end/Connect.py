# -*- coding: UTF-8 -*-
import pyodbc

def connect():
    try:
        conn = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=localhost;DATABASE=dbname;UID=sa;PWD=pwd')
#        conn.set_character_set("utf8")
        print "connection successful"
        return conn
    except pyodbc.Error,e:
        print "Error %d:%s" % (e.args[0], e.args[1])
        return -1