from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "account/base.html")
