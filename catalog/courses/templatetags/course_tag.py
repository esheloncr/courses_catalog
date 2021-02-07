from django import template
from django.utils import timezone
from ..models import Course
from ..filters import Filter
register = template.Library()


@register.simple_tag()
def get_courses():
    now = timezone.now()
    return Course.objects.filter(start_date__gte=now).order_by("start_date").first()


@register.simple_tag()
def get_query():
    return Course.objects.all()


@register.simple_tag()
def filters():
    return Filter()


"""passed = Event.objects.filter(date__lt=now).order_by('-date')
Прошедший курс
"""
#return Course.objects.all().order_by("start_date").reverse().first()