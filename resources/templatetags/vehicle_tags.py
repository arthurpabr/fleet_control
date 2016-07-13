from django import template

register = template.Library()

@register.simple_tag
def get_vehicles(total_items):
    list_vehicle = list()
    list_vehicle.append('Uno')
    list_vehicle.append('Fox')
    list_vehicle.append('Saveio')
    list_vehicle.append('Cruze')
    list_vehicle.append('Celta')
    list_vehicle.append('Paraty')
    list_vehicle.append('Onix')

    return list_vehicle[:total_items]
