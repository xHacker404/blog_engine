# Generated by Django 2.1.4 on 2019-03-05 10:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20190305_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 5, 11, 54, 1, 465764)),
        ),
    ]
