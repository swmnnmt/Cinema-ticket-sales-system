# Generated by Django 3.1.4 on 2021-01-21 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0008_auto_20210114_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showtime',
            name='free_seats',
            field=models.IntegerField(verbose_name='صندلی های خالی'),
        ),
        migrations.AlterField(
            model_name='showtime',
            name='saleable_seats',
            field=models.IntegerField(verbose_name='صندلی های قابل فروش'),
        ),
    ]
