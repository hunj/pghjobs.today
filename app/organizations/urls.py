from django.urls import path

from .views import OrganizationListView, OrganizationDetailView


urlpatterns = [
    path("", OrganizationListView.as_view(), name="organizations_list"),
    path("<slug:slug>", OrganizationDetailView.as_view(), name="organization_detail"),
]
