# Generated by Django 3.0.4 on 2020-03-21 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200321_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='helper',
            name='validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hospital',
            name='validated',
            field=models.BooleanField(default=False),
        ),
    ]