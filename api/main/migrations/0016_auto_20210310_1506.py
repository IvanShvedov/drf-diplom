# Generated by Django 3.1.7 on 2021-03-10 12:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210310_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='pub_date',
            field=models.CharField(blank=True, default=datetime.datetime(2021, 3, 10, 15, 6, 55, 424713), max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='pub_date',
            field=models.CharField(blank=True, default=datetime.datetime(2021, 3, 10, 15, 6, 55, 426708), max_length=200, null=True),
        ),
    ]
