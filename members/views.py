from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

def index(request):
    members = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'members': members
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    new_firstname = request.POST['first']
    new_lastname = request.POST['last']
    new_member = Members(firstname=new_firstname, lastname=new_lastname)
    new_member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    member = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'member': member
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    new_firstname = request.POST['first']
    new_lastname = request.POST['last']
    member = Members.objects.get(id=id)
    member.firstname = new_firstname
    member.lastname = new_lastname
    member.save()
    return HttpResponseRedirect(reverse('index'))