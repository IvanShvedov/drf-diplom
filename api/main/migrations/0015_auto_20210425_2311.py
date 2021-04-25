# Generated by Django 3.1.7 on 2021-04-25 20:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210420_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='cv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.cv'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='vacancy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.vacancy'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 25, 23, 11, 31, 678485), null=True),
        ),
        migrations.AlterField(
            model_name='cvresponse',
            name='date_response',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 25, 23, 11, 31, 682502), null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 25, 23, 11, 31, 680509), null=True),
        ),
        migrations.AlterField(
            model_name='vacancyresponse',
            name='date_response',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 25, 23, 11, 31, 682502), null=True),
        ),
    ]