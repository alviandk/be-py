# Generated by Django 3.1 on 2021-02-18 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_auto_20210218_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='description',
        ),
    ]
