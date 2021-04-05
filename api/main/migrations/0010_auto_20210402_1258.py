# Generated by Django 3.1.7 on 2021-04-02 09:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210402_1255'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Favoriete',
            new_name='Favorite',
        ),
        migrations.AlterField(
            model_name='cv',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 2, 12, 58, 51, 688635), null=True),
        ),
        migrations.AlterField(
            model_name='cvresponse',
            name='date_response',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 2, 12, 58, 51, 695616), null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 2, 12, 58, 51, 692623), null=True),
        ),
        migrations.AlterField(
            model_name='vacancyresponse',
            name='date_response',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 2, 12, 58, 51, 694617), null=True),
        ),
    ]