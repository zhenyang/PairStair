# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.template.context import Context
from stairs.models import Programmer

def index(request):
    programmers = Programmer.objects.all().order_by('name')
    template = loader.get_template('index.html')
    context = Context(dict_={'programmers': programmers})
    return HttpResponse(template.render(context))


def add_pair(request, firstProgrammer_id, secondProgrammer_id):
    first_programmer=Programmer.objects.get(id=firstProgrammer_id)
    second_programmer=Programmer.objects.get(id=secondProgrammer_id)
    first_programmer.add_pairing_with(second_programmer)
    return redirect('/index')


def add_programmer(request):
    pass