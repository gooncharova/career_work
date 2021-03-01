from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:dumptruck_id>/<int:coordinate_id>/',
         views.get_calculations, name='calculations'),
]
