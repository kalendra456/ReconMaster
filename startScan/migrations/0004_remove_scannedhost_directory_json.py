# Generated by Django 3.1.5 on 2021-03-08 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0003_scanhistory_celery_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scannedhost',
            name='directory_json',
        ),
    ]
