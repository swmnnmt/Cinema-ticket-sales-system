# Generated by Django 3.1.4 on 2021-01-11 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0003_auto_20210111_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='city',
            field=models.CharField(default='شیراز', max_length=30),
        ),
    ]
