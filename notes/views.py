# Create your views here.
from notes.models import Jobs
from notes.forms import JobForm, UpdateJobForm
from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
def create_job(request):
    template = "jobs/create_job.html"
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = JobForm
    new_dict = {'form':form}
    return render_to_response(template,new_dict, context_instance=RequestContext(request))

def job(request, job_id):
    if job_id:
        list = Jobs.objects.filter(id = job_id)
    else:
        list = ''
    template = "jobs/job.html"
    jobs_list = Jobs.objects.all()
    form = UpdateJobForm()
    testdict = {'jobs':jobs_list,'job':list, 'form':form}
    return render_to_response(template, testdict, context_instance=RequestContext(request))

def job_list(request):
    template = "jobs/job_list.html"
    jobs_list = Jobs.objects.all()
    test_dict = {'jobs':jobs_list,'form':form}
    return render_to_response(template, test_dict, context_instance=RequestContext(request))
