from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django_htmx.middleware import HtmxDetails
from grinder.forms import GrinderForm
from grinder.models import Grinder, GrinderBrand

# Create your views here.

class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails

def grinder(request: HtmxHttpRequest) -> HttpResponse:
    context = {}
    if request.method == "POST":
        form = GrinderForm(request.POST)
        if form.is_valid():
            grinder_count = Grinder.objects.count()
            grinder = insert_grinder(form)
            context["grinder"] = grinder
            context["grinder_count"] = grinder_count + 1
            return render(request, "grinder.html#grinder-item", context)
    grinders = Grinder.objects.all().order_by("id")
    page_num = request.GET.get("page", "1")
    page = Paginator(object_list=grinders, per_page=1).get_page(page_num)
    form = GrinderForm()
    context = {
        "page": page,
        "grinders": grinders,
        "form": form,
    }
    return render(
        request,
        "grinder.html",
        context
    )

def insert_grinder(form) -> Grinder:
    brand: GrinderBrand = form.cleaned_data["brand"]
    model = form.cleaned_data["model"]

    grinder = Grinder.objects.create(model=model, brand=brand)
    grinder.save()
    return grinder
