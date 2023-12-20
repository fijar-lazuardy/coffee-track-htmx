from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django_htmx.middleware import HtmxDetails
from grinder.models import Grinder

# Create your views here.

class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails

def grinder_all(request: HtmxHttpRequest) -> HttpResponse:
    grinders = Grinder.objects.all()
    page_num = request.GET.get("page", "1")
    page = Paginator(object_list=grinders, per_page=10).get_page(page_num)
    if request.htmx:
        print("di htmx")
        base_template = "partial.html"
    else:
        print("true")
        base_template = "base.html"
    return render(
        request,
        "grinder.html",
        {
            "base_template": base_template,
            "page": page,
        },
    )

def add_grinder(request):
    return "a"

