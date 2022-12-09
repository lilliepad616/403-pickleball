from django.urls import path
from .views import indexPageView
from .views import aboutPageView
from .views import equipPageView
from .views import courtsPageView
from .views import courtsCreatePageView
from .views import courtsUpdatePageView
from .views import courtsDeletePageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("about/", aboutPageView, name="about"),
    path("equip/", equipPageView, name="equip"),
    path("courts/", courtsPageView, name="courts"),
    path("courts/create/", courtsCreatePageView, name="create"),   
    path("courts/update/", courtsUpdatePageView, name="update"),   
    path("courts/delete/", courtsDeletePageView, name="delete"),   
] 