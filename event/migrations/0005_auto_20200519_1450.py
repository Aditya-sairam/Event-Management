# Generated by Django 2.1 on 2020-05-19 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20200519_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='mobile_number',
            field=models.CharField(max_length=500, null=True),
        ),
    ]