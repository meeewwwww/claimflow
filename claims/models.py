from django.core.validators import RegexValidator
from django.db import models

from employee.models import Flight


class Claim(models.Model):
    STATUSES = (
        ('in_progress', 'На рассмотрении'),
        ('completed', 'Рассмотрена'),
    )

    name = models.CharField(max_length=25, verbose_name='Имя', help_text='Имя пассажира')
    surname = models.CharField(max_length=50, verbose_name='Фамилия', help_text='Фамилия пассажира')
    booking_reference = models.CharField(unique=True, validators=[RegexValidator(r'[A-Za-z0-9]{8}')],
                                         verbose_name='Код бронирования',
                                         help_text='Код бронирования состоит из 8 символов (латинские буквы и цифры)')
    status = models.CharField(choices=STATUSES, default=STATUSES[0][1], verbose_name='Статус')
    flight_number = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='claims')
    email = models.EmailField()
    claim = models.TextField()
    attachment = models.FileField(upload_to='claim_attachment/%Y/%m/%d', default=None, blank=True,
                                  null=True, verbose_name='Приложение', help_text='Приложение должно быть одним файлом')