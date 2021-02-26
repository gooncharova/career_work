from django import template

register = template.Library()

ONE_HUNDRED_PER = 100


@register.filter(name='dump_truck_overload')
def dump_truck_overload(weight, carrying):
    overload = ((weight-carrying)/carrying)*ONE_HUNDRED_PER
    if overload < 0:
        return 0
    else:
        return round(overload, 2)
