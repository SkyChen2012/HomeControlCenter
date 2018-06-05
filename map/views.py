# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response,render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt

# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

# 接收POST请求数据
@csrf_exempt
def searchpost(request):
    print request.POST
    return HttpResponse(request.POST)

def search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)


# 接收POST请求数据
@csrf_exempt
def Address(request):
    print request.POST
    return HttpResponse(request.POST)

