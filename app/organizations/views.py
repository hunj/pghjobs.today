from django.views.generic import ListView, DetailView
from .models import Organization


class OrganizationListView(ListView):
    model = Organization
    template_name = 'orgs_list.html'
    context_object_name = 'organizations'


class OrganizationDetailView(DetailView):
    model = Organization
    template_name = 'org_detail.html'
    context_object_name = 'organization'
