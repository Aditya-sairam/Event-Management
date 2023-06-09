# Generated by Django 2.2 on 2020-05-19 06:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20200514_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date_registered',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='event',
            name='id_card',
            field=models.ImageField(upload_to='images'),
        ),
    ]
