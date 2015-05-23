from django import template

from ..models import Brother

register = template.Library()

@register.assignment_tag
def assignment_tag():
    pass
