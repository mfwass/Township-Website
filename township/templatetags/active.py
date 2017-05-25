from django import template
from django.core.urlresolvers import reverse, NoReverseMatch

register = template.Library()


@register.simple_tag(takes_context=True)
def active(context, test_path):
    path = context['request'].path
    if path == test_path:
        return 'active'
    return ''