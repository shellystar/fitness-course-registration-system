# -*- coding: utf-8 -*-
from back_end import Register
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

def register_mem_view(request):
    return render_to_response("registermember.html")

def register_mem(request):
    if request.method == "POST":
        u_account = request.POST.get('u_account', "")
        u_password = request.POST.get('u_password', "")
        if u_account == u"" or u_password == u"":
            return render_to_response("error_page.html", {"error": "login and password shouldn't be empty!"})
        u_name = request.POST.get('u_name', 'NULL')
        gender = request.POST.get('gender', 'NULL')
        phone = request.POST.get('phone', 0)
        age = request.POST.get('age', 0)
        if Register.newMember(u_account, u_password, u_name, gender, phone, age) == -1:
            return render_to_response("error_page.html")
        else:
            HttpResponse("Register succeed!")
            return HttpResponseRedirect('/login')
    else:
        return render_to_response("error_page.html", {"error": "注册失败！"})

def register_gym_view(request):
    return render_to_response("registergym.html")

def register_gym(request):
    if request.method == "POST":
        u_account = request.POST.get('g_account', "")
        u_password = request.POST.get('g_password', "")
        if u_account == u"" or u_password == u"":
            return render_to_response("error_page.html", {"error": "login and password shouldn't be empty!"})
        u_name = request.POST.get('g_name', 'NULL')
        g_addr = request.POST.get('g_addr', 'NULL')
        g_phone = request.POST.get('g_phone', 0)
        g_open = request.POST.get('g_open', 0)
        g_intro = request.POST.get('g_intro', 0)
        if Register.newGym(u_account,u_password,u_name,g_addr,g_open,g_phone,g_intro) == -1:
            return render_to_response("error_page.html")
        else:
            HttpResponse("Register succeed!")
            return HttpResponseRedirect('/login')
    else:
        return render_to_response("error_page.html", {"error": "failed to register"})