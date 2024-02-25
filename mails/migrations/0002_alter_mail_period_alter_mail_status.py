# Generated by Django 4.2 on 2024-02-25 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='period',
            field=models.CharField(choices=[('раз в день', 'раз в день'), ('раз в неделю', 'раз в неделю'), ('раз в месяц', 'раз в месяц')], default='once_a_day', max_length=30, verbose_name='Периодичность рассылки'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='status',
            field=models.CharField(choices=[('создана', 'создана'), ('завершена', 'завершена'), ('запущена', 'запущена')], default='created', max_length=30, verbose_name='Статус рассылки'),
        ),
    ]
