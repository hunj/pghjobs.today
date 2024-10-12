from django.urls import path

from .views import JobSearchView, JobDetailView


urlpatterns = [
    path("<uuid:pk>", JobDetailView.as_view(), name="job_detail"),
]
