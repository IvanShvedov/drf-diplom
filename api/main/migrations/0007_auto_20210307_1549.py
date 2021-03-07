# Generated by Django 3.1.7 on 2021-03-07 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210307_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='user',
        ),
        migrations.AddField(
            model_name='worker',
            name='education',
            field=models.JSONField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='worker',
            name='experience',
            field=models.JSONField(blank=True, max_length=500, null=True),
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='Experience',
        ),
    ]
