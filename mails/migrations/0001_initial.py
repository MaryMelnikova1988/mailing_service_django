# Generated by Django 4.2 on 2024-02-24 16:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=150, unique=True, verbose_name='email')),
                ('last_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('father_name', models.CharField(max_length=150, verbose_name='Отчество')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Содержимое')),
            ],
            options={
                'verbose_name': 'Клиент сервиса',
                'verbose_name_plural': 'Клиенты Сервиса',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Тема письма')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Тело письма')),
            ],
            options={
                'verbose_name': 'Сообщение для рассылки',
                'verbose_name_plural': 'Сообщения для рассылки',
            },
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Рассылка', max_length=100, verbose_name='Название рассылки')),
                ('date_start', models.DateField(default=django.utils.timezone.now, verbose_name='Дата начала рассылки')),
                ('date_end', models.DateField(default=django.utils.timezone.now, verbose_name='Дата окончания рассылки')),
                ('start_time', models.TimeField(default=django.utils.timezone.now, verbose_name='Время рассылки')),
                ('period', models.CharField(choices=[('once_a_day', 'раз в день'), ('once_a_week', 'раз в неделю'), ('once_a_month', 'раз в месяц')], default='once_a_day', max_length=30, verbose_name='Периодичность рассылки')),
                ('status', models.CharField(choices=[('created', 'создана'), ('ended', 'завершена'), ('in_work', 'запущена')], default='created', max_length=30, verbose_name='Статус рассылки')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активна')),
                ('clients', models.ManyToManyField(to='mails.client', verbose_name='Кому (клиенты сервиса)')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mails.message', verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_time_mail', models.DateTimeField(auto_now=True, verbose_name='дата и время последней попытки')),
                ('status', models.CharField(choices=[('expected', 'ожидается'), ('failed', 'провалено'), ('completed', 'завершено')], max_length=50, verbose_name='Статус попытки')),
                ('response', models.TextField(blank=True, null=True, verbose_name='Ответ сервера')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mails.client', verbose_name='Клиент')),
                ('mail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mails.mail', verbose_name='Рассылка')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
            },
        ),
    ]
