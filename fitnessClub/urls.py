# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import login_view
from . import home
from . import register_view
from . import search_view
from . import update_user_view
from . import modify
from . import gym_info_view


urlpatterns = [
    url(r'^home$', home.home),
    url(r'^login$',login_view.login_view),
    url(r'^login/log$',login_view.log),
    url(r'^register_mem$', register_view.register_mem_view),
    url(r'^register/reg_mem$', register_view.register_mem),
    url(r'^register_gym$', register_view.register_gym_view),
    url(r'^register/reg_gym$', register_view.register_gym),
    url(r'^home/search/coach$',search_view.search_srch_coach),
    url(r'^home/search_coach$',search_view.search_coach_view),
    url(r'^home/search_gym$',search_view.search_gym_view),
    url(r'^home/search/gym$',search_view.search_srch_gym),
    url(r'^home/search_project$',search_view.search_project_view),
    url(r'^home/search/project$',search_view.search_srch_project),
    url(r'^home/search_appoint$',search_view.search_appoint_view),
    url(r'^home/search/appoint$',search_view.search_srch_appoint),
    url(r'^home/update$',update_user_view.update_user_view),
    url(r'^home/update/mem$', update_user_view.update_mem_view),
    url(r'^home/update/gym$', update_user_view.update_gym_view),
    url(r'^home/add/coach$', modify.add_coach),
    url(r'^home/add/project$', modify.add_project),
    url(r'^home/add/appoint$', modify.add_appoint),
    url(r'^home/alter/coach$', modify.alter_coach),
    url(r'^home/alter/project$', modify.alter_project),
    url(r'^home/delete/appoint$', modify.delete_appoint),
    url(r'^home/delete/project$', modify.delete_project),
    url(r'^home/delete/coach$', modify.delete_coach),
    url(r'^home/search/gym_info$', gym_info_view.gym_info_view),
]
