from django.shortcuts import render
from base.utils import HtmxHttpRequest
from tools.forms import DripperForm
from tools.models import Dripper, EspressoMachine, Grinder
# Create your views here.

def tools(request: HtmxHttpRequest):
    context = {}
    if request.method == "POST":
        form = DripperForm(request.POST)
        if form.is_valid():
            dripper = form.save()
            context["dripper"] = dripper
        return render(request, "tools.html#dripper-items", context)
    dripper = Dripper.objects.all()
    dripper_form = DripperForm
    context["drippers"] = dripper
    context["dripper_form"] = dripper_form

    grinders = Grinder.objects.all()
    context["grinders"] = grinders

    espresso_machines = EspressoMachine.objects.all()
    context["espresso_machines"] = espresso_machines

    if request.htmx:
        return render(request, "tools.html", context)

    return render(request, "tools.html", context)

