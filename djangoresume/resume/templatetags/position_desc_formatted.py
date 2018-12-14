from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='position_desc_formatted', needs_autoescape=True)
def position_desc_formatted(value, autoescape=True):
    split_desc = value.split('- ')
    joined_desc = ''.join(split_desc).split('\r\n')
    list_desc = ['<li>' + d + '</li>' for d in joined_desc]

    return mark_safe('<ul>' + ''.join(list_desc) + '</ul>')
