# Generated by Django 3.1.7 on 2021-04-02 09:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210401_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 2, 12, 55, 33, 623683), null=True),
        ),
        migrations.AlterField(
            model_name='cvresponse',
            name='date_response',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 2, 12, 55, 33, 631663), null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 2, 12, 55, 33, 626676), null=True),
        ),
        migrations.AlterField(
            model_name='vacancyresponse',
            name='date_response',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 2, 12, 55, 33, 629666), null=True),
        ),
        migrations.CreateModel(
            name='Favoriete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField(blank=True, default=-1, null=True)),
                ('item_type', models.CharField(blank=True, default='vacancy', max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
