from django import template
register = template.Library()

@register.filter
def aster(count: int) -> str:
    return '*' * count