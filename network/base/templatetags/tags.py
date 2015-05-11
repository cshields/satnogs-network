import re

from django import template

register = template.Library()


@register.simple_tag
def active(request, pattern):
    if re.search(pattern, request.path):
        return 'active'
    return None


@register.simple_tag
def frq(value):
    to_format = float(value)
    formatted = format(float(to_format) / 1000000, '.3f')
    formatted = formatted + ' Mhz'
    return formatted
