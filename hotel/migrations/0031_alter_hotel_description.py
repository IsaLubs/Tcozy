# Generated by Django 4.2.10 on 2024-04-14 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0030_booking_checked_in_tracker_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
