from django.template.defaultfilters import stringfilter
from django import template

register = template.Library()

@register.filter(name='replace')
@stringfilter
def replace(value, arg):
    return value.replace(arg,'')

@register.filter(name='cria_label')
@stringfilter
def cria_label(value, arg):
    return arg.upper()+' '+value
