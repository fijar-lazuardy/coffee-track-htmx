from django.shortcuts import render
from base.utils import HtmxHttpRequest
from tools.models import Dripper
# Create your views here.

def tools(request: HtmxHttpRequest):
    context = {}
    # if request.htmx
    tool_name = request.GET.get("name", "")
    if tool_name == "dripper" or not tool_name:
        print("ada di sini")
        dripper = Dripper.objects.all()
        context["drippers"] = dripper
        context["dripper_fragment"] = "dripper.html"
        if request.htmx:
            return render(request, "tools.html", context)
        print(context)
        return render(request, "tools.html", context)

    return render(request, "tools.html", context)

