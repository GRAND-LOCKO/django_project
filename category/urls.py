from django.urls import path
from . import views

urlpatterns = [
    path("about/", views.about, name='aboutus'),
    # path("", views.hello, name='hello'),
    path("", views.index, name='index'),
    path("timeline/", views.horaire, name='timeline'),
    path("reviews/", views.revu, name='reviews'),
    path("booking/", views.reserver, name='booking'),
    path("learn/", views.info, name='learnn')
]