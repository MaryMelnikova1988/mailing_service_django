from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.CharField(max_length=150, verbose_name='email', unique=True)
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    father_name = models.CharField(max_length=150, verbose_name='Отчество')
    comment = models.TextField(verbose_name='Содержимое', **NULLABLE)

    def __str__(self):
        return f' {self.last_name} {self.first_name} {self.father_name} ({self.email})'

    class Meta:
        verbose_name = 'Клиент сервиса'
        verbose_name_plural = 'Клиенты Сервиса'


class Message(models.Model):
    title = models.CharField(max_length=250, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Тело письма', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Сообщение для рассылки'
        verbose_name_plural = 'Сообщения для рассылки'


class Mail(models.Model):
    PERIOD_CHOICES = [
        ('once_a_day', 'раз в день'),
        ('once_a_week', 'раз в неделю'),
        ('once_a_month', 'раз в месяц'),
    ]
    STATUS_CHOICES = [
        ('created', 'создана'),
        ('ended', 'завершена'),
        ('in_work', 'запущена'),
    ]
    name = models.CharField(max_length=100, verbose_name='Название рассылки', default='Рассылка')
    clients = models.ManyToManyField(Client, verbose_name='Кому (клиенты сервиса)')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name="Сообщение")
    date_start = models.DateField(verbose_name='Дата начала рассылки', default=timezone.now)
    date_end = models.DateField(verbose_name='Дата окончания рассылки', default=timezone.now)
    start_time = models.TimeField(verbose_name='Время рассылки', default=timezone.now)
    period = models.CharField(max_length=30, choices=PERIOD_CHOICES, verbose_name='Периодичность рассылки',
                              default='once_a_day')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, verbose_name='Статус рассылки',
                              default='created')
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    def __str__(self):
        return f'{self.name}: Дата начала: {self.date_start}, Дата окончания: {self.date_end}. Статус: {self.status}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Log(models.Model):

    STATUS_LOG = [('expected', 'ожидается'),
                ('failed', 'провалено'),
                ('completed', 'завершено'),
                ]

    mail = models.ForeignKey(Mail, on_delete=models.CASCADE, verbose_name='Рассылка')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    last_time_mail = models.DateTimeField(auto_now=True, verbose_name='дата и время последней попытки')
    status = models.CharField(max_length=50, choices=STATUS_LOG, verbose_name='Статус попытки')
    response = models.TextField(verbose_name='Ответ сервера', **NULLABLE)

    def __str__(self):
        return (f'Дата и время последней попытки: {self.last_time_mail}.'
                f' Статус попытки:{self.status}')

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'




