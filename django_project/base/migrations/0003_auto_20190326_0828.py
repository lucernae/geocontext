# Generated by Django 2.1.7 on 2019-03-26 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationsite',
            name='location_type',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='LocationSite',
        ),
        migrations.DeleteModel(
            name='LocationType',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
