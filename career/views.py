from django.shortcuts import get_object_or_404, redirect, render

from .forms import CoordinateForm
from .models import Coordinate, DumpTruck, Mineral, Warehouse


def index(request):
    all_dump_trucks = DumpTruck.objects.all()
    form = CoordinateForm(request.POST)
    if form.is_valid():
        new_coordinate = form.save(commit=False)
        new_coordinate.save()
        return redirect('calculations')
    form = CoordinateForm()
    context = {'all_dump_trucks': all_dump_trucks, 'form': form}
    return render(request, 'index.html', context)


def get_calculations(request, title):
    warehouse = get_object_or_404(Warehouse, title=title)
    context = {'warehouse': warehouse}
    return render(request, 'calculations.html', context)
