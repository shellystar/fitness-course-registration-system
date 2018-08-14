# -*- coding: utf-8 -*-
from back_end import Search
from back_end import Connect
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect


def gym_info_view(request):
    user_account = request.COOKIES.get('user_account')
    user_account = request.COOKIES.get('user_password')
    conn = Connect.connect()
    context = {}

    # check connection with database
    if conn == -1:
        return render_to_response("error_page.html", {'error': "database connection error!"})

    cur_gid = ''
    set_ck_flag = 0
    if request.method == 'POST':
        cur_gid = request.POST.get('g_id')
        set_ck_flag = 1

    # gym information
    gym_info = Search.SearchGymID(conn,cur_gid)
    # gym project
    project_info = Search.SearchGymProject(conn,cur_gid)
    # gym coach
    coach_info = Search.SearchGymCoach(conn,cur_gid)

    context['gym_info'] = gym_info[0]
    if len(project_info):
        context['project_info'] = project_info
        context['p_flag'] = 1
    else:
        context['project_info'] = "nil"
        context['p_flag'] = 0
    if len(coach_info):
        context['coach_info'] = coach_info
        context['c_flag'] = 1
    else:
        context['coach_info'] = "nil"
        context['c_flag'] = 0
    response = render_to_response("gym_info.html", context)

    if set_ck_flag == 1:
        response.set_cookie('gym_id', cur_gid, 3600)

    return response
