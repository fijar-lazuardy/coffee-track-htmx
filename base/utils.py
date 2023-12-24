from django_htmx.middleware import HtmxDetails
from django.http import HttpRequest

class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails
