from django.http import HttpResponse
from django.shortcuts import render
from HTML5Project.settings import BASE_DIR

# Create your views here.

from django.shortcuts import render


def MainPage(request):
    contest = {}
    return render(request, 'MainPage.html', contest)


def icon(request):
    file = open(str(BASE_DIR) + '/appfront/dist/favicon.ico', 'rb')
    return HttpResponse(file.read(), content_type='image/ico')