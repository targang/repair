from django.http.request import HttpRequest
from .models import Order
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

from pages.forms import OrderForm


@require_http_methods(["POST"])
def create_order(request: HttpRequest):
    name = request.POST["name"]
    phone = request.POST["phone"]
    message = request.POST["message"] or None
    if name and phone:
        Order.objects.create(name=name, phone=phone, message=message)

        return HttpResponse(status=200)
