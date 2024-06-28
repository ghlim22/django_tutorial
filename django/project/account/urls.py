from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path("", views.index),
    path("base/", views.index, name="index"),
    path("create/", views.AccountCreateView.as_view(), name="create")
]
