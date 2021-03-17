# Generated by Django 3.1.7 on 2021-03-17 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20210310_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='city',
        ),
        migrations.AddField(
            model_name='worker',
            name='address',
            field=models.JSONField(blank=True, default=list, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='pub_date',
            field=models.CharField(blank=True, default='2021-03-17 14:41:45.416831', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employer',
            name='address',
            field=models.JSONField(blank=True, default=list, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='address',
            field=models.JSONField(blank=True, default=list, max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='pub_date',
            field=models.CharField(blank=True, default='2021-03-17 14:41:45.418822', max_length=200, null=True),
        ),
    ]
