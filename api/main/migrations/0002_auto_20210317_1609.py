# Generated by Django 3.1.7 on 2021-03-17 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='pub_date',
            field=models.CharField(blank=True, default='2021-03-17 16:09:44.954026', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='pub_date',
            field=models.CharField(blank=True, default='2021-03-17 16:09:44.956021', max_length=200, null=True),
        ),
    ]