# Generated by Django 2.0.6 on 2018-06-27 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geocontext', '0004_auto_20180627_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='contextgroup',
            name='context_service_registries',
            field=models.ManyToManyField(through='geocontext.ContextGroupServices', to='geocontext.ContextServiceRegistry'),
        ),
    ]
