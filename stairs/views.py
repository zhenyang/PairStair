# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.template.context import Context
from stairs.models import Programmer

def index(request):
    programmers = Programmer.objects.all()
    names = []
    for programmer in programmers:
        names.append(programmer.name)
    template = loader.get_template('index.html')
    context = Context(dict_={'programmers': programmers})
    return HttpResponse(template.render(context))