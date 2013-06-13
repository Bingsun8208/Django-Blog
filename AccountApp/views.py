# Create your views here.
# -*-  coding:utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.core.mail import EmailMessage
from django.template import loader
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

import json
import time

from AccountApp.models import *

def getSession(request):
    accounts = None
    if "accounts" in request.session:
        accounts = request.session["accounts"]
    else:
        request.session["accounts"] = None
    accountId = None
    if "accountId" in request.session:
        accountId = request.session["accountId"]
    else:
        request.session["accountId"] = None
    if accountId == None:
        accountId = ''

    accountCreateDate = None
    if "accountCreateDate" in request.session:
        accountCreateDate = request.session["accountCreateDate"]
    else:
        request.session["accountCreateDate"] = None
    if accountCreateDate == None:
        accountCreateDate = ''

    return {
        'accounts': accounts,
        'sessionUserName': accountId,
        'accountCreateDate': accountCreateDate,
    }

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        userpwd  = request.POST.get('userpwd')

        if username and userpwd:
            accountObjs = accounts.objects.filter(accountId = username).filter(accountPwd = userpwd)
            if accountObjs:
                request.session["accounts"] = accountObjs[0]
                request.session["accountId"] = accountObjs[0].accountId
                request.session["accountCreateDate"] = accountObjs[0].createDate
                return HttpResponse(json.dumps({"loginStatus": "success", "errorMsg": u""}))
            else:
                return HttpResponse(json.dumps({"loginStatus": "failed", "errorMsg": u"用户名或密码错误"}))
        else:
            return HttpResponse(json.dumps({ "loginStatus": "failed", "errorMsg": u"用户名或密码错误"}))
    else:
        return HttpResponse(json.dumps({"loginStatus": "failed", "errorMsg": u"未正常接收到登陆数据，请重试"}))

@csrf_exempt
def logout(request):
    request.session["accounts"] = None
    request.session["accountId"] = None
    request.session["accountCreateDate"] = None

    arr = getSession(request)
    #return render(request, 'index.html', arr)

    return HttpResponseRedirect("/")

@csrf_exempt
def profile(request):
    arr = getSession(request)
    if arr['accounts'] == None:
        return render(request, '404.html')
    else:
        return render(request, 'profile.html', arr)

@csrf_exempt
def modifypwd(request):
    arr = getSession(request)
    if "accountId" in request.session:
        if request.method == 'POST':
            userOldPwd = request.POST.get('userOldPwd')
            userNewPwd = request.POST.get('userNewPwd')
            accountObj = accounts.objects.filter(accountId = arr["accountId"]).filter(accountPwd = userOldPwd)
            if accountObj:
                account = accountObj[0]
                account.accountPwd = userNewPwd
                account.save()
                return HttpResponse(json.dumps({ "status": "success", "errorMsg": u""}))
            else:
                return HttpResponse(json.dumps({ "status": "failed", "errorMsg": u"原密码错误"}))
        return render(request, 'index.html', arr)
    else:
        return render(request, 'index.html', arr)