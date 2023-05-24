from django import template

register = template.Library()

@register.filter(name='range_func')
def range_func(number):
    return range(number)