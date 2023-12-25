from django.http import HttpRequest
from django_htmx.middleware import HtmxDetails

# Create your views here.

class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails

def htmx_request_processor(request: HtmxHttpRequest):
    if request.htmx:
        return {"base_template" : "partial.html"}
    return {"base_template" : "base.html"}
