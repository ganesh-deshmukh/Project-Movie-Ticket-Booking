# Generated by Django 3.2 on 2021-04-24 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0015_showsfromtheater_theater'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showsfromtheater',
            name='theater',
        ),
    ]