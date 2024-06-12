from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

# Create your views here.


def index(request):
    # template = loader.get_template("home/index.html")
    return render(request, 'home/index.html', {'today': datetime.today()})
