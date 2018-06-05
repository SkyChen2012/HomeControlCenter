# -*- coding: utf-8 -*-
#***********************************************
#
#      Filename: urls.py
#
#        Author: Benson - zjxucb@gmail.com
#   Description: ---
#        Create: 2018-06-05 10:19:59
# Last Modified: 2018-06-05 10:20:02
#***********************************************

from __future__ import unicode_literals
from django.conf.urls import include, url  
from blog.views import *

urlpatterns = [ 
	# blog_1  
    url(r'^$',index),
    url(r'^blog/(?P<slug>[^\.]+).html', view_post, name='view_blog_post'),  
]
