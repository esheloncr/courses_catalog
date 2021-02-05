from django import template
from ..models import Course

register = template.Library()


@register.simple_tag()
def get_courses():
    return Course.objects.all().order_by("start_date").reverse().first()


@register.simple_tag()
def get_query():
    return Course.objects.all()

