# Generated by Django 3.0.4 on 2020-03-22 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0002_helper_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='helper',
            name='available_dates',
            field=models.IntegerField(default=28),
        ),
    ]
