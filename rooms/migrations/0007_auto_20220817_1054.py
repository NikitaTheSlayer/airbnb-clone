# Generated by Django 2.2.5 on 2022-08-17 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_auto_20220817_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='rooms.Room'),
        ),
        migrations.AlterField(
            model_name='room',
            name='amenities',
            field=models.ManyToManyField(blank=True, related_name='rooms', to='rooms.Amenity'),
        ),
        migrations.AlterField(
            model_name='room',
            name='facilities',
            field=models.ManyToManyField(blank=True, related_name='rooms', to='rooms.Facility'),
        ),
        migrations.AlterField(
            model_name='room',
            name='house_rules',
            field=models.ManyToManyField(blank=True, related_name='rooms', to='rooms.HouseRule'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rooms', to='rooms.RoomType'),
        ),
    ]
