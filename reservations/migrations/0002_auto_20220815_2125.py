# Generated by Django 2.2.5 on 2022-08-15 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='сreated',
            new_name='created',
        ),
    ]
