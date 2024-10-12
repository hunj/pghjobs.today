from django.views.generic import ListView
from jobs.models import Job

class JobsView(ListView):
    model = Job
