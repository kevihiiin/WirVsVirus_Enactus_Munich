# Generated by Django 3.0.4 on 2020-03-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0004_auto_20200322_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='helper',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
