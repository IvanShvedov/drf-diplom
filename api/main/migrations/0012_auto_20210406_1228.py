# Generated by Django 3.1.7 on 2021-04-06 09:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210405_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 6, 12, 27, 0, 15557), null=True),
        ),
        migrations.AlterField(
            model_name='cvresponse',
            name='cv',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='main.cv'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cvresponse',
            name='date_response',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 6, 12, 27, 0, 21541), null=True),
        ),
        migrations.AlterField(
            model_name='cvresponse',
            name='employer',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='cv_employer', to='main.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cvresponse',
            name='vacancy',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='main.vacancy'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cvresponse',
            name='worker',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='cv_worker', to='main.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 6, 12, 27, 0, 18548), null=True),
        ),
        migrations.AlterField(
            model_name='vacancyresponse',
            name='cv',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.cv'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vacancyresponse',
            name='date_response',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 6, 12, 27, 0, 21541), null=True),
        ),
        migrations.AlterField(
            model_name='vacancyresponse',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancy_employer', to='main.user'),
        ),
        migrations.AlterField(
            model_name='vacancyresponse',
            name='vacancy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.vacancy'),
        ),
        migrations.AlterField(
            model_name='vacancyresponse',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancy_worker', to='main.user'),
        ),
    ]