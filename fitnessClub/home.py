# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    user_account = request.COOKIES.get('user_account')
    user_type = request.COOKIES.get('user_type')
    if user_account.__len__() != 0 and user_type == 'member':
        return render_to_response("home_mem.html", {'user_account': user_account})
    if user_account.__len__() != 0 and user_type == 'gym':
        return render_to_response("home_gym.html", {'user_account': user_account})
    else:
        return render_to_response("error_page.html", {'error': "No user_account!"})