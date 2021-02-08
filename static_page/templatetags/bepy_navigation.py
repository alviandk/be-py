from django import template

register = template.Library()

@register.simple_tag
def active(path, name):
    try:
        first_path = path.split("/")[1]
    except:
        first_path = ''
    if first_path == name:
        return 'active'
    return ''
