# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from back_end import Connect
from back_end import GymOperation
from back_end import MemOperation

def delete_appoint(request):
    user_account = request.COOKIES.get('user_account')
    user_type = request.COOKIES.get('user_type')
    conn = Connect.connect()
    if conn == -1:
        return render_to_response("error_page.html", {'error': "interrupt!"})
    context = {}
    if request.method == "POST":
        delete_apid = request.POST.get('dap_id')
        delete_amid = request.POST.get('dam_id')
        results = -1
        if user_type == 'member':
            results = MemOperation.delete_appointment (conn,delete_apid,user_account)
        else:
            results = GymOperation.delete_appointment (conn,delete_apid,delete_amid)
        if results == -1:
            context['delete_flag'] = 0
        else:
            HttpResponse("Delete succeed!")
            context['delete_flag'] = 1
        if user_type == 'member':
            return render_to_response("search_appoint.html",context)
        else:
            return render_to_response("search_appoint_guser.html", context)

    else:
        return render_to_response("error_page.html", {"error": "failed to delete!"})

def add_appoint(request):
    user_account = request.COOKIES.get('user_account')
    user_type = request.COOKIES.get('user_type')
    conn = Connect.connect()
    if conn == -1:
        return render_to_response("error_page.html", {'error': "interrupt!"})
    context = {}
    if request.method == "POST":
        add_apid = request.POST.get('ap_id')
        add_amid = request.POST.get('am_id')
        results = -1
        if user_type == 'member':
            results = MemOperation.insert_appointment_info(conn, add_apid, user_account)
        else:
            results = GymOperation.insert_appointment_info(conn, add_apid,add_amid, user_account)
            print results
        if results == -1:
            context['add_flag'] = 0
        else:
            HttpResponse("Delete succeed!")
            context['add_flag'] = 1
        if user_type == 'member':
            return render_to_response("search_project.html", context)
        else:
            return render_to_response("search_project_guser.html", context)

    else:
        return render_to_response("error_page.html", {"error": "failed to add appointment!"})

def delete_project(request):
        user_account = request.COOKIES.get('user_account')
        conn = Connect.connect()
        if conn == -1:
            return render_to_response("error_page.html", {'error': "interrupt!"})
        context = {}
        if request.method == "POST":
            opera = request.POST.get('modify')
            pid = request.POST.get('dp_id')
            results = -1
            results = GymOperation.delete_project(conn,user_account,pid)
            if results == -1:
                context['delete_flag'] = 0
            else:
                HttpResponse("Delete succeed!")
                context['delete_flag'] = 1
            return render_to_response("search_project_guser.html", context)

        else:
            return render_to_response("error_page.html", {"error": "failed to delete!"})

def add_project(request):
    user_account = request.COOKIES.get('user_account')
    conn = Connect.connect()
    if conn == -1:
        return render_to_response("error_page.html", {'error': "interrupt!"})
    context = {}
    if request.method == "POST":
        pid = request.POST.get('map_id')
        pname = request.POST.get('map_name')
        pdate = request.POST.get('map_date')
        ptime = request.POST.get('map_time')
        pcapa = request.POST.get('map_capa')
        pintro = request.POST.get('map_intro')
        results = -1
        results = GymOperation.insert_project_info(conn, pid, user_account, pname, pdate, ptime, pcapa, pintro,pcapa)
        if results == -1:
            context['add_flag'] = 0
        else:
            HttpResponse("Delete succeed!")
            context['add_flag'] = 1
        return render_to_response("search_project_guser.html", context)

    else:
        return render_to_response("error_page.html", {"error": "failed to delete!"})

def alter_project(request):
    user_account = request.COOKIES.get('user_account')
    conn = Connect.connect()
    if conn == -1:
        return render_to_response("error_page.html", {'error': "interrupt!"})
    context = {}
    if request.method == "POST":
        pid = request.POST.get('map_id')
        pname = request.POST.get('map_name')
        pdate = request.POST.get('map_date')
        ptime = request.POST.get('map_time')
        pcapa = request.POST.get('map_capa')
        premain = request.POST.get('map_remain')
        pintro = request.POST.get('map_intro')
        results = -1
        results = GymOperation.update_project_info(conn, pid, user_account, pname, pdate, ptime, premain, pintro,pcapa)
        if results == -1:
            context['alter_flag'] = 0
        else:
            HttpResponse("Delete succeed!")
            context['alter_flag'] = 1
        return render_to_response("search_project_guser.html", context)

    else:
        return render_to_response("error_page.html", {"error": "failed to modify!"})


def delete_coach(request):
    user_account = request.COOKIES.get('user_account')
    conn = Connect.connect()
    if conn == -1:
        return render_to_response("error_page.html", {'error': "interrupt!"})
    context = {}
    if request.method == "POST":
        delete_cid = request.POST.get('c_id')
        results = -1
        print results
        results = GymOperation.delete_coach(conn, delete_cid,user_account)
        print "2"
        if results == -1:
            context['delete_flag'] = 0
        else:
            HttpResponse("Delete succeed!")
            context['delete_flag'] = 1
        print results
        return render_to_response("search_coach_guser.html", context)

    else:
        return render_to_response("error_page.html", {"error": "failed to delete!"})

def add_coach(request):
    user_account = request.COOKIES.get('user_account')
    conn = Connect.connect()
    if conn == -1:
        return render_to_response("error_page.html", {'error': "interrupt!"})
    context = {}
    if request.method == "POST":
        cid = request.POST.get('c_id')
        cname = request.POST.get('c_name')
        cgender = request.POST.get('c_gender')
        cage = request.POST.get('c_age')
        cphone = request.POST.get('c_phone')
        cintro = request.POST.get('c_intro')
        results = -1
        results = GymOperation.insert_coach_info(conn,cid,user_account,cname,cgender,cage,cphone,cintro)
        if results == -1:
            context['add_flag'] = 0
        else:
            HttpResponse("Delete succeed!")
            context['add_flag'] = 1
        return render_to_response("search_coach_guser.html", context)

    else:
        return render_to_response("error_page.html", {"error": "failed to add coach!"})

def alter_coach(request):
    user_account = request.COOKIES.get('user_account')
    conn = Connect.connect()
    if conn == -1:
        return render_to_response("error_page.html", {'error': "interrupt!"})
    context = {}
    if request.method == "POST":
        cid = request.POST.get('c_id')
        cname = request.POST.get('c_name')
        cgender = request.POST.get('c_gender')
        cage = request.POST.get('c_age')
        cphone = request.POST.get('c_phone')
        cintro = request.POST.get('c_intro')
        results = -1
        results = GymOperation.update_coach_info(conn,cid,user_account,cname,cgender,cage,cphone,cintro)
        print results
        if results == -1:
            context['alter_flag'] = 0
        else:
            HttpResponse("alter succeed!")
            context['alter_flag'] = 1
        return render_to_response("search_coach_guser.html", context)

    else:
        return render_to_response("error_page.html", {"error": "failed to modify coach!"})