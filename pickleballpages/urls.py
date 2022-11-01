from django.urls import path
from .views import indexPageView
from .views import aboutPageView
from .views import equipPageView
from .views import courtsPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("about/", aboutPageView, name="about"),
    path("equip/", equipPageView, name="about"),
    path("courts/", courtsPageView, name="about"),   
] 