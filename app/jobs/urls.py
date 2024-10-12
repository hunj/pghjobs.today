from django.urls import path

from .views import JobsView


urlpatterns = [
    path("", JobsView.as_view(), name="jobs_list"),
]