from typing import Any
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from jobs.models import Job


class JobSearchView(ListView):
    model = Job
    template_name = 'job_list.html'
    paginate_by = 15
    context_object_name = "jobs"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        qs = Job.objects.all()
        if query := self.request.GET.get('q'):
            print(query)
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(location__icontains=query) |
                Q(description__icontains=query)
                )
        return qs


class JobDetailView(DetailView):
    model = Job
    template_name = 'job_detail.html'
    context_object_name = "job"
