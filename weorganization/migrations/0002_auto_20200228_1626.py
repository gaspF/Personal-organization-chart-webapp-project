# Generated by Django 3.0.3 on 2020-02-28 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weorganization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='starting_time',
            field=models.TimeField(default=datetime.datetime(2020, 2, 28, 16, 26), verbose_name='Heure de début'),
        ),
    ]