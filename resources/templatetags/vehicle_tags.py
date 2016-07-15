from django import template

register = template.Library()

@register.simple_tag
def get_vehicles(total_items):
    list_vehicle = []
    return list_vehicle[:total_items]
