from django.shortcuts import render
from app.models import *
# Create your views here.

def dis_topic(request):
    LOT=Topic.objects.all()
    LOT=Topic.objects.filter(topic_name='cricket')
    d={'topic':LOT}
    return render(request,'dis_topic.html',d)


def dis_web(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(topic_name='cricket')
    LOW=Webpage.objects.filter(url='http://virat.com')
    d={'web':LOW}
    return render(request,'dis_web.html',d)

def dis_access(request):
    LOA=Access.objects.all()
    LOA=Access.objects.filter(author='ronda')
    d={'access':LOA}
    return render(request,'dis_access.html',d)