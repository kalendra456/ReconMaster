# Generated by Django 3.1.2 on 2020-11-09 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scannedhost',
            name='directory_json',
            field=models.JSONField(null=True),
        ),
    ]
