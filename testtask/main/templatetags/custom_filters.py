from django import template

register = template.Library()

@register.filter
def sequence_num(value, arg):
    index = arg - 1
    return value + (100 * index)
