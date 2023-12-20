from django.urls import path
from grinder.views import grinder_all

urlpatterns = [
    path("", grinder_all)
]
