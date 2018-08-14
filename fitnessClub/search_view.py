# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from back_end import Search
from back_end import Login
from back_end import Connect

def search_gym_view(request):
    return render_to_response("search_gym.html")

def search_project_view(request):
    user_account = request.COOKIES.get('user_account')
    user_type = request.COOKIES.get('user_type')
    if user_type == 'member':
        return render_to_response("search_project.html")
    if user_type == 'gym':
        return render_to_response("search_project_guser.html")

def search_coach_view(request):
    return render_to_response("search_coach_guser.html")

def search_appoint_view(request):
    user_account = request.COOKIES.get('user_account')
    user_type = request.COOKIES.get('user_type')
    if user_type == 'member':
        return render_to_response("search_appoint.html")
    if user_type == 'gym':
        return render_to_response("search_appoint_guser.html")

def search_srch_gym(request):
    user_account = request.COOKIES.get('user_account')
    user_password = request.COOKIES.get('user_password')
    user_type = request.COOKIES.get('user_type')
    conn = Login.login(user_account, user_password, user_type)
    context = {}
    if conn == -1:
        return render_to_response("error_page.html", {'error': "连接中断！"})

    if request.method == "POST":
        srch_gname = request.POST.get('keyword_gname')
        srch_gaddr = request.POST.get('keyword_gaddr')
        results = Search.SearchGym(conn,srch_gname,srch_gaddr)

        if len(results):
            context['srch_flag'] = 1
            context['results'] = results
        else:
            context['srch_flag'] = 0
        return render_to_response("search_gym.html", context)
    else:
        return render_to_response("error_page.html", {'error': "request error!"})

def search_srch_project(request):
    user_account = request.COOKIES.get('user_account')
    user_type = request.COOKIES.get('user_type')
    context = {}
    conn = Connect.connect()
    if conn == -1:
        return render_to_response("error_page.html", {'error': "interrupt!"})
    if request.method == "POST":
        srch_pgym = ''
        if user_type == 'member':
            srch_pgym = request.POST.get('keyword_pgym')
        else:
            srch_pgym = user_account
        srch_pname = request.POST.get('keyword_pname')
        srch_pdate = request.POST.get('keyword_pdate')
        srch_ptime = request.POST.get('keyword_ptime')
        results = Search.SearchProject(conn,user_type,srch_pgym,srch_pname,srch_pdate,srch_ptime)
        if len(results):
            context['srch_flag'] = 1
            context['results'] = results
        else:
            context['srch_flag'] = 0
        if user_type == 'member':
            return render_to_response("search_project.html", context)
        else:
            return render_to_response("search_project_guser.html", context)
    else:
        return render_to_response("error_page.html", {'error': "request error!"})

def search_srch_coach(request):
    user_account = request.COOKIES.get('user_account')
    conn = Connect.connect()
    context = {}
    if conn == -1:
        return render_to_response("error_page.html", {'error': "interrupt!"})

    if request.method == "POST":
        srch_cid = request.POST.get('keyword_cid')
        srch_cname = request.POST.get('keyword_cname')
        results = Search.SearchCoach(conn,srch_cid,srch_cname,user_account)
        if len(results):
            context['srch_flag'] = 1
            context['results'] = results
        else:
            context['srch_flag'] = 0
        return render_to_response("search_coach_guser.html", context)
    else:
        return render_to_response("error_page.html", {'error': "request error!"})

def search_srch_appoint(request):
    user_account = request.COOKIES.get('user_account')
    user_type = request.COOKIES.get('user_type')
    conn = Connect.connect()
    context = {}
    if conn == -1:
        return render_to_response("error_page.html", {'error': "interrupt!"})

    if request.method == "POST":
        srch_apname = request.POST.get('keyword_apname')
        srch_apdate = request.POST.get('keyword_apdate')
        results = Search.SearchAppoint(conn,srch_apname,srch_apdate,user_account,user_type)
        if len(results):
            context['srch_flag'] = 1
            context['results'] = results
        else:
            context['srch_flag'] = 0
        if user_type == 'member':
            return render_to_response("search_appoint.html", context)
        else:
            return render_to_response("search_appoint_guser.html", context)
    else:
        return render_to_response("error_page.html", {'error': "request error!"})
