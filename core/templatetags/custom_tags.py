from django import template


register = template.Library()


@register.filter
def timedelta_to_hours(td):
    if not td:
        return "00:00:00"
    total_seconds = td.seconds
    hours = total_seconds // 3600
    minutes = (total_seconds - hours * 3600) // 60
    seconds = (total_seconds - hours * 3600 - minutes * 60)
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'