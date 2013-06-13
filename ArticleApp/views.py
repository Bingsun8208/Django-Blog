# Create your views here.
# -*-  coding:utf-8 -*-
from django.http import HttpResponse
from django.http import Http404
from django.core.mail import EmailMessage
from django.template import loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from AccountApp.views import getSession

from ArticleApp.models import *
import datetime

@csrf_exempt
def _404(request):
    return render(request, '404.html')

@csrf_exempt
def index(request):
    boards_obj = boards.objects.all()
    article_obj = articles.objects.order_by('-publishDate').all()[:10]

    arr = getSession(request)
    arr["boardList"] = boards_obj
    arr["articleList"] = article_obj

    return render(request,'index.html', arr)

@csrf_exempt
def right(request):
    return render(request,'rightContent.html',{"users":'yubing'})

@csrf_exempt
def board(request, boardNameFilter, pageNo=1):
    arr = getSession(request)
    board = boards.objects.filter(boardName=boardNameFilter)[0]
    if pageNo == u'':
        pageNo = u'1'
    pageNo = int(pageNo)
    if pageNo < 1:
        pageNo = 1
    startIndex = (pageNo - 1) * 20 + 1
    endIndex = pageNo * 20
    articles_obj = board.articles_set.all()[startIndex:endIndex]

    arr["board"] = board
    arr["articleList"] = articles_obj
    return render(request,'boardList.html', arr)

@csrf_exempt
def article(request, articleId):
    arr = getSession(request)
    articleId = int(articleId)
    articles_obj = articles.objects.filter(articleId=articleId)
    if articles_obj.count() == 0:
        return render(request, '404.html')
    articleObj = articles_obj[0]
    arr["article"] = articleObj


    replyList = replies.objects.filter(article__articleId=articleId)
    arr["replyList"] = replyList

    return render(request, 'article.html', arr)