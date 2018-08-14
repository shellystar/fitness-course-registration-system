# -*- coding: UTF-8 -*-
import pyodbc
import Connect

def login(user_account, user_password, user_type):
    conn = Connect.connect()
    try:
        result = []
        if user_type == 'member':
            print "user_type is member"
            sql = """SELECT *
                      FROM Member
                      WHERE mem_id = '%s' AND mem_key = '%s'"""%(user_account, user_password)
            check_user = conn.cursor()
            check_user.execute(sql)
            result = check_user.fetchall()

        if user_type == 'gym':
            print "user_type is gym"
            sql = """SELECT *
                      FROM Gym
                      WHERE gym_id =  '%s' AND gym_key = '%s'"""%(user_account, user_password)
            check_user = conn.cursor()
            check_user.execute(sql)
            result = check_user.fetchall()
        print result
        print len(result)
        if len(result) == 0:
            print "Wrong account or password"
            if conn:
                conn.close()
            return -1
        else:
            return conn

    except pyodbc.Error,e:
        print "Error %d:%s" % (e.args[0], e.args[1])
        if conn:
            conn.close()
        return -1

