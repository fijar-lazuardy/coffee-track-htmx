from django.urls import path
from tools.views import *

urlpatterns = [
    path("", tools, name="tools")
]
