from django import template
import random

from minerals.models import Mineral

register = template.Library()

@register.filter('verbose_name')
def verbose_name(obj, field_name):
    return obj._meta.get_field(field_name).verbose_name
    
@register.filter('get_attr')
def get_attr(obj, val): 
    return getattr(obj, val)

@register.simple_tag
def rand_pk():
    return random.randint(1,874)