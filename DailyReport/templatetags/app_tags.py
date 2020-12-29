# 現在不使用。後で修正。
from django import template
from DailyReport.models import Item

register = template.Library()


# @register.inclusion_tag('DailyReport/includes/tmp_count.html')
@register.inclusion_tag('DailyReport/includes/tmp_count.html')
def render_tmp_count():
    return {
        'tmp_count': Item.objects.all(),
    }
