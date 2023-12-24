from django.urls import path
from grinder.views import *

urlpatterns = [
    path("", grinder, name="grinder"),
]
