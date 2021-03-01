from django.shortcuts import get_object_or_404, redirect, render

from .additions import (get_equation_of_line,
                        get_mineral_quality_characteristics)
from .forms import CoordinateForm
from .models import (Coordinate, DumpTruck, DumpTruckMineral, Mineral,
                     WarehouseMineral)


def index(request):
    """ Главная страница. Выводим информацию о всех
    самосвалах в таблицы, форму для введения координаты """
    all_dump_trucks = DumpTruck.objects.all()
    form = CoordinateForm(request.POST or None)
    if form.is_valid():
        new_coordinate = form.save(commit=False)
        new_coordinate.save()
        dumptruck_id = request.POST['dumptruck_id']
        coordinate_id = new_coordinate.id
        return redirect('calculations', dumptruck_id=dumptruck_id,
                        coordinate_id=coordinate_id)
    context = {'all_dump_trucks': all_dump_trucks, 'form': form}
    return render(request, 'index.html', context)


def get_calculations(request, dumptruck_id, coordinate_id):
    """ Смотрим, попадает ли введенная координата в заданную
    область полигона склада. В зависимости от этого выводим
    нобходимую информацию о складе в таблицу  """
    dump_truck = get_object_or_404(DumpTruck, id=dumptruck_id)
    warehouse = dump_truck.warehouse
    warehouse_polygon = warehouse.polygon_coord.values()
    coordinate = get_object_or_404(Coordinate, id=coordinate_id)
    equations_of_line = []
    # В цикле ниже получаем все возможные отрезки для заданных
    # координат полигона и уравнения прямых для них
    for i in range(len(warehouse_polygon)):
        for j in range(i+1, len(warehouse_polygon)):
            equations_of_line.append(get_equation_of_line(
                warehouse_polygon[i], warehouse_polygon[j]))
    y_lines = []
    # В новом цикле проверяем попадает ли x из заданной координаты
    # в промежуток [x1, x2] для каждого уравнения прямой. В случае
    # попадания подставляем x в соответствующее уравнение прямой.
    for item in equations_of_line:
        if (item['x_interval'][0] <= coordinate.x_coordinate
                <= item['x_interval'][1]):
            y_line = item['k'] * coordinate.x_coordinate + item['b']
            y_lines.append(y_line)
    # В списке y_lines все посчитанные y для x,
    #  попавших в промежуток [x1, x2]
    y_lines = sorted(y_lines)
    warehouse_mineral = get_object_or_404(
        WarehouseMineral, warehouse=warehouse)
    print(warehouse_mineral)
    dumptruck_mineral = get_object_or_404(
        DumpTruckMineral, dump_truck=dump_truck)
    # Проверяем, попадает ли y заданной координаты в посчитанные y.
    # Если да - координата попала в область полигона, считаем
    # информацию по складу, сохраняем ее в базу
    warehouse_mineral_weight_bef = warehouse_mineral.weight
    warehouse_mineral_weight_aft = warehouse_mineral.weight
    mineral = get_object_or_404(Mineral, id=warehouse_mineral.mineral.id)
    if y_lines:
        if y_lines[0] <= coordinate.y_coordinate <= y_lines[-1]:
            warehouse_mineral.weight += dumptruck_mineral.weight
            warehouse_mineral.save()
            warehouse_mineral_weight_aft = warehouse_mineral.weight
            wh_mineral_cont = get_mineral_quality_characteristics(
                warehouse_mineral, dumptruck_mineral)
            mineral.iron_content = wh_mineral_cont[1]
            mineral.silicon_content = wh_mineral_cont[0]
            mineral.save()
    context = {'warehouse': warehouse,
               'warehouse_mineral_weight_bef': warehouse_mineral_weight_bef,
               'warehouse_mineral_weight_aft': warehouse_mineral_weight_aft,
               'mineral': mineral,
               }
    return render(request, 'calculations.html', context)
