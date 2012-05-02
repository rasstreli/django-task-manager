# Create your views here.
from datetime import datetime
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from persons.models import Person
from persons.forms import PersonForm, LoginForm
def create_account(request):
    template = "create_account.html"
    form = PersonForm(initial={'date_joined':datetime.now()})
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('index')))
    dictToReturn = {'form':form}
    return render_to_response(template,dictToReturn,context_instance = RequestContext(request))

def index(request):
    template = "index.html"
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username,password = password)
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/test')
    dictToReturn={'a':1, 'form':form}
    return render_to_response(template, dictToReturn, context_instance = RequestContext(request))