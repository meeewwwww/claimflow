from django.core.validators import RegexValidator
from django.db import models

from employee.models import Flight


class Claim(models.Model):
    STATUSES = (
        ('in_progress', 'На рассмотрении'),
        ('completed', 'Рассмотрена'),
    )

    name = models.CharField(max_length=25, validators=[RegexValidator(r'[A-Z]+')],
                            verbose_name='Имя', help_text='Имя пассажира как в загранпаспорте')
    surname = models.CharField(max_length=50,  validators=[RegexValidator(r'[A-Z]+')],
                               verbose_name='Фамилия', help_text='Фамилия пассажира как в загранпаспорте')
    booking_reference = models.CharField(unique=True, validators=[RegexValidator(r'[A-Z0-9]{8}')],
                                         verbose_name='Код бронирования',
                                         help_text='Код бронирования состоит из 8 символов (латинские буквы и цифры)')
    status = models.CharField(choices=STATUSES, default=STATUSES[0][1], verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата поступления претензии')
    flight_number = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='claims')
    email = models.EmailField()
    claim = models.TextField()
    attachment = models.FileField(upload_to='claim_attachment/%Y/%m/%d', default=None, blank=True,
                                  null=True, verbose_name='Приложение', help_text='Приложение должно быть одним файлом')

    def __str__(self):
        return f'{self.flight_number}, {self.booking_reference}, {self.created.strftime('%d %b %H:%M')}'