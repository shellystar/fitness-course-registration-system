# -*- coding: utf-8 -*-
import pyodbc

def insert_coach_info(conn,c_id,g_id,c_name,c_gender,c_age,c_phone,c_intro):
    cur = conn.cursor()
    insert_sql = """INSERT INTO Coach
                    VALUES('%s','%s','%s','%s','%s','%s','%s')""" % (c_id,g_id,c_name,c_gender,c_age,c_phone,c_intro)
    try:
        cur.execute(insert_sql)
        conn.commit()
        print "insert successful"
        return 0
    except pyodbc.Error, e:
        conn.rollback()
        for index in range(len(e.args)):
            print "Error %s" % (e.args[index])
        return -1

def delete_coach (conn,c_id,g_id):
    cur = conn.cursor()
    sql = """DELETE FROM Coach
              WHERE coach_id = '%s'AND gym_id = '%s'""" % (c_id,g_id)
    print sql
    try:
        cur.execute(sql)
        conn.commit()
        print "delete successful"
        return 0
    except pyodbc.Error, e:
        conn.rollback()
        for index in range(len(e.args)):
            print "Error %s" % (e.args[index])
        return -1

def update_coach_info(conn,c_id,g_id,c_name,c_gender,c_age,c_phone,c_intro):
    cur = conn.cursor()
    update_sql = """UPDATE Coach
                     SET coach_name='%s',coach_gender='%s',coach_age='%s',coach_phone='%s',coach_introduce = '%s'
                     WHERE coach_id = '%s' and gym_id = '%s'""" % (c_name,c_gender,c_age,c_phone,c_intro,c_id,g_id)
    try:
        cur.execute(update_sql)
        conn.commit()
        print "update successful"
        return 0
    except pyodbc.Error, e:
        conn.rollback()
        for index in range(len(e.args)):
            print "Error %s" % (e.args[index])
        return -1

def insert_project_info(conn,p_id,g_id,p_name,p_date,p_time,rema,intro,capa):
    cur = conn.cursor()
    sql = """INSERT INTO Project
              VALUES('%s','%s','%s','%s','%s','%s','%s','%s')""" %(p_id,g_id,p_name,p_date,p_time,rema,intro,capa)
    try:
        cur.execute(sql)
        conn.commit()
        print "insert successful"
        return 0
    except pyodbc.Error, e:
        conn.rollback()
        for index in range(len(e.args)):
            print "Error %s" % (e.args[index])
        return -1

def delete_project(conn,p_gym,p_id):
    cur = conn.cursor()
    sql = """DELETE FROM Project
              WHERE gym_id = '%s' and project_id='%s'""" % (p_gym, p_id)
    print sql
    try:
        cur.execute(sql)
        conn.commit()
        print "delete successful"
        return 0
    except pyodbc.Error, e:
        conn.rollback()
        for index in range(len(e.args)):
            print "Error %s" % (e.args[index])
        return -1

def update_project_info(conn,p_id,g_id,p_name,p_date,p_time,rema,intro,capa):
    cur = conn.cursor()
    update_sql = """UPDATE Project
                     SET gym_id='%s',project_name='%s',
                     project_date = '%s',project_time = '%s',
                     remaining='%s',capacity='%s',
                     project_introduce = '%s'
                     WHERE project_id = '%s'""" % (g_id,p_name,p_date,p_time,rema,capa,intro,p_id)
    print update_sql
    try:
        cur.execute(update_sql)
        conn.commit()
        print "update successful"
        return 0
    except pyodbc.Error, e:
        conn.rollback()
        for index in range(len(e.args)):
            print "Error %s" % (e.args[index])
        return -1

def update_gym_info(conn,g_id,g_key,g_name,g_address,g_open,g_phone,g_intro):
    cur = conn.cursor()
    update_sql = """UPDATE Gym
                     SET gym_key='%s',gym_name='%s',gym_address='%s',openning_time='%s',gym_phone='%s',gym_introduce = '%s'
                     WHERE gym_id = '%s'""" % (g_key,g_name,g_address,g_open,g_phone,g_intro,g_id)
    try:
        cur.execute(update_sql)
        conn.commit()
        print "update successful"
        return 0
    except pyodbc.Error, e:
        conn.rollback()
        for index in range(len(e.args)):
            print "Error %s" % (e.args[index])
        return -1

def delete_appointment(conn, p_id, m_id):
    cur = conn.cursor()
    sql = """DELETE FROM Appointment
             WHERE project_id = '%s'AND mem_id = '%s'""" % (p_id, m_id)
    update_remaining_sql = """UPDATE Project
                              SET remaining = remaining + 1
                              WHERE project_id = '%s'""" % p_id
    try:
        cur.execute(sql)
        cur.execute(update_remaining_sql)
        conn.commit()
        return 0
    except pyodbc.Error, e:
        conn.rollback()
        for index in range(len(e.args)):
            print "Error %s" % (e.args[index])
        return -1

def insert_appointment_info(conn,p_id,m_id,user_account):
    cur = conn.cursor()
    check_remaining_sql = """SELECT *
                              FROM Project
                              WHERE project_id = '%s' AND remaining > 0 AND gym_id = '%s'"""% (p_id,user_account)
    print check_remaining_sql
    insert_sql = """INSERT INTO Appointment
                    VALUES('%s','%s')""" % (p_id,m_id)
    update_remaining_sql = """UPDATE Project
                         SET remaining = remaining - 1
                         WHERE project_id = '%s'""" % p_id
    print update_remaining_sql
    try:
        cur.execute(check_remaining_sql)
        check_remaining_result = cur.fetchall()
        print len(check_remaining_result)
        if not len(check_remaining_result):
            print "No remaining project id %s" % p_id
            return -1
        cur.execute(insert_sql)
        cur.execute(update_remaining_sql)
        conn.commit()
        return 0
    except pyodbc.Error, e:
        conn.rollback()
        for index in range(len(e.args)):
            print "Error %s" % (e.args[index])
        return -1