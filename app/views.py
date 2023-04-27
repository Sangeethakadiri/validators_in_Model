from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.forms import *
def insert_topic(request):
    TF=TopicForm()
    d={'TF':TF}

    if request.method=="POST":
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('Topic is inserted')
        else:
            return HttpResponse('data is not valid')

    return render(request,'insert_topic.html',d)
