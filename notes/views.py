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
    dict_to_return = {'form':form}
    return render_to_response(template,dict_to_return,context_instance=RequestContext(request))

def job(request, job_id):
    if job_id:
        job = Jobs.objects.filter(id = job_id)
    else:
        job = ''
    template = "jobs/job.html"
    form = UpdateJobForm()
    dict_to_return = {'job':job, 'form':form}
    return render_to_response(template, dict_to_return, context_instance=RequestContext(request))

def job_list(request):
    template = "jobs/job_list.html"
    jobs_list = Jobs.objects.all()
    dict_to_return = {'jobs':jobs_list}
    return render_to_response(template, dict_to_return, context_instance=RequestContext(request))
