# Create your views here.
from django.shortcuts import redirect, render_to_response
from django.template.context import  RequestContext
from stairs.models import Programmer

def index(request):
    programmers = Programmer.objects.all().order_by('name')
    return render_to_response('index.html', RequestContext(request, {'programmers': programmers}))

def add_pair(request, firstProgrammer_id, secondProgrammer_id):
    first_programmer = Programmer.objects.get(id=firstProgrammer_id)
    second_programmer = Programmer.objects.get(id=secondProgrammer_id)
    first_programmer.add_pairing_with(second_programmer)
    return redirect('/index')

def add_programmer(request):
    if request.method == 'POST':
        name = request.POST['programmer_name']
        Programmer(name=name).save()
        return redirect('/index')
    return render_to_response('add_programmer.html', RequestContext(request))