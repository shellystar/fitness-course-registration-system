# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from back_end import Login

def login_view(request):
    return render_to_response("login.html")

def log(request):
    if request.method == 'POST':
        user = request.POST
        conn = Login.login(user['user_account'], user['user_password'],user['user_type'])
        if conn == -1:
            return render_to_response("error_page.html", {"error": "failed！"})
        else:
            response = HttpResponseRedirect('/home')
            response.set_cookie('user_account',user['user_account'],3600)
            response.set_cookie('user_password',user['user_password'],3600)
            response.set_cookie('user_type',user['user_type'],3600)
            return response
