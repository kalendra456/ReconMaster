# Generated by Django 3.1.5 on 2021-01-10 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0002_auto_20201109_0703'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanhistory',
            name='celery_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
