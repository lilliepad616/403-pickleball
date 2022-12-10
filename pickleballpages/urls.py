from django.urls import path
from .views import indexPageView
from .views import aboutPageView
from .views import equipPageView
from .views import showCourtsPageView
from .views import addCourtPageView
from .views import showSingleCourtPageView
from .views import updateCourtPageView
from .views import deleteCourtPageView

urlpatterns = [
    path("about/", aboutPageView, name="about"),
    path("equip/", equipPageView, name="equip"),
    path("courts/", showCourtsPageView, name="courts"),
    path("showCourt/<int:court_id>/", showSingleCourtPageView, name="showSingleCourt"),
    path("updateCourt/", updateCourtPageView, name="updateCourt"),
    path("deleteCourt/<int:court_id>/", deleteCourtPageView, name="deleteCourt"),
    path("addCourt/", addCourtPageView, name="addCourt"),
    path("", indexPageView, name="index"),
] 