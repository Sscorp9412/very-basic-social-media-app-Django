# Generated by Django 3.0.8 on 2020-07-26 05:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiler',
            name='dob',
            field=models.DateField(default=datetime.datetime(2020, 7, 26, 5, 22, 46, 401929, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
