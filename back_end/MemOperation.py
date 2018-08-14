# -*- coding: utf-8 -*-
import pyodbc

def insert_appointment_info(conn,p_id,m_id):
    cur = conn.cursor()
    check_remaining_sql = """SELECT *
                              FROM Project
                              WHERE project_id = '%s' AND remaining > 0"""% p_id
    insert_sql = """INSERT INTO Appointment
                    VALUES('%s','%s')""" % (p_id,m_id)
    update_remaining_sql = """UPDATE Project
                         SET remaining = remaining - 1
                         WHERE project_id = '%s'""" % p_id

    try:
        cur.execute(check_remaining_sql)
        check_remaining_result = cur.fetchall()
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

def delete_appointment (conn,p_id,m_id):
    cur = conn.cursor()
    sql = """DELETE FROM Appointment
              WHERE project_id = '%s'AND mem_id = '%s'""" % (p_id,m_id)
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

def update_member_info(conn,m_id,m_key,m_name,m_gender,m_phone,m_age):
    cur = conn.cursor()
    update_sql = """UPDATE Member
                     SET mem_key='%s',mem_name='%s',mem_gender='%s',mem_phone='%s',mem_age='%s'
                     WHERE mem_id = '%s'""" % (m_key,m_name,m_gender,m_phone,m_age,m_id)
    try:
        cur.execute(update_sql)
        conn.commit()
        return 0
    except pyodbc.Error, e:
        conn.rollback()
        for index in range(len(e.args)):
            print "Error %s" % (e.args[index])
        return -1