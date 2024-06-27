from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import reverse

from account.models import TestProfile

def index(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        temp = request.POST.get('hello_world_input')

        new_test_model = TestProfile()
        new_test_model.text = temp
        new_test_model.save()

        test_list = TestProfile.objects.all()

        return HttpResponseRedirect(reverse('account:index'))
    test_list = TestProfile.objects.all()
    return render(request, "account/base.html", context={'test_list': test_list})