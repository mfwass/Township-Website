from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def active(context, test_path):
    path = context['request'].path
    if path == test_path:
        return 'active'
    return ''