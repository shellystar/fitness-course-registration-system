# -*- coding: utf-8 -*-
from back_end import MemOperation
from back_end import GymOperation
from back_end import Connect
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

def update_user_view(request):
    user_type = request.COOKIES.get('user_type')
    if user_type == 'member':
        return render_to_response("updatemember.html")
    else:
        return render_to_response("updategym.html")

def update_mem_view(request):
    user_account = request.COOKIES.get('user_account')
    conn = Connect.connect()

    if request.method == "POST":
        u_password = request.POST.get('u_password')
        if u_password == u"":
            return render_to_response("error_page.html", {"error": "password shoudn't be empty"})
        u_name = request.POST.get('u_name', 'NULL')
        gender = request.POST.get('gender', 'NULL')
        phone = request.POST.get('phone', 0)
        age = request.POST.get('age', 0)
        if MemOperation.update_member_info(conn,user_account,u_password,u_name,gender,phone,age) == -1:
            return render_to_response("error_page.html")
        else:
            HttpResponse("Modify succeed!")
            return HttpResponseRedirect('/home')
    else:
        return render_to_response("error_page.html", {"error": "failed to modify"})

def update_gym_view(request):
    user_account = request.COOKIES.get('user_account')
    conn = Connect.connect()

    if request.method == "POST":
        u_password = request.POST.get('g_password', "")
        if u_password == u"":
            return render_to_response("error_page.html", {"error": "password shoudn't be empty"})
        u_name = request.POST.get('g_name', 'NULL')
        g_addr = request.POST.get('g_addr', 'NULL')
        g_phone = request.POST.get('g_phone', 0)
        g_open = request.POST.get('g_open', 0)
        g_intro = request.POST.get('g_intro', 0)
        if GymOperation.update_gym_info(conn,user_account,u_password,u_name,g_addr,g_open,g_phone,g_intro) == -1:
            return render_to_response("error_page.html")
        else:
            HttpResponse("Modify succeed!")
            return HttpResponseRedirect('/home')
    else:
        return render_to_response("error_page.html", {"error": "failed to modify"})