# Generated by Django 3.1.7 on 2021-04-19 17:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210406_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 19, 20, 59, 10, 679087), null=True),
        ),
        migrations.AlterField(
            model_name='cvresponse',
            name='date_response',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 19, 20, 59, 10, 689060), null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 19, 20, 59, 10, 683080), null=True),
        ),
        migrations.AlterField(
            model_name='vacancyresponse',
            name='date_response',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 19, 20, 59, 10, 688064), null=True),
        ),
    ]