from django import template

from township.models import SiteBanner

register = template.Library()

@register.simple_tag
def banner():
    return SiteBanner.get()