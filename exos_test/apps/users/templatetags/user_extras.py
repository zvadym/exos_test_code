import datetime
from django import template

register = template.Library()


@register.filter
def eligible(born):
    today = datetime.date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    # yes, we can use timedelta and do something like
    # age = (date.today() - birth_date) // timedelta(days=365.2425)
    # but I prefer first solution

    return 'allowed' if age > 13 else 'blocked'


@register.filter
def bizz_fuzz(value):
    result = ''

    # Python 3
    if not value % 3:
        result += 'Bizz'
    if not value % 5:
        result += 'Fuzz'

    return result if result else value
