from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculations', views.get_calculations, name='calculations'),
]
