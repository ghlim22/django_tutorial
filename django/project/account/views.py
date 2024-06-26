from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, HttpResponseForbidden
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from .deco import account_ownership_required
from .forms import AccountUpdateForm
from .models import TestProfile

has_ownership = [login_required, account_ownership_required]


@login_required
def index(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        temp = request.POST.get('hello_world_input')

        new_test_model = TestProfile()
        new_test_model.text = temp
        new_test_model.save()

        test_list = TestProfile.objects.all()

        return HttpResponseRedirect(reverse('account:index'))
    else:
        test_list = TestProfile.objects.all()
        return render(request, template_name="account/base.html", context={'test_list': test_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("account:index")
    template_name = "account/create.html"


@method_decorator(has_ownership, 'get')
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = "account/detail.html"


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm;
    success_url = reverse_lazy("account:index")
    template_name = "account/update.html"


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy("account:login")
    template_name = "account/delete.html"
