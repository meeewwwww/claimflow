from django.core.validators import RegexValidator
from django.db import models


class Flight(models.Model):
    flight_number = models.CharField(validators=[RegexValidator(r'CF[0-9]{4}')], verbose_name='Номер рейса',
                                     help_text='Номер рейса состоит из кода компании и четырех цифр, например, CF1234')
    departure_time_plan = models.TimeField(verbose_name='Планируемое время вылета')
    departure_time_fact = models.TimeField(verbose_name='Фактическое время вылета')
    arrival_time_plan = models.TimeField(verbose_name='Планируемое время прилета')
    arrival_time_fact = models.TimeField(verbose_name='Фактическое время прилета')
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий к рейсу',
                               help_text='Введите причину задержки вылета, прилета рейса или иные комментарии')