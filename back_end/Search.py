# -*- coding: UTF-8 -*-
import pyodbc

def SearchGymID(conn, gid):
    sql = """select gym_id,gym_name,gym_address,openning_time,gym_phone,gym_introduce
              from Gym
              where gym_id = '%s'""" % gid
    some_gym = conn.cursor()
    some_gym.execute(sql)
    some_search_result = some_gym.fetchall()
    return some_search_result

def SearchGymProject(conn, gid):
    sql = """select project_name,project_introduce
              from Project
              where gym_id = '%s'""" % gid
    some_gym = conn.cursor()
    some_gym.execute(sql)
    some_search_result = some_gym.fetchall()
    return some_search_result

def SearchGymCoach(conn, gid):
    sql = """select coach_name,coach_gender,coach_introduce
              from Coach
              where gym_id = '%s'""" % gid
    some_gym = conn.cursor()
    some_gym.execute(sql)
    some_search_result = some_gym.fetchall()
    return some_search_result

def SearchGym(conn, gname, gaddr):
 #   try:
        if not len(gname) and not len(gaddr):
            sql = """select gym_id, gym_name, gym_address, openning_time, gym_phone
                      from Gym"""
        elif not len(gname):
            sql = """select gym_id, gym_name, gym_address, openning_time, gym_phone
                     from Gym
                     where gym_address LIKE '%s'""" % ('%'+gaddr+'%')

        elif not len(gaddr):
            sql = """select gym_id, gym_name, gym_address, openning_time, gym_phone
                     from Gym
                     where gym_name LIKE '%s'""" % ('%'+gname+'%')

        elif len(gname) and len(gaddr):
            sql = """select gym_id, gym_name, gym_address, openning_time, gym_phone
                     from Gym
                     where gym_name LIKE '%s' AND gym_address LIKE '%s'""" % ('%'+gname+'%','%'+gaddr+'%')


        some_gym = conn.cursor()
        some_gym.execute(sql)
        some_search_result = some_gym.fetchall()
#
 #  if len(some_search_result) == 0:
#            print "No matching Gym"
#            return -1
#        else:
        return some_search_result

#    except pyodbc.Error, e:
#        for index in range(len(e.args)):
#            print "Error %s" % (e.args[index])
#        return -1

def SearchCoach(conn, cid, cname,user_account):
#    try:
        sql = ""
        if not len(cid) and not len(cname):
            sql = """select *
                      from Coach
                      where gym_id = '%s'""" % user_account
        elif not len(cid):
            sql = """select *
                      from Coach
                      where coach_name LIKE '%s' and gym_id = '%s'""" % ('%' + cname + '%',user_account)
        elif not len(cname):
            sql = """select *
                      from Coach
                      where coach_id = '%s' and gym_id = '%s'""" % (cid,user_account)
        elif len(cid) and len(cname):
            sql = """select *
                  from Coach
                  where coach_id = '%s' and coach_name LIKE '%s' and gym_id = '%s'""" % (cid,'%'+cname+'%',user_account)

        some_coach = conn.cursor()
        some_coach.execute(sql)
        some_search_result = some_coach.fetchall()
#        if len(some_search_result) == 0:
#            print "No matching coach"
#            return -1
#        else:
        return some_search_result

#    except pyodbc.Error, e:
#        for index in range(len(e.args)):
#            print "Error %s" % (e.args[index])
#        return -1


def SearchProject(conn,user_type,pgym,pname,pdate,ptime):
#    try:
        if user_type == "member":
            if not len(pgym) and not len(pname) and not len(pdate) and not len(ptime):
                sql = """select P.project_id,P.project_name,G.gym_name,P.project_date,P.project_time,P.remaining,P.capacity,P.project_introduce
                        from Project P join Gym G on P.gym_id = G.gym_id"""
            else:
                sql = """select P.project_id,P.project_name,G.gym_name,P.project_date,P.project_time,P.remaining,P.capacity,P.project_introduce
                         from Project P join Gym G on P.gym_id = G.gym_id
                        where G.gym_name like '%s' OR P.project_name LIKE '%s' OR P.project_date = '%s' OR P.project_time  = '%s'""" % ('%' + pgym + '%', '%' + pname + '%', '%' + pdate + '%', '%' + ptime + '%')
        else:
            if not len(pname) and not len(pdate) and not len(ptime):
                sql = """select P.project_id,P.project_name,P.project_date,P.project_time,P.remaining,P.capacity,P.project_introduce
                          from Project P
                          where P.gym_id = '%s'""" % pgym
            else:
                sql = """select P.project_id,P.project_name,P.project_date,P.project_time,P.remaining,P.capacity,P.project_introduce
                         from Project P
                        where (P.project_name LIKE '%s' OR P.project_date = '%s' OR P.project_time  = '%s') and P.gym_id = '%s'""" % ('%'+pname+'%','%'+pdate+'%','%'+ptime+'%',pgym)
        print sql
        some_project = conn.cursor()
        some_project.execute(sql)
        some_search_result = some_project.fetchall()
#        if len(some_search_result) == 0:
#            print "No matching project"
#            return -1
#        else:
        return some_search_result

#    except pyodbc.Error, e:
#        for index in range(len(e.args)):
#            print "Error %s" % (e.args[index])
#        return -1

def SearchAppoint(conn,pname,pdate,user_account,user_type):
 #   try:
        if user_type == "member":
            if not len(pname) and not len(pdate):
                sql = """select A.project_id,P.project_name,P.project_date,P.project_time,P.remaining,P.capacity,G.gym_id,G.gym_name,G.gym_phone,A.mem_id,M.mem_phone
                          from ((Appointment A join Project P on A.project_id = P.project_id) join Gym G on P.gym_id = G.gym_id) join Member M on A.mem_id = M.mem_id
                          where A.mem_id = '%s'""" % (user_account)
            elif not len(pname):
                sql = """select A.project_id,P.project_name,P.project_date,P.project_time,P.remaining,P.capacity,G.gym_id,G.gym_name,G.gym_phone,A.mem_id,M.mem_phone
                          from ((Appointment A join Project P on A.project_id = P.project_id) join Gym G on P.gym_id = G.gym_id) join Member M on A.mem_id = M.mem_id
                           where P.project_date = '%s' and A.mem_id = '%s'""" % (pdate,user_account)
            elif not len(pdate):
                sql = """select A.project_id,P.project_name,P.project_date,P.project_time,P.remaining,P.capacity,G.gym_id,G.gym_name,G.gym_phone,A.mem_id,M.mem_phone
                          from ((Appointment A join Project P on A.project_id = P.project_id) join Gym G on P.gym_id = G.gym_id) join Member M on A.mem_id = M.mem_id
                           where P.project_name LIKE '%s' and A.mem_id = '%s'""" % (pname,user_account)
            else:
                sql = """select A.project_id,P.project_name,P.project_date,P.project_time,P.remaining,P.capacity,G.gym_id,G.gym_name,G.gym_phone,A.mem_id,M.mem_phone
                          from ((Appointment A join Project P on A.project_id = P.project_id) join Gym G on P.gym_id = G.gym_id) join Member M on A.mem_id = M.mem_id
                          where P.project_name LIKE '%s' AND P.project_date = '%s' AND A.mem_id = '%s'""" % ('%'+pname+'%',pdate,user_account)
        else:
            if not len(pname) and not len(pdate):
                sql = """select A.project_id,P.project_name,P.project_date,P.project_time,P.remaining,P.capacity,G.gym_id,G.gym_name,G.gym_phone,A.mem_id,M.mem_phone
                         from ((Appointment A join Project P on A.project_id = P.project_id) join Gym G on P.gym_id = G.gym_id) join Member M on A.mem_id = M.mem_id
                         where G.gym_id = '%s'""" % (user_account)
            elif not len(pname):
                sql = """select A.project_id,P.project_name,P.project_date,P.project_time,P.remaining,P.capacity,G.gym_id,G.gym_name,G.gym_phone,A.mem_id,M.mem_phone
                          from ((Appointment A join Project P on A.project_id = P.project_id) join Gym G on P.gym_id = G.gym_id) join Member M on A.mem_id = M.mem_id
                          where  P.project_date = '%s' and G.gym_id = '%s')""" % (pdate, user_account)
            elif not len(pdate):
                sql = """select A.project_id,P.project_name,P.project_date,P.project_time,P.remaining,P.capacity,G.gym_id,G.gym_name,G.gym_phone,A.mem_id,M.mem_phone
                          from ((Appointment A join Project P on A.project_id = P.project_id) join Gym G on P.gym_id = G.gym_id) join Member M on A.mem_id = M.mem_id
                          where P.project_name = '%s' and G.gym_id = '%s' """ % ('%' + pname + '%', user_account)
            else:
                sql = """select A.project_id,P.project_name,P.project_date,P.project_time,P.remaining,P.capacity,G.gym_id,G.gym_name,G.gym_phone,A.mem_id,M.mem_phone
                         from ((Appointment A join Project P on A.project_id = P.project_id) join Gym G on P.gym_id = G.gym_id) join Member M on A.mem_id = M.mem_id
                         where P.project_name = '%s' AND P.project_date = '%s' AND and G.gym_id = '%s')""" % ('%'+pname+'%',pdate,user_account)

        some_appointment = conn.cursor()
        some_appointment.execute(sql)
        some_search_result = some_appointment.fetchall()
#        if len(some_search_result) == 0:
#            print "No matching Appointment"
#            return -1
#        else:
        return some_search_result

#    except pyodbc.Error, e:
#        for index in range(len(e.args)):
#            print "Error %s" % (e.args[index])
#        return -1