from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Url, Info
from multiprocessing import Process
from urlparse.threads import main


def index(request):
    result = render(request, 'urlparse/index.html')
    return result

def get_data(request):
    p = Process(target=main)
    p.start()
    p.join()
    return HttpResponse('ok')

def load_data(request):
    data = serializers.serialize('json', Info.objects.all())
    return HttpResponse(data)
