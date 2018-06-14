from django.conf.urls import url
from . import views

urlpatterns = [
    url('getlist', views.getlist),
    url('', views.api404)
]
