from django.shortcuts import get_object_or_404, render

from .models import Coordinate, DumpTruck, Mineral, Warehouse


def index(request):
    all_dump_trucks = DumpTruck.objects.all()
    context = {'all_dump_trucks': all_dump_trucks}
    return render(request, 'index.html', context)


def get_calculations(request):
    pass
