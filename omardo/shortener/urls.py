from django.urls import path

from . import views

app_name = "shortener"

urlpatterns = [
    path("_<key>/", views.get_redirect, name="redirect"),
    path("_/<key>/", views.get_redirect, name="redirect"),
]
