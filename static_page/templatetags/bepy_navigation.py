from django import template

register = template.Library()

@register.simple_tag
def active(path, name):
    first_path = path.split("/")[1]
    if first_path == name:
        return 'active'
    return ''
