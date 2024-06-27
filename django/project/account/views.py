from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        return render(request, "account/base.html", context={'text': 'POST METHOD!'})
    return render(request, "account/base.html", context={'text': 'GET METHOD!'})
