# Generated by Django 2.1.1 on 2018-10-15 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dota2', '0002_auto_20181015_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='created',
            field=models.DateTimeField(default=datetime.datetime),
        ),
    ]
