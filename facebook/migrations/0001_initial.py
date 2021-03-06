# Generated by Django 3.0.8 on 2020-07-25 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profiler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=254)),
                ('bio', models.CharField(blank=True, max_length=254)),
                ('profile_url', models.CharField(blank=True, max_length=254)),
            ],
        ),
    ]
