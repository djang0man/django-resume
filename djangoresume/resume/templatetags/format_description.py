from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='format_description', needs_autoescape=True)
def format_description(value, autoescape=True):
    split_desc = value.split('\r\n')
    list_desc = ['<li>' + d + '</li>' for d in split_desc]

    return mark_safe('<ul>' + ''.join(list_desc) + '</ul>')
