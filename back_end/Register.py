# -*- coding: UTF-8 -*-
import pyodbc
import Connect

def newMember(u_id, u_key, u_name, gender, phone, age):
    try:
        conn = Connect.connect()
        try:
            register = conn.cursor()
            insert_user_info = """INSERT INTO Member(mem_id,mem_key,mem_name,mem_gender,mem_phone,mem_age)
                             VALUES ('%s','%s','%s','%s','%s','%s')""" % (u_id,u_key,u_name,gender,phone,age)

            register.execute(insert_user_info)
            conn.commit()
            print "register successful"
            return 0

        except pyodbc.Error, e:
            conn.rollback()
            for index in range(len(e.args)):
                print "Error %s" % (e.args[index])
            return -1

    except pyodbc.Error, e:
        for index in range(len(e.args)):
            print "Error %s" % (e.args[index])
        return -1

def newGym(g_id, g_key, g_name, g_addr, g_open, g_phone, g_intro):
    try:
        conn = Connect.connect()
        try:
            register = conn.cursor()
            insert_gym_info = """INSERT INTO Gym
                                  VALUES ('%s','%s','%s','%s','%s','%s','%s')""" % (g_id,g_key,g_name,g_addr,g_open,g_phone,g_intro)
            register.execute(insert_gym_info)
            conn.commit()
            print "register successful"
            return 0

        except pyodbc.Error, e:
            conn.rollback()
            for index in range(len(e.args)):
                print "Error %s" % (e.args[index])
            return -1

    except pyodbc.Error, e:
        for index in range(len(e.args)):
            print "Error %s" % (e.args[index])
        return -1