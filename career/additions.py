from career_work.settings import ONE_HUNDRED_PER


def get_equation_of_line(dot1, dot2):
    """ Находим k и b из уравнения прямой типа kx+b
    А также промежуток [x1, x2] """
    dot1_x = dot1['x_coordinate']
    dot1_y = dot1['y_coordinate']
    dot2_x = dot2['x_coordinate']
    dot2_y = dot2['y_coordinate']
    k = (dot2_y - dot1_y) / (dot2_x - dot1_x)
    b = dot1_y - k * dot1_x
    if dot1_x < dot2_x:
        x_interval = [dot1_x, dot2_x]
    else:
        x_interval = [dot2_x, dot1_x]
    return {'k': round(k, 2), 'b': round(b, 2), 'x_interval': x_interval}


def get_mineral_weight(mineral_weight, mineral_content):
    """ Находим массу полезного вещества в руде """
    mineral_weight = mineral_weight * (mineral_content/ONE_HUNDRED_PER)
    return mineral_weight


def get_mineral_quality_characteristics(warehouse_mineral, dumptruck_mineral):
    """ Находим качественные характеристики руды после разгрузки.
    Могу лишь извиниться за код ниже:) Он безусловно кошмарный
    и требует переделки. """
    warehouse_mineral_weight = warehouse_mineral.weight
    dumptruck_mineral_weight = dumptruck_mineral.weight
    warehouse_mineral_silicon_cont = warehouse_mineral.mineral.silicon_content
    warehouse_mineral_iron_cont = warehouse_mineral.mineral.iron_content
    dumptruck_mineral_silicon_cont = dumptruck_mineral.mineral.silicon_content
    dumptruck_mineral_iron_cont = dumptruck_mineral.mineral.iron_content
    SiO2_weight_warehouse = get_mineral_weight(
        warehouse_mineral_weight, warehouse_mineral_silicon_cont)
    Fe_weight_warehouse = get_mineral_weight(
        warehouse_mineral_weight, warehouse_mineral_iron_cont)
    SiO2_weight_dumptruck = get_mineral_weight(
        dumptruck_mineral_weight, dumptruck_mineral_silicon_cont)
    Fe_weight_dumptruck = get_mineral_weight(
        dumptruck_mineral_weight, dumptruck_mineral_iron_cont)
    mineral_new_weight = warehouse_mineral_weight + dumptruck_mineral_weight
    SiO2_new_weight = SiO2_weight_warehouse + SiO2_weight_dumptruck
    Fe_new_weight = Fe_weight_warehouse + Fe_weight_dumptruck
    warehouse_mineral_silicon_cont = (
        SiO2_new_weight * ONE_HUNDRED_PER)/mineral_new_weight
    warehouse_mineral_iron_cont = (
        Fe_new_weight * ONE_HUNDRED_PER)/mineral_new_weight
    return [int(warehouse_mineral_silicon_cont),
            int(warehouse_mineral_iron_cont)]
