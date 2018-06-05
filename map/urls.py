# -*- coding: utf-8 -*-
#***********************************************
#
#      Filename: urls.py
#
#        Author: Benson - zjxucb@gmail.com
#   Description: ---
#        Create: 2018-06-05 10:35:58
# Last Modified: 2018-06-05 10:35:59
#***********************************************
from __future__ import unicode_literals
from django.conf.urls import include, url  
from map.views import *

urlpatterns = [ 
    url(r'^search$', search),
    url(r'^search-post$', search_post),
    url(r'^searchpost$',searchpost),
    url(r'^Address$',Address)
]

