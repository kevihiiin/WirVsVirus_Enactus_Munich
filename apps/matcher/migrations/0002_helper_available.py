# Generated by Django 3.0.4 on 2020-03-22 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='helper',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
