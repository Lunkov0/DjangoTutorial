from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World!!!')

def detail(request, question_id):
    return HttpResponse("You're looking for at question %s" % question_id)

def results(request, question_id):
    response = "You're looking at results of the question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
