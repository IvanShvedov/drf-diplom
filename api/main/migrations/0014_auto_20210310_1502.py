# Generated by Django 3.1.7 on 2021-03-10 12:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210310_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 10, 12, 2, 2, 894529, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 10, 12, 2, 2, 896515, tzinfo=utc), null=True),
        ),
    ]