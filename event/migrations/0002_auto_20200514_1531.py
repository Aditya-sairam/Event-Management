# Generated by Django 2.2 on 2020-05-14 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='registration_name',
            new_name='registration_number',
        ),
    ]
